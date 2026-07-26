# OpenCode Config

Personal OpenCode configuration — custom agents, MCP servers, skills, and a `setup.sh` script to bootstrap everything on a fresh environment.

## Quickstart

```bash
git clone <repo-url>
cd opencode
./setup.sh
```

That single command will:
1. Rename the directory to `opencode` (if it isn't already)
2. Move it to `~/.config/opencode` (prompting before overwriting an existing directory)
3. Re-execute itself from the new location with all paths corrected
4. Install npm dependencies
5. Install external skills (humanizer, terminal-skills, etc.)
6. Print a summary of what's installed and what's missing

### Platform support

| OS/Shell | Status |
|---|---|
| Linux (Debian/Ubuntu) | ✅ Full support via `apt-get` |
| Linux (Arch) | ✅ Full support via `pacman` |
| macOS | ✅ Full support via `brew` |
| Windows (Git Bash/MSYS2) | ✅ Full support via `choco` |
| Windows (WSL) | ✅ Runs as native Linux (uses WSL's `apt-get`) |
| Windows (PowerShell/cmd) | ❌ Not supported — use Git Bash or WSL |

If you're already at `~/.config/opencode`, the relocation step is skipped.

### Flags

| Flag | Description |
|---|---|
| `-y` / `--yes` | Skip all prompts (auto-confirm overwrite) |
| `--with-python` | Install Python ML packages (transformers, torch) + PDF tools |
| `--with-system` | Install system packages (poppler/qpdf/tesseract) |

All three can be combined:
```bash
./setup.sh -y --with-python --with-system
```

### Windows (Git Bash + Chocolatey) setup

The script natively detects Git Bash / MSYS2 / Cygwin via `uname -s` and handles Windows paths and cross-filesystem moves correctly. To get started on Windows:

**Prerequisites:**
- [Git for Windows](https://git-scm.com) (provides Git Bash)
- [Node.js](https://nodejs.org) — `choco install nodejs`
- [Chocolatey](https://chocolatey.org/install) — required for `--with-system` flag

**Run:**
```bash
# Basic setup (npm + skills) — any Git Bash terminal
./setup.sh

# Full setup with system deps — requires elevated (Run as Administrator) Git Bash
./setup.sh -y --with-system --with-python
```

The script will auto-detect Chocolatey and run `choco install -y poppler qpdf tesseract` when `--with-system` is passed. Python is detected as `python` (not `python3`) on Windows — the fallback is built in.

## How `setup.sh` Works

The script runs in 8 phases:

| Phase | Step | Description |
|---|---|---|
| **1** | **Auto-relocation** | Detects if the clone lives outside `~/.config/opencode`, renames it to `opencode`, and moves it there. Checks for unpushed/dirty git state before overwriting. Re-execs from the new location. |
| **2** | **Prerequisites** | Checks for `node`, `npm`/`bun`, and Python (`python3` → falls back to `python` on Windows). |
| **3** | **npm dependencies** | Runs `npm install` (or `bun install`) to install the OpenCode plugin. |
| **4** | **Skill installation** | Installs external skills (humanizer via `skills add`, optional skills via `terminal-skills`). |
| **5** | **Python deps** | (optional) Installs `transformers`, `torch`, `pypdf`, `pdfplumber`, `reportlab`. |
| **6** | **System deps** | (optional) Auto-detects package manager: `apt-get` → `pacman` → `brew` → `choco`. Installs `poppler`/`qpdf`/`tesseract` with correct package names per platform. |
| **7** | **Environment vars** | Checks for required env vars (`FIGMA_MCP_TOKEN`, `GOOGLE_STITCH_MCP_TOKEN`) and creates `.env.example`. |
| **8** | **Summary** | Lists all found skills (in-repo + external) and next steps. |

## Installed Plugin

This config uses the `@opencode-ai/plugin` npm package (v1.3.17), tracked in `package.json`. Run `./setup.sh` or `npm install` to keep it updated.

## Skills

### Bundled in this repo (auto-discovered by OpenCode)

| Skill | Directory | Purpose |
|---|---|---|
| **ai-detector** | `skills/ai-detector/` | 11-signal heuristic + optional HuggingFace ML model to detect AI-generated text. Used by the student agent for self-verification before delivering output. |
| **backend-tester** | `skills/backend-tester/` | Analyzes logs and creates comprehensive backend test files. |
| **frontend-tester** | `skills/frontend-tester/` | Tests UI, creates automation scripts, validates user interactions. |
| **ui-analyzer** | `skills/ui-analyzer/` | Analyzes UI from images/project descriptions to create design specs. |
| **ui-designer** | `skills/ui-designer/` | Creates and analyzes modern, responsive UI designs. |

### Installed in `~/.agents/skills/` (by `setup.sh`)

| Skill | Source | Purpose |
|---|---|---|
| **humanizer** | [blader/humanizer](https://github.com/blader/humanizer) | Strips AI writing patterns from text. Removes inflated symbolism, promotional language, em dash overuse, hedging, and other detectable signals. |
| **caveman** | terminal-skills | Ultra-compressed communication mode (cuts token usage ~75%). |
| **create-readme** | terminal-skills | Creates README documentation for projects. |
| **design-taste-frontend** | terminal-skills | Anti-slop frontend skill for landing pages and portfolios. |
| **find-skills** | terminal-skills | Discovers and installs agent skills. |
| **full-output-enforcement** | terminal-skills | Enforces complete code generation (no placeholders, no truncation). |
| **gws-docs** | terminal-skills | Read and write Google Docs. |
| **high-end-visual-design** | terminal-skills | Premium agency-level visual design system. |
| **industrial-brutalist-ui** | terminal-skills | Mechanical, Swiss-typographic interfaces. |
| **minimalist-ui** | terminal-skills | Clean editorial-style warm monochrome interfaces. |
| **pdf** | terminal-skills | Full PDF manipulation (read, merge, split, OCR, encrypt, etc.). |
| **redesign-existing-projects** | terminal-skills | Upgrades existing websites to premium quality. |
| **supabase** | terminal-skills | Supabase integration (Auth, Database, Edge Functions, Realtime, etc.). |
| **supabase-postgres-best-practices** | terminal-skills | Postgres performance optimization from Supabase. |
| **ui-ux-pro-max** | terminal-skills | Comprehensive UI/UX design with 50+ styles, 161 palettes, 57 font pairings. |

## Agents

### Main agents (`agents/`)

| Agent | File | Purpose |
|---|---|---|
| **Main** | `agents/main-agent.md` | Primary general-purpose agent. |
| **Student** | `agents/student.md` | Academic agent with anti-hallucination research workflow, human-sounding output (humanizer + ai-detector), and source integrity enforcement. Temperature: 0.82. |
| **Designer** | `agents/designer.md` | UI/UX agent. |
| **Tester** | `agents/tester.md` | Software testing agent. |
| **Plan** | `agents/plan.md` | Planning and task-breakdown agent. |

### Sub-agents (`agents/subagent/`)

| Sub-agent | Purpose |
|---|---|
| **coder** | Code writing, debugging, refactoring. |
| **research-synthesis** | Deep multi-source research and synthesis. Temperature: 0.78. |
| **documentation-writer** | Structured technical documentation. Temperature: 0.7. |
| **data-analysis-agent** | Data processing, stats, visualization. Temperature: 0.72. |
| **devops-agent** | CI/CD, Docker, deployment. |
| **security-reviewer** | Code/config/dependency vulnerability audits. |
| **accessibility-reviewer** | WCAG and inclusive design audits. |
| **image-media-agent** | Diagrams, illustrations, and visual assets using SVG, Mermaid, and programmatic generation (free). |
| **project-context-loader** | Project documentation loading and caching. |

## MCP Servers

Configured in `opencode.json`:

| Server | Type | Purpose |
|---|---|---|
| **server-filesystem** | Local | Filesystem access to `/mnt/hdd/repo/`, `~/.config/`, `/mnt/hdd/Downloads/` |
| **context7-mcp** | Remote | Up-to-date library/framework documentation |
| **framelink-figma-mcp** | Local | Figma file data and image export via `FIGMA_MCP_TOKEN` |
| **chrome-devtools-mcp** | Local | Browser automation, screenshots, performance traces |
| **google-stitch-mcp** | Remote | UI generation and editing via Gemini, needs `GOOGLE_STITCH_MCP_TOKEN` |
| **github-mcp** | Remote | GitHub API (disabled by default), needs `GITHUB_MCP_TOKEN` |

### Required environment variables

```
export FIGMA_MCP_TOKEN="your_figma_personal_access_token"
export GOOGLE_STITCH_MCP_TOKEN="your_google_stitch_api_key"
```

Optional:
```
export GITHUB_MCP_TOKEN="your_github_token"
```

## File Structure

```
~/.config/opencode/
├── AGENTS.md              # Agent behavior rules
├── README.md              # This file
├── opencode.json          # MCP server config
├── tui.json               # Terminal UI config
├── package.json           # npm dependencies (@opencode-ai/plugin)
├── setup.sh               # Bootstrap script
├── .env.example           # Env var template
├── agents/
│   ├── main-agent.md
│   ├── student.md
│   ├── designer.md
│   ├── tester.md
│   ├── plan.md
│   └── subagent/          # 9 sub-agent definitions
└── skills/
    ├── ai-detector/       # Bundled AI text detector
    ├── backend-tester/
    ├── frontend-tester/
    ├── ui-analyzer/
    └── ui-designer/
```
