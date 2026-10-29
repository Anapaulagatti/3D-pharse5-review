# 3D-pharse5-review

## Deployment status: NOT DEPLOYED

This repository contains deployment controls only. The compiled Phaser Review Portal and artwork have NOT been pushed here. Owner public-exposure approval remains PENDING. No Phase3B-B/C/D is authorized.

The workflow deploys an existing, pinned compiled-site commit: no npm install, Vite rebuild, NPC/art generation or gameplay-source checkout. Both manual deployments and automatic updates require an exact manifest and completed individual exposure records, then the protected github-pages environment. Commercial release remains BLOCKED_PENDING_REVIEW.

### First owner setup

1. In Settings → Pages, select GitHub Actions. In Settings → Environments → github-pages, require owner review, restrict to main and protect approved-releases records. API/settings access must actually work; these settings are not claimed configured by this commit.
2. Review the pending candidate record under review-candidates. Resolve each specific depiction concern or exclude it in a functioning public-safe subset; do not treat fictional names or a boolean as clearance. One consolidated owner decision may cover all individual records. Do not publish artwork while this record is PENDING.
3. Only after explicit public-exposure approval, push the matching already-compiled artifact commit to an immutable version branch in this review repository. Verify the branch and exact manifest; no source rebuild is needed.
4. Commit the signed-off record to approved-releases/current.approved.json and retain an immutable copy under approved-releases/history/<phase>.approved.json. A push of an approved record starts the same Pages workflow automatically. The protected environment still requires owner review before upload.
5. Confirm the actual deployment page_url and playable HTTPS site, desktop/mobile controls, all26NPCs, clock, snapshots and console before announcing a live link. This repo README or a successful Git push is not a playable deployment.

### History and rollback

Each compiled release must include the earlier immutable phases directories and history links. history_gate.py rejects removal or modification of a recorded snapshot manifest. Retain all compiled version branches and their Git history; never force-push. For rollback, prepare a new compiled distribution whose current root selects the older approved snapshot while retaining ALL existing phase snapshots, obtain approval for its exact manifest, and promote via the same receipt workflow. No gameplay rebuild or production-site change is required.

### Safety boundary

The project path is /3D-pharse5-review/. Normal and QA saves are isolated from the existing v0.5 project site, which shares the github.io origin. The original game's repository, Pages workflow and artwork are untouched. No tokens or private source/audit materials belong in this repository. A noindex tag is not access control.
