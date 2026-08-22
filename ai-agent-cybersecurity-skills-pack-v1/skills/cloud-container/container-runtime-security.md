# 容器運行時安全

**分類：** 容器與雲端安全 | **框架：** CIS Docker Benchmark + NIST SP 800-190  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查容器運行時的安全配置，防止容器逃逸和特權提升攻擊。

## 使用方式
```
請審查 [Docker Compose / Kubernetes Deployment / Helm Chart] 的容器安全配置：
1. 容器是否以 root 運行（應用非特權用戶）
2. 是否掛載了高風險主機路徑（/var/run/docker.sock / /host）
3. 是否啟用了 --privileged 模式（最高風險）
4. 是否有 securityContext 配置（readOnlyRootFilesystem / allowPrivilegeEscalation）
5. 資源限制是否配置（CPU/Memory limits 防 DDoS）
6. 網路策略是否隔離（NetworkPolicy）
```

## 安全 Kubernetes Deployment 範例
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 65532    # 非 root
        fsGroup: 65532
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: app
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop: ["ALL"]   # 移除所有 Linux capabilities
        resources:
          limits:
            cpu: "500m"
            memory: "256Mi"
          requests:
            cpu: "100m"
            memory: "128Mi"
```

## 參考框架
- CIS Kubernetes Benchmark v1.9
- NIST SP 800-190 Application Container Security
- MITRE ATT&CK T1610（Deploy Container）
