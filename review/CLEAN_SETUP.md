# Clean checkout và tính tái lập

Checkout độc lập /workspace/roadmap-v4-clean, branch feature/roadmap-v4-jeju-hangul-quests từ source hiện tại; không reset về checkpoint cũ. npm ci cài138packages vào node_modules riêng với npm_config_cache=/workspace/.cache/roadmap-v4-npm. Lượt đầu cache mặc định /home/agent/.npm không ghi được, lỗi được giữ.

Project giữ các test bảo toàn đối chiếu với những commit/checkpoint cũ ngoài lịch sử shallow. Clone sạch không chứa các object unreachable đó; đọc object store lịch sử của /workspace/roadmap-v4 qua .git/objects/info/alternates sau khi kiểm tra chúng hiện hữu. Không đổi expected hash, bỏ test, sửa artwork hoặc giả remote fetch. Một checkout độc lập mà thiếu lịch sử tương tự cần fetch các exact historical refs hoặc cung cấp read-only object store trước khi chạy preservation tests. Đây là phụ thuộc lịch sử Git của test, không phải npm/runtime dependency.

Node24, Chromium hệ thống, Python3/Pillow/numpy/scipy dùng cho QA/authoring; standalone ZIP chỉ cần Python3 chuẩn và browser. Playwright FFmpeg vendor endpoint403; dùng bản /usr/bin/ffmpeg đã cài và đăng ký workspace binary, không tải dịch vụ trả phí. Native sources không được re-export trong npmci/setup.

Lệnh final: npm run typecheck; npm run assets:check; npm run lint; npm run format:check; npm test -- --maxWorkers=1; npm run build; CI=1 PIXEL_PREVIEW_PORT=4495 PIXEL_REPORT_DIR=docs/roadmap-v4/final-clean-e2e PLAYWRIGHT_BROWSERS_PATH=/workspace/.cache/ms-playwright npm run test:e2e. Một worker, không video/hash audit đồng thời để tránh lặp contention của lượt trước; không tăng deadline hoặc bỏ assertions.

Navigation QA cache được tạo lazy khi thiếu hoặc fingerprint canonicalmanifest/masks/physicalguard/generator thay đổi. Không cần chép .cache từ checkout khác. navigation.py chỉ ghi derivedcache và NAV_GUIDE, không tự ghi đè nav_path.py. Cache tái tạo đã kiểm SHA array bằng bản trước; ordinary keyboard walk/run kiểm41waypoints thực sự. Đây là QA planner đọc dữ liệu, không phải runtime collision/character engine mới.
