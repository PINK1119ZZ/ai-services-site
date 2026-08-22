# 水平/垂直權限提升測試

**分類：** 身份驗證與授權 | **框架：** OWASP Top 10 A01:2021  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別 API 和功能中的 Broken Access Control（BAC）漏洞，防止使用者訪問他人資源或提升至管理員權限。

## 使用方式
```
請審查 [API/功能程式碼] 的權限控制：

水平越權（IDOR）檢查：
1. 資源 ID 是否直接暴露在 URL（/api/orders/12345）
2. 是否驗證資源屬於當前用戶
3. GraphQL/REST API 是否有對象層級授權

垂直越權檢查：
1. 管理員功能是否只在前端隱藏
2. 角色切換邏輯是否在服務端驗證
3. 批量操作是否有授權檢查

輸出：漏洞位置 + 利用場景 + 修復建議
```

## 修復範例
```python
# ❌ 危險（IDOR）
@app.get("/api/orders/{order_id}")
async def get_order(order_id: int, user=Depends(get_current_user)):
    return db.query(Order).filter(Order.id == order_id).first()

# ✅ 安全（驗證資源所有權）
@app.get("/api/orders/{order_id}")
async def get_order(order_id: int, user=Depends(get_current_user)):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user.id  # 關鍵：驗證所有權
    ).first()
    if not order:
        raise HTTPException(status_code=404)
    return order
```

## 參考框架
- OWASP Top 10 A01:2021 Broken Access Control
- MITRE ATT&CK T1078（Valid Accounts）
- OWASP IDOR Prevention Cheat Sheet
