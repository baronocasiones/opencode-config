---
description: Archive session state to docs and update local AGENTS.md
---

Execute the End protocol.

1. Analyze this session: all file changes, API endpoints defined, dependencies added, conventions established, patterns used.

2. For each relevant module, update the corresponding file in docs/:
   - Create the file if it does not exist
   - Append only — never remove existing content
   - Only update files relevant to what was actually changed

3. Check if a local AGENTS.md exists in the project root. If not, invoke the /init command to create it. Then append a session entry under ## Session History with:
   - Date and module name
   - What was implemented
   - Any new conventions or patterns established

4. Print: "[end] Session archived. docs/ updated. AGENTS.md updated."
