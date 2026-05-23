# claude-code-security-review bypass PoC

This repo demonstrates a logic-flaw bypass in `anthropics/claude-code-security-review`
where committing `.claudecode-marker/marker.json` to a PR causes the security scanner
to skip itself entirely.

See PR #1 for the PoC.
