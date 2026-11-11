# V4 · QA kỹ thuật và giới hạn nghiệm thu

PARTIAL · READY_FOR_OWNER_REVIEW trên Canvas (candidate riêng tư). DefaultAUTO/SwiftShader tại9b vẫnFAIL81/82, lượt full-profile hiện tại PASS được ghi riêng bên dưới; chưa được nghiệm thu. Không phải human art/gameplay/Korean acceptance, DEPLOYED hoặc commercial clearance.

Source compiled: `21cc539259853952c91e548fb782cbd6df2e8785`. Full sạch: `35e0b40593835cf69a556f171210e623fa47f3aa`. SOURCE_EQUIVALENCE.json đối chiếu src/assets/dependencies/config giống nhau; commit35 chỉ thêm3dòng chờ marker thật trong test, còn compiled game21 không đổi. Tool ghi video được sửa riêng để tôn trọng cooldown/trạng thái đất; không sửa game. Sáu video quay từ đúng source compiled cuối, không build dev giả screenshot.

|Check|Kết quả|
|---|---|
|npmci/typecheck/assets/lint/format/build|PASS; npmci138packages; build-sizeWARN giữ nguyên|
|Full unit|236/236PASS,0FAIL|
|Full E2E Canvas fallback,1worker/0retries|82/82PASS,0FAIL/0flaky/0skipped; samecases/assertions/timeouts|
|Full defaultAUTO/SwiftShader|81PASS/1FAIL(Taeyang total120s); FAIL giữnguyên, không suy từ Canvas|
|Protectedsource/art|10763files unchanged|
|Runtimeclosure|627files,599prior exact/28new-derived|
|Native rooms|36164opaqueprop+192floorpixels,0difference|
|Native cropbody|4stages,root909604/scale1/nearest,0difference|
|HangulactualUI|36cases across4topics×3grades, NFC/NFD/IME|
|Questactualflow|12/12 across earnedfarm+continuation,37events/3longtraces|
|Jeju|Plain/debug78legs each, negatives water/wall/roof retained|
|Videos|V01–05+debug,whole-take finalcompiled, silent|
|PhysicalAndroid/iPhone/GPU|NOT TESTED|
|Newart/gameplay/Korean|PENDING_HUMAN_REVIEW|
|PublicV4/livebackend/multiplayer/ads|Not deployed/disabled; separate approval|

## Lỗi cũ không bị xóa

Firstfull77:71PASS/6FAIL. Ba fixture phòng dùngexit320438 và cắt qua đồ nội thất; chỉ sửa driver theo floor/solids/exit thật, không bỏ assertion/tăngtimeout. Ba lỗi init/residency trước dưới tải video/hash song song: contention là giả thuyết phù hợp, chưa chứng minh là nguyên nhân duy nhất. Giữ log/context/screenshot; finalfull82 chạy lại toàn bộ, không chỉ chạy lại6caFAIL. CollectionJSONimportNode24 trước đó chạy0test, được lưu riêng; đọcJSON quafs trong test, không sửa bank/runtime. Unit prior thiếuhistoricalobjects được sửa quyền đọc lịch sử, không đổi expectedhash.

Full82 tại8d30ee8f:80PASS2FAIL được giữ riêng. Bookshop now exactXYrestore thay Y<326. NPC chờ MOVE_TO_WAYPOINT rồi giữ nguyên15s đo di chuyển; diagnostic6/6 có WORK8s trước walk, chưa tái hiện fail ban đầu. Không sửa NPC engine/routes/art hoặc tăngdeadline.

A009full82 lần hai80PASS2FAIL:coldStudio prebootstrap5s vàfinejoystick8s. Bảyca focusedPASS sau correctboot readiness/ordinaryWASD đi bộ41waypoints; cùng tuyến đã thử chạy. No runtime/mask edit. Diagnostic sampling ảnh hưởng release timing nên không giả là tái hiện đúng oldtimeout. adfdpreflight235/236timeout,0E2E; giữ mọi hash/file/5s cap và gộp mismatch assertions để giảmoverhead, focused6/6PASS3.91s. Full236/82 cuối là lượt riêng.

Wrong actual room purchase của bản liveNov9V2 vẫnFAIL trong hồ sơ cũ. Không lấy testtransactionV4 mới để giả sửa kết quả lịch sử. Native review đã bắt crop-tip ở viền luống và crop-root dưới timber, sửa trước finalcompiled: sáu opening masks riêng,535connectedfringe pixels, rootYvisual<=16px; logicalcoords/collision/nativeatlas không đổi.

A01/A09/A16 vẫnPARTIAL về humanquality, A12 cònpublicapproval; xem ACCEPTANCE_MATRIX.json. ZIP/CRC/extractedHTTP/gameplay/playback cần đọc finalPACKAGE_PROOF ngoàiartifact, không một checksum tự tham chiếu.



Lỗi full9bCanvas80/82, full21Canvas81/82 và hai takeV01 lỗi được giữ riêng; xem QA_RUN_HISTORY.md, LIFECYCLE_AND_DEBUG_FIX.md và MARKER_PUBLICATION_DIAGNOSTIC.json. Bộ ảnh36cell/sáu luống mọi stage là ART FIXTURES ghi rõ, không thay video hành động thật. FARM_REWARD_READBACK.json xác nhận nhận+2radish/+3scallion/+3carrot và tiêu thụ đúng1hạt mỗi loại.


## Full profile mặc định hiện tại ·35e0b405

PASS · {'startTime': '2026-11-11T14:01:36.055Z', 'duration': 1070131.429, 'expected': 82, 'skipped': 0, 'unexpected': 0, 'flaky': 0} · không retry/skipping. Xem CURRENT_DEFAULT_PROFILE_E2E.json và CURRENT_AUTO_FULL.log. Đây là cả82ca với browser capabilities mặc định; một số ca vốn yêu cầuCanvas vẫn giữ nguyên. Không giả đây là82ca WebGL thuần. TimeoutTaeyang120s cũ tại9b vẫn chưa có nguyên nhân duy nhất được chứng minh; lượt mới không được dùng để tuyên bố đã sửa lỗi cũ hay chứng nhậnGPU/thiết bị thật.
