# Kubernetes RBAC 審計

**分類：** 容器與雲端安全 | **框架：** CIS Kubernetes Benchmark  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 Kubernetes RBAC 配置，識別過度寬泛的角色綁定和特權 Service Account。

## 使用方式
```
請審查 [Kubernetes RBAC 配置] 的安全性：
1. 找出所有 cluster-admin 角色綁定（最高風險）
2. 找出 verb: ["*"] 或 resource: ["*"] 的 ClusterRole
3. 找出 default Service Account 是否有過多權限
4. 找出容器掛載 Service Account token 但不需要的情況
5. 找出跨命名空間的敏感資源訪問
6. 識別 RBAC 提權路徑
```

## 安全 RBAC 範例
```yaml
# ❌ 危險（cluster-admin 綁定到普通服務）
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: production
roleRef:
  kind: ClusterRole
  name: cluster-admin  # 絕對不應這樣

---
# ✅ 安全（最小權限，限制命名空間）
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]  # 只讀，限定資源類型
```

## 掃描指令
```bash
# 找出所有 cluster-admin 綁定
kubectl get clusterrolebindings -o json | \
  jq '.items[] | select(.roleRef.name == "cluster-admin")'

# 使用 rbac-police 深度分析
rbac-police eval
```

## 參考框架
- CIS Kubernetes Benchmark v1.9 Section 5
- RBAC Police（自動化分析工具）
- NSA/CISA Kubernetes Hardening Guide
