# 区块头解析器

> 比特币底层协议解析

## 对应学习

- 笔记：[02-区块链基础概念](../../../../03-钱包开发/01-核心原理/02-区块链基础概念.md#项目-3区块头解析器)
- 阶段：钱包开发 / 核心原理 / 项目 3

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

## 待实现功能

- [ ] `BlockHeader` 类/结构体
- [ ] `BlockParser.parse_header(raw_bytes)`
- [ ] `calculate_hash()` - 双 SHA256
- [ ] `validate_pow()` - 验证难度目标
- [ ] `bits_to_target()` - 难度转换

## 验收标准

- [ ] 能正确解析比特币创世区块头
- [ ] 计算出的 Hash 与区块链浏览器一致
- [ ] 能验证任意区块的 PoW 有效性

## 进阶挑战

- 解析完整区块（含交易列表）
- 实现区块同步器（连接比特币网络）

---

**状态**: 🔲 待开始 | **预计**: 2-3h | [返回阶段目录](../README.md)
