# Local validation corrections · 2026-11-11

Canvas full suite at 9b937216: 80 PASS / 2 FAIL, zero skipped/flaky. The complete report and log are preserved in canvas-9b-full/.

## Exact interior position

Workshop reload restored [319.1522417329603,326.1483824273696] instead of the live [320.33028163041706,324.97034252991284]. The room only saved each 500 simulation ms. A frame could remain unsaved after releasing movement even after a wall-clock delay under slow rendering. The scene now saves on the moving-to-stopped transition and on pagehide/visibilitychange. Closing guards and abortable scene listeners prevent resurrecting a removed room save. Movement, collision, anchors and approved artwork are unchanged.

The first focused workshop + Jeju rerun after the persistence fix passed 2/2 in 51.4s. This is focused evidence only, not a clean full suite. The three original room tests additionally verify that pagehide after exit does not resurrect a room save.

## Read-only collision overlay

The Jeju failure was a 120s total test timeout; a focused rerun on the same old overlay passed. A unique historical cause is therefore NOT established. The old diagnostic replayed one Graphics rectangle per visible 8px sample every rendered frame (approximately 14,400 at 1280x720), even though samples refreshed only every 250ms. It now rasterizes the same queries/colors/alpha at the same cadence into one native, nearest-filtered CanvasTexture. Dynamic foot/zone/landmark outlines are retained. This changes diagnostic rendering only, not any passability query, player physics, camera, base artwork or mask.

A fresh full-suite result remains required. Default AUTO/SwiftShader 81/82 at 9b is retained separately; this optimization is not proof of a WebGL fix. Physical hardware remains NOT TESTED.

## Final complete Canvas regression run

Full clean validation35e0b405:236/236unit and82/82CanvasE2E,0failed/flaky/skipped/retries. This is a fresh complete run, not combined focused results. The compiled game remains21cc5392;35e0b405 changes only the landmark-snapshot await in the test. Source equivalence is recorded separately. The old full81/82and80/82results remain archived. Default AUTO/WebGL and physical hardware are separate unresolved acceptance categories.
