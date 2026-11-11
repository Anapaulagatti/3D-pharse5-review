# Performance · bounded browser evidence

Cloud Chromium 154.0.8037.57; CPU INTEL(R) XEON(R) PLATINUM 8573C; cgroup quota 4cores. Actual compiled source21cc5392. These are short observations, not physical-device or sustained-FPS acceptance.

|Viewport|DPR|Renderer|RAF median/p95 ms|Decoded RGBA estimate|
|---|---|---|---|---|
|[1280, 900]|1|Canvas|16.70/16.80|53056700 bytes|
|[1024, 768]|2|Canvas|16.70/16.70|53056700 bytes|
|[667, 375]|3|Canvas|16.70/16.80|48694220 bytes|

Eight real door cycles: {'countDelta': 0, 'rgbaEstimateDelta': 0, 'claim': 'Eight bounded real-door cycles only, not an unbounded leak guarantee'}

Default AUTO/SwiftShader full suite at9b937216 was81PASS1FAIL (Taeyang total120s); its cause remains unproven. The new complete236unit/82E2E pass applies to Canvas fallback with capability flags explicitly recorded. A short AUTO startup observation does not close the full-profile performance issue. AndroidChrome/iPhoneSafari/physicalGPU, battery and thermal behavior: NOT TESTED. JS heap and RGBA figures are estimates, not measured GPU/process residency.

Fresh current default35 full82E2E:82PASS/0FAIL/0flaky/skipped/retries,17.8minutes on the same cloud environment. Historical Taeyang120s unique cause remains unproven. This is whole-suite functional evidence, not sustained mobile/hardwareGPU certification.
