# 雲端網路安全組審計

**分類：** 容器與雲端安全 | **框架：** CIS Cloud Benchmark  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
審查 AWS Security Group / GCP Firewall Rules / Azure NSG 的入站/出站規則，找出過度寬泛的網路暴露。

## 使用方式
```
請審查 [Security Group / Firewall Rules] 的安全性：
1. 找出允許 0.0.0.0/0 的入站規則（特別是 SSH 22、RDP 3389、DB 3306/5432）
2. 找出不必要的對外暴露服務
3. 找出出站規則是否有限制（防資料外洩）
4. 找出未使用的 Security Group
5. 識別跨 VPC 的不必要連線
6. 評估防禦縱深是否足夠（多層隔離）
```

## 高風險規則快速識別
```bash
# AWS：找出開放 SSH 到全世界的 Security Group
aws ec2 describe-security-groups \
  --filters "Name=ip-permission.from-port,Values=22" \
            "Name=ip-permission.cidr,Values=0.0.0.0/0" \
  --query 'SecurityGroups[*].{ID:GroupId,Name:GroupName}'

# AWS：找出開放 RDS 到全世界的規則
aws ec2 describe-security-groups \
  --filters "Name=ip-permission.from-port,Values=3306" \
            "Name=ip-permission.cidr,Values=0.0.0.0/0"
```

## 修復建議
| 服務 | 建議入站規則 |
|------|------------|
| SSH（22）| 僅限 Bastion Host IP / VPN IP |
| DB（3306/5432）| 僅限應用服務器 Security Group |
| Redis（6379）| 僅限應用服務器 Security Group |
| HTTPS（443）| 0.0.0.0/0（對外服務） |
| HTTP（80）| 僅 Load Balancer（強制 HTTPS） |

## 參考框架
- CIS AWS Foundations Benchmark 4.x
- MITRE ATT&CK T1190（Exploit Public-Facing Application）
- AWS VPC Security Best Practices
