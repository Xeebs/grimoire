Publish all skills in skills/ that have passed testing and are marked ready. For each skill:
1. Verify gh auth status — abort if unauthenticated
2. Run final quality check against the criteria in CLAUDE.md
3. git add and commit the skill directory with message: feat(skills): add {skill-name} for {industry}
4. git push to Xeebs/grimoire main
5. Create a GitHub Discussion in Announcements announcing the skill
6. Send a push notification
7. Log the publish to pipeline/published.md
8. Update the signal status to PUBLISHED in pipeline/queue.md
