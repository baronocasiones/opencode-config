---
description: Load module context based on session goal
---

Execute the Start protocol with this instruction: $ARGUMENTS

1. Parse the instruction to identify the target module and session goal.

2. Read the local AGENTS.md in the project root for session history. If it exists, note the most recent sessions and conventions.

3. Read the corresponding docs/ file for that module. If it does not exist, report that and ask what to work on.

4. If the file exists, display:
   - Current state of the module
   - What has been completed across previous sessions
   - What remains to be done
   - Any conventions or patterns established for this module

5. Set up context and wait for instructions. Do not begin work until the user confirms.
