# Đối chiếu roadmap V4 · 11/11/2026

Nguồn quyết định mới nhất: HUMAN_DIRECTIVE.md (10/11), sau các approval V2 và feedback P0. Bảy Gate lịch sử được giữ nguyên; bảy workstream không phải bảy phase mới. Source baseline18babd92; code candidate21cc5392 (native farm assets giữ từ8d; thêm flush save phòng và read-only debug raster); artwork cũ được kiểm bằng PROTECTED_AUDIT.json. Bản V2 public ghi nhận ngày9/11 là artifact671d267e / manifestcdf3f6d5; báo cáo cũ overallFAIL Wrong actual room purchase vẫn giữ nguyên, không đổi thànhPASS từ test local mới.

|Gate lịch sử|Thực tế / phase tương ứng|Trạng thái|
|---|---|---|
|0 Audit/recovery|Phase1 và cleanup3BD; baseline/hash/checkpoint/closure|DONE nền tảng; audit candidate được báo riêng|
|1 Engine/pipeline|Phaser4.2.1, TS/Vite, renderer nearest/native, tools và lazy textures|DONE nền tảng; hardware không được suy từ browser|
|2 Art/avatar/world|Gate1–G3D;1B/2A/2B12players;2C28cosmetics gốc/24active;3A26NPC|APPROVED nền tảng. Art farm/interior/HUD dẫn xuất V4 chờ human review|
|3 First Delivery/Sign Repair/Courier Rush|3BC/3BD in-world economy; V4 ba phòng/12quest/36Hangul|IMPLEMENTED LOCAL CANDIDATE; human gameplay/Korean review pending|
|4 Wardrobe/local social/backend|Character Studio/wardrobe đã có; adapter local|PARTIAL. Backend/presence thật BLOCKED_UNTIL_OWNER_APPROVAL|
|5 Advanced/co-op/PvP/ads|Hợp đồng/mock local xác định; flags tắt; ad provider disabled|PARTIAL local. Live multiplayer/matchmaking/ads/FSRS sync NOT IMPLEMENTED/BLOCKED|
|6 Device/performance/accessibility/security/release|QA browser/closure/hashes/ZIP; exact exposure gate|PARTIAL. Android/iPhone/GPU vật lý NOT TESTED; public V4 pending|

|Phase vận hành|Phạm vi thực tế|
|---|---|
|1/1B|Bốn nhân vật đầu và motion đã được chủ dự án duyệt|
|2A/2B|Studio và mở rộng12identities; không đổi motion trong V4|
|2C|28cosmetics lịch sử;4hair items đã retired,24active giữ nguyên|
|3A|26NPC; safeguards danh tính công khai; art/IDs giữ nguyên|
|3B-A|NPC Daily Life + Review Portal giữ lại|
|3B-B|26NPC public preview và motion/cosmetic hotfix giữ lại|
|3B-C|Hair removal/collision/quest nền tảng giữ lại|
|3B-D + V2/V4 workstreams|Gameplay vật lý, farm/shop/quest, bản V4 hiện tại|
|3B-E và sau|Không tự đặt tên/claim đã hoàn thành; chờ chỉ đạo sau nghiệm thu|

## Bảy workstream thực hiện

1. Recovery/checkpoint/native pipeline: tiếp tục branch hiện tại, pin lịch sử và nguồn gốc, clean checkout riêng; không regenerate art đã duyệt.
2. Farm: sáu mask theo đúng lòng luống, bỏ crop cũ sát mép, giữ timber nguồn;36cells độc lập,12crop, visual root nằm trên đất. Timers/save/lock/reward giữ nguyên cơ chế thật.
3. HUD: skin native nine-slice, wallet/receipts, bag/stack/categories, journal/hints/tracking và hotbar thật, ba viewport/DPR; thao tác trồng/tưới/thu hoạch vẫn trong world.
4. Interiors: market704×512, bookshop640×544, workshop704×480; floor/props/blockers khác nhau; chính sprite player/NPC được chuyển scene; cửa và dịch vụ có range check.
5. Learning/economy/quests:36Hangulitems, NFC/NFD/IME,12quest/5tuyến/2nhánh/3hội tụ, save additive/backup và reward một lần; tiếng Hàn chưa chuyên gia duyệt.
6. Social/future: giữ nguyên contracts/mock local/disabled flags từ V2; không lập backend, tài khoản mạng, ads hay giả người chơi online.
7. QA/release: full clean scripts, video input thật, PNG native, hash/closure/ZIP/HTTP; public exactmanifest là quyết định riêng của chủ dự án.
