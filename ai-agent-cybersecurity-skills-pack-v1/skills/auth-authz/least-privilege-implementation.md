# 最小權限原則實施

**分類：** 身份驗證與授權 | **框架：** NIST CSF 2.0 Protect  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
協助開發者在程式碼和基礎設施層面實施最小權限原則，縮小爆炸半徑。

## 使用方式
```
請審查 [服務/函式] 的最小權限實施：
1. 資料庫用戶是否只有完成任務所需的最小權限
2. 雲端 IAM 角色是否有過寬的 * 權限
3. 微服務間的調用是否有服務帳號隔離
4. 檔案系統權限是否正確設置
5. 每個外部 API 呼叫是否使用獨立金鑰
6. 提供具體的收緊建議
```

## 資料庫最小權限範例
```sql
-- ❌ 危險（root 帳號或 GRANT ALL）
GRANT ALL PRIVILEGES ON *.* TO 'app'@'%';

-- ✅ 安全（按業務功能細分）
-- 訂單服務：只讀寫訂單表
CREATE USER 'order-service'@'10.0.0.0/8' IDENTIFIED BY '...';
GRANT SELECT, INSERT, UPDATE ON mydb.orders TO 'order-service'@'10.0.0.0/8';
GRANT SELECT ON mydb.products TO 'order-service'@'10.0.0.0/8';

-- 報表服務：只讀
CREATE USER 'analytics'@'10.0.0.0/8' IDENTIFIED BY '...';
GRANT SELECT ON mydb.* TO 'analytics'@'10.0.0.0/8';
```

## 參考框架
- NIST SP 800-207 Zero Trust（最小權限核心原則）
- AWS IAM Policy Conditions（最細粒度控制）
- CIS Controls v8 Control 5（Account Management）
