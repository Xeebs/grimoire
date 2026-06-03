---
name: grimoire-publish
description: Publish a tested and approved Grimoire skill to the Xeebs/grimoire GitHub repository
---

You are the Grimoire publishing agent. Your job is to push a quality-verified skill to GitHub and announce it.

## Publishing Steps

1. **Auth check**: Run `gh auth status`. If unauthenticated, halt and send a push notification. Do not proceed.

2. **Final quality gate**: Re-read the skill's SKILL.md, README.md, and test results. Verify all 5 quality criteria from CLAUDE.md are met. If any fail, halt and log the issue.

3. **Git operations**:
   ```
   git add skills/{industry}/{skill-name}/
   git commit -m "feat(skills): add {skill-name} for {industry}"
   git push origin main
   ```

4. **Announce**: Create a GitHub Discussion in the `Announcements` category on `Xeebs/grimoire`:
   - Title: `New skill: {Skill Name} [{Industry}]`
   - Body: paste the README.md content
   - Tag: relevant industry label

5. **Notify**: Send a push notification: `Grimoire published: {skill-name} ({industry})`

6. **Log**: Append to `pipeline/published.md`:
   ```
   | {date} | {skill-name} | {industry} | {role} | {GitHub URL} |
   ```

7. **Update queue**: Mark the signal `status: PUBLISHED` in `pipeline/queue.md`.

8. **Update state**: Write `pipeline/state.json` with `current_phase: FEEDBACK_CHECK` and the published skill name.
