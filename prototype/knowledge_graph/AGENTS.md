# Knowledge-graph prototype

This directory is an isolated, non-operational prototype. Read `README.md`,
`GOAL_BRIEF.md`, and `docs/design.md` before changing its behavior.

- Only edit inside this directory. The parent evidence archive and the Wave 4
  experiment are read-only. Preserve the existing dirty worktree.
- Source quotations, publication dates, observation times, interpretations, and
  compliance results are different things. Do not merge them.
- Never interpret a missing fact as false or as not applicable. Never turn a
  stored bulletin, route direction, or source-text conflict into a clearance.
- No real driver identifiers, credentials, production data, or secret values.
- The local dependency allowance is the already installed NetworkX 3.6.1 and
  Python 3.11 standard library. Do not add dependencies or unrelated refactors.
- Do not delete, skip, weaken, or narrow tests to make a goal pass.
- New test expectations are prototype assertions, not human-approved policy.
- Do not create ADRs. Write concise, targeted documentation for changes.
- Run `python3 -m unittest discover -s tests -v` after each checkpoint. Review
  the diff and do an extra adversarial QA pass before declaring completion.
- Consumer-app testing requires a captured tool call and response. An API,
  CLI, or manual copy/paste test is not a consumer-app connector test.
- Ask before public hosting, new dependencies, purchases, changing account
  security, or changing production/application configuration.

