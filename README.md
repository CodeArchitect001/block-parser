# 区块头解析器

> 比特币底层协议解析

## 对应学习

- 笔记：[02-区块链基础概念](../../../../03-钱包开发/01-核心原理/02-区块链基础概念.md#项目-3区块头解析器)
- 阶段：钱包开发 / 核心原理 / 项目 3
- 📚 **交互式概念指南**：[visual-guides/index.html](./visual-guides/index.html)（推荐先阅读）
  - 📦 [区块头结构](./visual-guides/block-header.html)
  - 🔄 [字节序转换](./visual-guides/endianness.html)
  - 🔐 [双 SHA256 哈希](./visual-guides/sha256.html)
  - ⛰️ [难度目标](./visual-guides/difficulty.html)
  - ⛏️ [PoW 挖矿模拟](./visual-guides/mining.html)
  - 🌳 [默克尔树](./visual-guides/merkle-tree.html)

## 项目目标

实现比特币区块的二进制解析，理解区块头的 80 字节结构。

## 区块头结构（80 bytes）

```
Version      : 4 bytes
PrevHash     : 32 bytes
Merkle Root  : 32 bytes
Timestamp    : 4 bytes
Bits         : 4 bytes（难度目标）
Nonce        : 4 bytes
```

## 已实现功能

- [x] `BlockHeader` 类/结构体 - 解析 80 字节区块头
- [x] `BlockParser.parse_header(raw_bytes)` - 区块解析器
- [x] `calculate_hash()` - 双 SHA256 哈希计算
- [x] `validate_pow()` - 验证工作量证明
- [x] `bits_to_target()` - 难度目标转换

## 验收标准

- [x] 能正确解析比特币创世区块头
- [x] 计算出的 Hash 与区块链浏览器一致
- [x] 能验证任意区块的 PoW 有效性

## 快速开始

```bash
# 运行测试
python main.py --test

# 解析创世区块
python main.py --hex 0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c

# 使用 Python API
from src.parser import BlockParser

header = BlockParser.parse_header(raw_bytes)
block_hash = BlockParser.get_block_hash(header)
is_valid = BlockParser.validate_header(header)
```

## 项目结构

```
block-parser/
├── src/
│   ├── block_header.py    # BlockHeader 类
│   ├── hash_utils.py      # 双 SHA256 实现
│   ├── difficulty.py      # 难度计算
│   └── parser.py          # 解析器主类
├── tests/                 # 测试用例
├── visual-guides/         # 交互式概念指南
└── main.py               # 命令行工具
```

## 进阶挑战

- 解析完整区块（含交易列表）
- 实现区块同步器（连接比特币网络）

---

**状态**: ✅ 已完成 | **耗时**: 2-3h | [开发指南](./DEVELOPMENT.md) | [返回阶段目录](../README.md)
