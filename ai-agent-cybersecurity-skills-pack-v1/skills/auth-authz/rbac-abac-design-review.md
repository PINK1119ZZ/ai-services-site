# RBAC / ABAC 設計審查

**分類：** 身份驗證與授權 | **框架：** NIST RBAC Standard  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查角色基礎存取控制（RBAC）或屬性基礎存取控制（ABAC）的設計與實作，確保最小權限原則。

## 使用方式
```
請審查 [授權系統] 的設計安全性：
1. 角色定義是否遵循最小權限（無過度寬泛的 admin 角色）
2. 權限檢查是否在服務端執行（非僅前端）
3. 動態權限計算是否有緩存污染風險
4. 角色繼承是否有意外的權限提升路徑
5. 是否有細粒度的資源層級授權（ABAC）
6. 權限變更是否即時生效（或有延遲窗口）
```

## RBAC 最佳實踐
```typescript
// ❌ 危險（過度寬泛的 admin 角色）
enum Role { USER, ADMIN }
// ADMIN 可以做所有事

// ✅ 安全（細粒度權限）
enum Permission {
  READ_ORDERS, WRITE_ORDERS, DELETE_ORDERS,
  READ_USERS, WRITE_USERS, DELETE_USERS,
  READ_ANALYTICS,  // 只讀報表的角色不需要寫入
}

const ROLES: Record<string, Permission[]> = {
  'order-manager': [Permission.READ_ORDERS, Permission.WRITE_ORDERS],
  'analyst':       [Permission.READ_ORDERS, Permission.READ_ANALYTICS],
  'super-admin':   Object.values(Permission),
};
```

## 參考框架
- NIST SP 800-207 Zero Trust（最小權限）
- OWASP Access Control Cheat Sheet
- AWS IAM Policy Design Patterns
