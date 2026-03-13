# 区块头解析器 (Go 版本)

> 手动实现比特币区块头解析器，用于学习 Go 语言和区块链底层原理。
> 
> ⚠️ **警告**：这是学习项目，从零开始自己实现，不要复制现成代码！

---

## 🎯 项目目标

使用 **Go 语言** 实现比特币区块头解析器：
- 解析 80 字节区块头结构
- 实现双 SHA256 哈希计算
- 验证工作量证明 (PoW)
- 掌握 Go 语言核心概念

---

## 📁 项目结构

```
block-parser/
├── go-version/              # Go 实现（你正在开发的）
│   ├── README.md           # Go版本学习指南
│   ├── go.mod
│   ├── main.go
│   └── ...（你的代码）
├── visual-guides/          # 交互式概念学习指南
│   ├── index.html
│   ├── block-header.html
│   └── ...（可视化演示）
└── README.md               # 本文件
```

---

## 🚀 快速开始

### 前置知识
在开始之前，建议先阅读交互式指南理解概念：
1. 打开 `visual-guides/index.html`
2. 依次学习各个概念

### 开始编码

```bash
cd go-version

# 按照 README.md 中的步骤实现
cat README.md
```

---

## 📚 学习资源

### 概念理解（可视化）
- 📦 [区块头结构](./visual-guides/block-header.html)
- 🔄 [字节序转换](./visual-guides/endianness.html)
- 🔐 [双 SHA256 哈希](./visual-guides/sha256.html)
- ⛰️ [难度目标](./visual-guides/difficulty.html)

### Go 语言学习
- [A Tour of Go](https://go.dev/tour/)
- [Go by Example](https://gobyexample.com/)

---

## 🔀 分支说明

| 分支 | 说明 |
|------|------|
| `main` | 当前分支，用于 Go 版本开发 |
| `feature/block-parser` | Python 版本实现（已存档） |
| `feature/go-implementation` | 当前 Go 开发分支 |

---

## ✅ 验收标准

- [ ] 能正确解析创世区块头
- [ ] 计算出的区块哈希与浏览器一致
- [ ] PoW 验证通过
- [ ] 完整测试覆盖
- [ ] 代码符合 Go 语言习惯

---

**状态**: 🟡 Go版本开发中 | [Go版本指南](./go-version/README.md)
