# Fresh regression harness timing diagnosis

Initial full2026-11-04run:69PASS/2FAIL. Mobile Korean-answer test expected20coins from the readonly window snapshot immediately after tapping; snapshot still0, while captured DOM already displayed20coins/completed quest. Visitor-window test closed shop, then read the previous paused=true snapshot even though conversation was closed and NPC interaction control restored.

The game commits inventory/reward and releases its UI lock synchronously. NPCManager publishes window.__NPC_WORLD__ at the end of update (src/npcs/manager.ts:542); main publishes window.__GATE3__ including paused once per frame (src/gate3/main.ts:656). These are observation snapshots, not synchronous command results. Initial follow-up fixed coins polling and exposed the same immediate paused assertion later in the mobile test. Both coin and close assertions now wait for the same exact expected value using normal expect.poll; no game logic,assertion value or timeout threshold changed.

Keep original full/first follow-up failures in reports. Final repeated follow-up results are separate, not relabeled as a clean original full run. No product fix is claimed for a test observation race. Prior lost2026-11-03results remain historical only.
