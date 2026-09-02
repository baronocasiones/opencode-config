## Donts 
- make sure to not populate unnecessary .md files unless I told you so. 
- don't make any duplicate .md files, just update the existing ones

## State-Freeze Workflow

### /end
Auto-archive session. Analyze all changes, update relevant docs/*.md files (additive only), append session context to the local project AGENTS.md. Create local AGENTS.md via /init if missing.

### /start
Load context from local AGENTS.md and docs/ based on user instruction. Display current state, completed work, remaining work, and conventions. Wait for user confirmation before proceeding.
