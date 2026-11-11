# Khôi phục an toàn

V4 là candidate riêng tư, không thay bản public. Source baseline18babd92 và tag checkpoint/before-roadmap-v4-20261110 được giữ; không reset branch đang làm việc, không retarget tag lịch sử.

Public rollback đã giữ: artifact671d267e5c3c49eceb2578dbdc847d1bb92eb136 trên artifact/roadmap-v2-671d267e; SHA256 export-manifest cdf3f6d5b117a4912fda9d88c2dc12d1cdfeded4ba39ca343bab217918b578db. File manifest gốc byte-exact nằm V2_ROLLBACK_MANIFEST.json. Nếu V4 được duyệt và deploy sau này, rollback qua workflow Pages hiện có chọn đúng artifact cũ, qua receipt/hash/history/environment gates; không force-push/xóa lịch sử và không deploy nhánh game main. Khả năng launch V2 local đã kiểm; chưa thực hiện rollback live trong task này.

Save V4 additive có storySchema1 và giữ backup byte-exact save trước nâng cấp. Không ghi localStorage profile mới lên website học chính. Khi chủ dự án muốn xem V2 không trộn save, dùng browser profile riêng hoặc export save trước khi đổi; không tự xóa tiến độ người chơi.
