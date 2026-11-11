# Korean Pixel Town V4 · nghiệm thu tổng hợp

Candidate V4 mới là bản riêng tư, ưu tiên review Canvas. Lượt AUTO/SwiftShader9b cũ81PASS/1FAIL(Taeyang120s) chưa có nguyên nhân duy nhất được chứng minh; lượt đầy đủ hiện tại35 đạt82/82,0retry/skipping, không được tự suy từ Canvas sang WebGLPASS; Pages chưa được cập nhật bởi task này. Xem FINAL_DELIVERY.json / PACKAGE_PROOF.json để lấy đúng artifact, manifest, ZIP và checksum, không lấy bản cũ trên Pages làm V4.

1. Giải nén ROADMAP_V4_PLAYABLE_REVIEW.zip. Chạy `python3 start-review.py --port 4492` trong thư mục vừa giải nén. Chỉ cần Python3 và browser; không cần npm, tài khoản hay backend.
2. Mở `http://127.0.0.1:4492/review/` để xem native PNG, so sánh trước/sau và sáu video liên tục. Chọn **Chơi V4 Canvas** để vào cùng game compiled; Portal/NPC/Daily Life vẫn có từ trang đầu.
3. WASD/phím mũi tên di chuyển, Shift chạy, E tương tác ở gần. Mobile landscape: joystick + nút hành động. Chọn nhân vật trong Studio hiện có; không có nhân vật hoặc cosmetic mới trong V4.
4. Farm: gặp NPC nhận hạt/nhiệm vụ, đến đúng ô trống; hotbar chọn hạt/công cụ rồi E để xới–gieo–tưới. Nhìn stage thay đổi theo đồng hồ thật; chọn thu hoạch rồi E để lấy crop. Sáu luống/36ô độc lập. Khóa hạt được mở qua hai mốc quest, không cần tiền thật hoặc tăng tốc QA.
5. Xu/túi đồ/sổ nhiệm vụ đều phản ánh save thật. Theo dõi tuyến và đọc gợi ý điểm đến trong journal; không có nút hoàn thành từ xa. Town Coins không phải điểm học chính thức.
6. Ba cửa tại world717,2605 (góc hạt giống),1128,2605 (hiệu sách),1418,2605 (xưởng). Đi sát cửa rồi E; bên trong đi tới NPC/quầy/bàn công việc mới tương tác được. Đi về cửa ra rồi E để trở lại world. Không cần QA spawn để vào.
7. Hiệu sách có luyện36câu theo chủ đề/cấp độ: chọn đáp án Hangul hoặc gõ Hangul. Dịch Hàn→Việt là mode riêng; luyện tập tự do không khóa bằng xu hoặc giả ghi kết quả lên website học.
8. Jeju: từ nút đầu cầu phía đảo đi qua đường cong phía đông hanok xuống thềm cửa; thử cả đi bộ/chạy hai chiều. Video riêng có overlay chỉ rõ chỗ mask nối được mở, không mở nước/tường/mái.
9. Theo các tuyến Thư/Nông trại/Thương nhân/Sân xưa/Jeju để trải nghiệm12quest. VideoV05 là một lượt tiếp tục từ save hai nhiệm vụ farm đã kiếm được thật; xem ba trace/hội tụ/reward trong QUEST_RUNTIME.json. VideoV03 có100xu fixture thử giao dịch, được ghi rõ; không phải giới thiệu tài khoản mặc định có100xu.

Korean/new art/gameplay: chờ người nghiệm thu. Android/iPhone/GPU vật lý: NOT TESTED. Không có live backend, multiplayer, quảng cáo, dữ liệu học viên hoặc thay đổi website học chính. Muốn public V4 cần duyệt đúng artifact/manifest cuối; approval V2 không tự áp dụng.

Để dùng đúng mode đã kiểm: `/play/?renderer=canvas`. `/play/` AUTO giữ nguyên renderer canonical và còn cảnh báo software-GPU ở trên; không tuyên bố đã fix. Xem TEST_RENDER_PROFILES.json và DEFAULT_PROFILE_E2E.json, CANVAS_PROFILE_E2E.json tách biệt.

Lượt hiện tại mặc định: CURRENT_DEFAULT_PROFILE_E2E.json (82/82PASS); Canvas: CANVAS_PROFILE_E2E.json (82/82PASS). Các số liệu là toàn bộ hai lượt riêng biệt, không gộp retries. Favicon dùng lại icon xu đã được phép, không đổi game/artwork.
