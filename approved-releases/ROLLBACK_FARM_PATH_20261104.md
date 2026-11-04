# Exact farm/path rollback

Before hotfix promotion, actualHTTPSmanifest17306fc4/3570files and previous run41760249901success confirmed. Current live artifact9fce709a is tagged checkpoint/pages-9fce709a-before-farm-path-20261104 and its byte-exact receipt retained at approved-releases/rollback/phase3bd-9fce709a.approved.json. Earlierfff156b6 is preserved too.

Rollback: existing Publish workflow dispatch operationdeploy and approval_path approved-releases/rollback/phase3bd-9fce709a.approved.json. Required github-pages reviewer remains enforced; do not rebuild, alter historical snapshots or touch productionv0.5. Verify actualHTTPSmanifest17306fc4 and browser gameplay after rollback. This is a recovery reference, not a claim that rollback was performed.
