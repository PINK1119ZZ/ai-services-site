# Mass Assignment 防禦

**分類：** API 安全 | **框架：** OWASP API3:2023  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
識別並防禦 Mass Assignment 漏洞，防止攻擊者透過 API 修改不應暴露的欄位（如 isAdmin、role、balance）。

## 使用方式
```
請掃描 [API 控制器/Serializer 程式碼] 中的 Mass Assignment 風險：
1. 找出所有直接將請求 body 映射到模型的位置
2. 識別哪些欄位不應由使用者控制（is_admin/role/status/balance）
3. 找出缺少欄位白名單的 PUT/PATCH 端點
4. 評估是否可透過 JSON body 注入額外欄位
5. 提供修復方案（Allowlist 欄位）
```

## 修復範例
```python
# ❌ 危險（直接 Mass Assignment）
@app.put("/api/users/{user_id}")
async def update_user(user_id: int, data: dict, user=Depends(get_current_user)):
    db.query(User).filter(User.id == user_id).update(data)
    # 攻擊者可發送 {"is_admin": true, "balance": 999999}

# ✅ 安全（Pydantic allowlist）
class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    # 注意：is_admin、role、balance 不在這裡

@app.put("/api/users/{user_id}")
async def update_user(
    user_id: int, 
    data: UserUpdateRequest,  # 只允許白名單欄位
    user=Depends(get_current_user)
):
    update_data = data.dict(exclude_unset=True)
    db.query(User).filter(User.id == user_id).update(update_data)
```

## 參考框架
- OWASP API Security API3:2023（Broken Object Property Level Authorization）
- MITRE CWE-915（Improperly Controlled Modification of Dynamically-Determined Object Attributes）
