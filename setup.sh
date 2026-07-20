#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_TARGET="${HOME}/.agents/skills"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

info()  { echo -e "${GREEN}[✓]${NC} $1"; }
warn()  { echo -e "${YELLOW}[!]${NC} $1"; }
err()   { echo -e "${RED}[✗]${NC} $1"; }
header(){ echo -e "\n${CYAN}━━━ $1 ━━━${NC}"; }

echo -e "${CYAN}
╔══════════════════════════════════════╗
║   OpenCode Config Setup             ║
║   ${SCRIPT_DIR}  ║
╚══════════════════════════════════════╝${NC}"

# ── Parse flags ─────────────────────────────────────────────────────
AUTO_YES=0
WITH_PYTHON=0
WITH_SYSTEM=0
REMAINING_ARGS=()
for arg in "$@"; do
  case "$arg" in
    -y|--yes)      AUTO_YES=1 ;;
    --with-python) WITH_PYTHON=1 ;;
    --with-system) WITH_SYSTEM=1 ;;
    *)             REMAINING_ARGS+=("$arg") ;;
  esac
done
set -- "${REMAINING_ARGS[@]}"

# ── Phase 1: Auto-relocation ───────────────────────────────────────
header "Checking installation path"

TARGET_DIR="${HOME}/.config/opencode"
CURRENT_NAME="$(basename "$SCRIPT_DIR")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

if [ "$SCRIPT_DIR" = "$TARGET_DIR" ]; then
  info "Already at ${TARGET_DIR}"
else
  echo ""
  echo "  This clone lives at: ${SCRIPT_DIR}"
  echo "  OpenCode expects it at: ${TARGET_DIR}"
  echo ""

  # Step 1: Rename to 'opencode' if not already
  if [ "$CURRENT_NAME" != "opencode" ]; then
    echo "  Renaming ${CURRENT_NAME} → opencode..."
    mv "$SCRIPT_DIR" "${PARENT_DIR}/opencode" 2>/dev/null || {
      err "Failed to rename directory (permissions?)"
      exit 1
    }
    SCRIPT_DIR="${PARENT_DIR}/opencode"
    info "Renamed to opencode"
  fi

  # Step 2: Check if target already exists
  if [ -d "$TARGET_DIR" ]; then
    HAS_UNPUSHED=0
    if [ -d "${TARGET_DIR}/.git" ]; then
      git -C "$TARGET_DIR" log --oneline @{u}..HEAD 2>/dev/null | grep -q . && HAS_UNPUSHED=1
      git -C "$TARGET_DIR" status --porcelain 2>/dev/null | grep -q . && HAS_UNPUSHED=1
    fi

    warn "${TARGET_DIR} already exists!"
    if [ "$HAS_UNPUSHED" = 1 ]; then
      echo "  ⚠  The existing directory has unpushed commits or dirty files!"
      echo "  It will be PERMANENTLY REMOVED."
    else
      echo "  It will be PERMANENTLY REMOVED and replaced."
    fi
    echo ""

    if [ "$AUTO_YES" != 1 ]; then
      read -p "  Continue? [y/N] " -n 1 -r
      echo ""
      if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        err "Relocation aborted by user"
        exit 1
      fi
    fi

    rm -rf "$TARGET_DIR"
    info "Removed existing ${TARGET_DIR}"
  fi

  # Step 3: Move to target (handles cross-filesystem)
  mkdir -p "${HOME}/.config"
  if ! mv "$SCRIPT_DIR" "$TARGET_DIR" 2>/dev/null; then
    echo "  Cross-filesystem move detected, using copy..."
    cp -a "$SCRIPT_DIR" "$TARGET_DIR" && rm -rf "$SCRIPT_DIR"
  fi
  info "Moved to ${TARGET_DIR}"

  # Step 4: Re-exec from new location
  echo ""
  echo "  Relocation complete. Re-executing from new location..."
  exec "$TARGET_DIR/setup.sh" "$@"
fi

# ── Phase 2: Prerequisites ──────────────────────────────────────────
header "Checking prerequisites"

command -v node >/dev/null 2>&1 || { err "node is required. Install from https://nodejs.org"; exit 1; }
info "node $(node -v)"

if command -v bun >/dev/null 2>&1; then
  PKG_MGR="bun"
  INSTALL_CMD="bun install"
  info "bun $(bun --version) detected"
elif command -v npm >/dev/null 2>&1; then
  PKG_MGR="npm"
  INSTALL_CMD="npm install"
  info "npm detected"
else
  err "npm or bun is required"
  exit 1
fi

command -v python3 >/dev/null 2>&1 || warn "python3 not found — ai-detector and PDF skill will not work"
python3 --version 2>/dev/null && info "python3 $(python3 --version | cut -d' ' -f2)" || true

# ── Phase 3: npm dependencies ──────────────────────────────────────
header "Installing npm dependencies"

cd "$SCRIPT_DIR"
if [ -f "package.json" ]; then
  $INSTALL_CMD
  info "npm dependencies installed"
else
  warn "package.json not found — skipping npm install"
fi

# ── Phase 4: Skill installation ─────────────────────────────────────
header "Installing skills"

mkdir -p "$SKILLS_TARGET"

install_skill_via_npx() {
  local skill_name="$1"
  local npx_pkg="$2"
  if [ ! -d "${SKILLS_TARGET}/${skill_name}" ]; then
    echo "  Installing ${skill_name}..."
    if npx "$npx_pkg" 2>/dev/null; then
      info "${skill_name} installed"
    else
      warn "Could not install ${skill_name} — skipping"
    fi
  else
    info "${skill_name} already installed"
  fi
}

