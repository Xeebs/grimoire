Address feedback from a GitHub Issue on a published Grimoire skill. Usage: /project:fix-issue {issue-number}

Steps:
1. Fetch the issue from Xeebs/grimoire using gh
2. Identify which published skill the issue references
3. Read the current SKILL.md and README.md for that skill
4. Analyze the feedback and propose specific improvements
5. Update the skill files, re-run test scenarios to verify the fix
6. Commit the update with message: fix(skills): address issue #{number} in {skill-name}
7. Push to Xeebs/grimoire and close the issue with a comment
