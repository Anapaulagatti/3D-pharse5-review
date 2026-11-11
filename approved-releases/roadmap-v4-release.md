V4 public review release — owner authorized exact payload

Artifact: e5f2e4ddfe5ce6d611172302cada81b56c51dcbc
Manifest SHA256: 5a00ce7bae1aedb00a1904006f4bdfab79c58d96c4fded41aa85ae840759c4ee
Files: 868 plus unchanged export-manifest.json.
Source runtime: 21cc539259853952c91e548fb782cbd6df2e8785.

Owner explicitly approved this exact artifact/manifest and updating review Pages in chat. Receipt records processing time, not an authenticated message timestamp. This is public gameplay preview permission, not commercial/legal/artistic/Korean-language/device certification. No approved payload file was rebuilt or changed for deployment.

The existing review-pages.yml workflow retains receipt, exact byte/hash, historical archive, protected-environment and real HTTPS browser gates. Review controls add QA for V4; they are not added to the published manifest. Failed local verifier rehearsals were QA mistakes (trade cooldown, workshop approach coordinates, asynchronous readback), corrected without touching game/art.

Rollback: checkpoint/pages-v2-before-v4-20261111 -> 671d267e5c3c49eceb2578dbdc847d1bb92eb136, manifest cdf3f6d5b117a4912fda9d88c2dc12d1cdfeded4ba39ca343bab217918b578db. Old approved V2 receipt remains approved-releases/history/roadmap-v2.approved.json. To restore, use the existing workflow_dispatch operation=deploy with that receipt path and required github-pages reviewer; verify live manifest and actual gameplay. Do not force-push or delete history. The older1a immutable archive and all six snapshot manifests remain byte-verified.

The source game's main and production v0.5 remain untouched. Physical Android/iPhone/GPU NOT TESTED. No Phase3B-E, backend, multiplayer or ads authorized. A successful deployment job alone is not gameplay verification.
