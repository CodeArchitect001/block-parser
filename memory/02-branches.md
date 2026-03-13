# 记忆 02: 分支结构

## 🌳 分支树

```
main (origin/main)
├── feature/block-parser          [Python实现 - 已存档]
│   └── 完整Python版本（供参考，不要直接看）
│
├── feature/go-implementation     [当前分支 - 进行中]
│   └── Go版本开发（你的代码）
│
└── (其他未来分支...)
```

## 📋 分支说明

| 分支名 | 状态 | 用途 | 是否可修改 |
|--------|------|------|-----------|
| `main` | 保护 | 主分支 | ❌ 不要直接修改 |
| `feature/block-parser` | 存档 | Python版本参考 | ❌ 已存档，不动 |
| `feature/go-implementation` | 活跃 | Go版本开发 | ✅ 当前工作分支 |

## 🔄 常用命令

```bash
# 查看当前分支
git branch

# 查看所有分支
git branch -a

# 切换分支（示例）
git checkout feature/block-parser    # 查看Python版本
git checkout feature/go-implementation  # 回到Go开发

# 提交更改
git add .
git commit -m "描述你的更改"
```

## ⚠️ 重要提醒

1. **当前在 `feature/go-implementation` 分支**
2. **Python 代码在 `feature/block-parser` 分支**
3. **Go 开发时不要切换到 Python 分支查看代码**（避免 temptation）
4. **可以看概念指南 `visual-guides/`，不要看 Python 源码**
