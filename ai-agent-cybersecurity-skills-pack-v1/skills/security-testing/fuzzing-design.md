# 模糊測試（Fuzzing）設計

**分類：** 安全測試自動化 | **框架：** OSS-Fuzz + AFL++  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
設計模糊測試策略，自動生成大量隨機或變異輸入，找出程式崩潰和未預期行為。

## 使用方式
```
請為 [函式/API/解析器] 設計模糊測試：
1. 識別適合 Fuzzing 的目標（解析器、反序列化、文件處理）
2. 選擇 Fuzzing 策略（Mutation-based vs Generation-based）
3. 生成 Fuzzing Harness 程式碼
4. 設計種子語料庫（Seed Corpus）
5. 設定崩潰分析和 Dedup 策略
6. CI/CD 整合方式
```

## Python Fuzzing 範例（Atheris）
```python
import atheris
import sys

def TestOneInput(data: bytes):
    """Fuzzing harness：餵給任何二進位輸入"""
    fdp = atheris.FuzzedDataProvider(data)
    
    try:
        # 目標：解析使用者提供的 JSON
        import json
        json_str = fdp.ConsumeUnicodeNoSurrogates(100)
        result = parse_user_data(json_str)  # 你的函式
    except (json.JSONDecodeError, ValueError):
        pass  # 預期的例外，不算崩潰
    # 如果 parse_user_data 拋出非預期例外 → Fuzzer 標記崩潰

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
```

## 推薦工具
- Python：Atheris（Google）、Hypothesis
- C/C++：AFL++、libFuzzer
- API：RESTler（Microsoft REST API Fuzzer）
- 多語言：OSS-Fuzz（Google，免費用於開源專案）

## 參考框架
- Google OSS-Fuzz Program
- OWASP Fuzz Testing Guide
- AFL++ Documentation