# Humanizer — the most critical skill
if [ ! -d "${SKILLS_TARGET}/humanizer" ]; then
  echo "  Installing humanizer..."
  if command -v npx >/dev/null 2>&1; then
    if npx -y skills add blader/humanizer --path "$SKILLS_TARGET" 2>/dev/null; then
      info "humanizer installed via skills CLI"
    else
      echo "  Trying git clone..."
      git clone --depth 1 https://github.com/blader/humanizer.git "${SKILLS_TARGET}/humanizer" 2>/dev/null && \
        info "humanizer installed via git" || \
        warn "Could not install humanizer — try: npx skills add blader/humanizer"
    fi
  else
    warn "npx not available — cannot install humanizer"
  fi
else
  info "humanizer already installed"
fi

# terminal-skills meta-skill (enables the agent to find more skills)
if ! command -v terminal-skills >/dev/null 2>&1; then
  echo "  Installing terminal-skills CLI..."
  npm install -g terminal-skills 2>/dev/null && info "terminal-skills CLI installed" || warn "Could not install terminal-skills CLI"
fi

# Try to install skills from terminalskills.io that might be available
TERMINAL_SKILLS=("pdf" "supabase" "gws-docs")
for skill in "${TERMINAL_SKILLS[@]}"; do
  if [ ! -d "${SKILLS_TARGET}/${skill}" ]; then
    echo "  Looking up ${skill} on terminalskills.io..."
    npx terminal-skills install "$skill" 2>/dev/null && info "${skill} installed" || \
      warn "${skill} not found on terminalskills — may need manual install"
  else
    info "${skill} already installed"
  fi
done

# ── Phase 5: Python dependencies (optional) ─────────────────────────
header "Python dependencies"

if command -v python3 >/dev/null 2>&1; then
  if [ "$WITH_PYTHON" = 1 ]; then
    echo "  Installing Python packages for ML detection..."
    pip3 install transformers torch --quiet 2>/dev/null && \
      info "Python ML packages installed" || \
      warn "Could not install transformers/torch"
    echo "  Installing Python packages for PDF skill..."
    pip3 install pypdf pdfplumber reportlab --quiet 2>/dev/null && \
      info "Python PDF packages installed" || \
      warn "Could not install PDF packages"
  else
    echo "  Skipping Python packages (use --with-python to install)"
  fi
fi

# ── Phase 6: System dependencies (optional) ─────────────────────────
header "System dependencies"

if [ "$WITH_SYSTEM" = 1 ]; then
  if command -v apt-get >/dev/null 2>&1; then
    echo "  Installing system packages..."
    sudo apt-get update -qq && sudo apt-get install -y -qq poppler-utils qpdf tesseract-ocr 2>/dev/null && \
      info "System packages installed" || \
      warn "Could not install all system packages"
  elif command -v brew >/dev/null 2>&1; then
    echo "  Installing system packages via brew..."
    brew install poppler qpdf tesseract 2>/dev/null && \
      info "System packages installed" || \
      warn "Could not install all system packages"
  else
    warn "No package manager detected — install manually: poppler-utils, qpdf, tesseract-ocr"
  fi
else
  echo "  Skipping system packages (use --with-system to install)"
fi

# ── Phase 7: Environment variables ──────────────────────────────────
header "Environment variables"

MISSING_ENV=0
check_env() {
  if [ -z "${!1:-}" ]; then
    warn "$1 is not set"
    MISSING_ENV=1
  else
    info "$1 is set"
  fi
}

check_env "FIGMA_MCP_TOKEN"
check_env "GOOGLE_STITCH_MCP_TOKEN"

if [ ! -f "${SCRIPT_DIR}/.env.example" ]; then
  cat > "${SCRIPT_DIR}/.env.example" << 'EOF'
# Required for Figma MCP
export FIGMA_MCP_TOKEN="your_figma_personal_access_token"

# Required for Google Stitch MCP
export GOOGLE_STITCH_MCP_TOKEN="your_google_stitch_api_key"

# Optional: GitHub MCP (disabled by default)
export GITHUB_MCP_TOKEN="your_github_token"
EOF
  info ".env.example created"
fi

if [ "$MISSING_ENV" -eq 1 ]; then
  echo "  Set missing variables in your shell rc file or copy .env.example to .env and source it."
fi

# ── Phase 8: Summary ────────────────────────────────────────────────
header "Summary"

LOCAL_REPO_SKILLS=()
for d in "${SCRIPT_DIR}/skills/"*/; do
  [ -d "$d" ] && LOCAL_REPO_SKILLS+=("$(basename "$d")")
done

INSTALLED_SKILLS=()
for d in "${SKILLS_TARGET}/"*/; do
  [ -d "$d" ] && INSTALLED_SKILLS+=("$(basename "$d")")
done

echo "  Skills in repo:     ${LOCAL_REPO_SKILLS[*]:-(none)}"
echo "  Skills in ~/.agents: ${INSTALLED_SKILLS[*]:-(none)}"

if [ ${#INSTALLED_SKILLS[@]} -eq 0 ]; then
  warn "No external skills installed in ~/.agents/skills/"
  echo "  Re-run this script or install skills manually:"
  echo "    npx skills add blader/humanizer"
  echo "    npx terminal-skills install <name>"
fi

info "Setup complete!"
echo ""
echo "  Next steps:"
echo "    1. Source your env vars:     source .env (or add to ~/.bashrc)"
echo "    2. Install Python deps:      $0 --with-python"
echo "    3. Install system deps:      $0 --with-system"
echo "    4. Open OpenCode and verify skills are detected"
echo ""
