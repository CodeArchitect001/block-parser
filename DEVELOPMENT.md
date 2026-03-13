# 区块头解析器 - 开发指南

## 🎯 开发目标

实现一个比特币区块头解析器，能够：
1. 解析 80 字节的区块头
2. 计算区块哈希（双 SHA256）
3. 验证工作量证明（PoW）
4. 转换难度目标（Bits ↔ Target）

---

## 📁 项目结构

```
block-parser/
├── src/
│   ├── __init__.py
│   ├── block_header.py      # BlockHeader 类
│   ├── parser.py            # BlockParser 类
│   ├── hash_utils.py        # 哈希相关工具
│   └── difficulty.py        # 难度计算
├── tests/
│   ├── __init__.py
│   ├── test_block_header.py
│   ├── test_parser.py
│   └── test_difficulty.py
├── data/
│   └── genesis_block.bin    # 创世区块二进制数据
├── main.py                  # 入口文件
├── requirements.txt         # 依赖
└── README.md
```

---

## 📝 开发步骤

### 步骤 1: 初始化项目

```bash
# 创建目录结构
mkdir -p src tests data

# 创建文件
touch src/__init__.py tests/__init__.py
```

### 步骤 2: 实现 BlockHeader 类

**文件**: `src/block_header.py`

```python
import struct
from typing import Dict

class BlockHeader:
    """
    比特币区块头 (80 bytes)
    
    字段:
        version     (int):    区块版本号 (4 bytes)
        prev_hash   (bytes):  前一区块哈希 (32 bytes)
        merkle_root (bytes):  默克尔根 (32 bytes)
        timestamp   (int):    时间戳 (4 bytes)
        bits        (bytes):  难度目标 (4 bytes)
        nonce       (int):    随机数 (4 bytes)
    """
    
    SIZE = 80  # 区块头固定 80 字节
    
    def __init__(self, version: int, prev_hash: bytes, merkle_root: bytes,
                 timestamp: int, bits: bytes, nonce: int):
        self.version = version
        self.prev_hash = prev_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce
    
    @classmethod
    def from_bytes(cls, raw_bytes: bytes) -> 'BlockHeader':
        """
        从 80 字节解析区块头
        
        Args:
            raw_bytes: 80 字节的区块头数据
            
        Returns:
            BlockHeader 实例
            
        Raises:
            ValueError: 如果数据长度不是 80 字节
        """
        # TODO: 实现解析逻辑
        pass
    
    def to_bytes(self) -> bytes:
        """将区块头序列化为 80 字节"""
        # TODO: 实现序列化逻辑
        pass
    
    def to_dict(self) -> Dict:
        """转换为字典格式（方便显示）"""
        return {
            'version': self.version,
            'prev_hash': self.prev_hash[::-1].hex(),  # 大端序显示
            'merkle_root': self.merkle_root[::-1].hex(),
            'timestamp': self.timestamp,
            'bits': self.bits.hex(),
            'nonce': self.nonce
        }
    
    def __repr__(self) -> str:
        return f"BlockHeader(version={self.version}, timestamp={self.timestamp}, nonce={self.nonce})"
```

### 步骤 3: 实现哈希工具

**文件**: `src/hash_utils.py`

```python
import hashlib

def double_sha256(data: bytes) -> bytes:
    """
    计算双 SHA256 哈希
    
    Args:
        data: 输入数据
        
    Returns:
        32 字节的哈希值
    """
    # TODO: 实现双 SHA256
    pass

def calculate_block_hash(block_header: bytes) -> bytes:
    """
    计算区块哈希
    
    注意: 区块头是小端序存储，但显示时要翻转成大端序
    
    Args:
        block_header: 80 字节的区块头
        
    Returns:
        32 字节的区块哈希（小端序）
    """
    # TODO: 计算哈希
    pass
```

### 步骤 4: 实现难度计算

**文件**: `src/difficulty.py`

```python
def bits_to_target(bits: bytes) -> int:
    """
    将 compact bits 转换为目标值
    
    Bits 格式: [系数 3 字节（小端序）][指数 1 字节]
    公式: Target = Coefficient * 256^(Exponent - 3)
    
    Args:
        bits: 4 字节的 bits 值
        
    Returns:
        目标值（大整数）
    """
    # TODO: 实现 bits 到 target 的转换
    pass

def target_to_bits(target: int) -> bytes:
    """
    将目标值转换为 compact bits
    
    Args:
        target: 目标值
        
    Returns:
        4 字节的 bits 值
    """
    # TODO: 实现 target 到 bits 的转换
    pass

def validate_pow(block_hash: bytes, target: int) -> bool:
    """
    验证工作量证明
    
    规则: block_hash 作为大整数必须小于 target
    
    Args:
        block_hash: 32 字节的区块哈希（小端序）
        target: 难度目标值
        
    Returns:
        是否满足难度目标
    """
    # TODO: 实现 PoW 验证
    pass
```

### 步骤 5: 实现 BlockParser

**文件**: `src/parser.py`

```python
from .block_header import BlockHeader
from .hash_utils import calculate_block_hash
from .difficulty import bits_to_target, validate_pow

class BlockParser:
    """区块解析器"""
    
    @staticmethod
    def parse_header(raw_bytes: bytes) -> BlockHeader:
        """解析区块头"""
        return BlockHeader.from_bytes(raw_bytes)
    
    @staticmethod
    def get_block_hash(header: BlockHeader) -> str:
        """
        获取区块哈希（大端序显示）
        
        Returns:
            64 字符的十六进制字符串
        """
        # TODO: 实现
        pass
    
    @staticmethod
    def validate_header(header: BlockHeader) -> bool:
        """
        验证区块头是否满足 PoW
        
        Returns:
            是否有效
        """
        # TODO: 实现
        pass
```

### 步骤 6: 入口文件

**文件**: `main.py`

```python
#!/usr/bin/env python3
"""
比特币区块头解析器

Usage:
    python main.py --hex <hex_string>
    python main.py --file <binary_file>
"""

import argparse
from src.parser import BlockParser

def main():
    parser = argparse.ArgumentParser(description='比特币区块头解析器')
    parser.add_argument('--hex', help='十六进制格式的区块头')
    parser.add_argument('--file', help='二进制区块头文件')
    
    args = parser.parse_args()
    
    # TODO: 实现命令行接口
    pass

if __name__ == '__main__':
    main()
```

---

## 🧪 测试用例

### 创世区块数据

```python
# 创世区块头（80 字节，十六进制）
GENESIS_BLOCK_HEADER = bytes.fromhex(
    "01000000" +  # version
    "0000000000000000000000000000000000000000000000000000000000000000" +  # prev_hash
    "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a" +  # merkle_root
    "29ab5f49" +  # timestamp
    "ffff001d" +  # bits
    "1dac2b7c"    # nonce
)

# 创世区块哈希（大端序显示）
GENESIS_BLOCK_HASH = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
```

### 测试文件示例

**文件**: `tests/test_block_header.py`

```python
import unittest
from src.block_header import BlockHeader

class TestBlockHeader(unittest.TestCase):
    
    def test_parse_genesis_block(self):
        """测试解析创世区块"""
        # 准备测试数据
        raw = bytes.fromhex("01000000...")
        
        # 解析
        header = BlockHeader.from_bytes(raw)
        
        # 验证字段
        self.assertEqual(header.version, 1)
        self.assertEqual(header.timestamp, 1231006505)
        self.assertEqual(header.nonce, 2083236893)
        # ... 更多验证
    
    def test_serialize_roundtrip(self):
        """测试序列化和反序列化"""
        raw = bytes.fromhex("01000000...")
        header = BlockHeader.from_bytes(raw)
        serialized = header.to_bytes()
        self.assertEqual(raw, serialized)

if __name__ == '__main__':
    unittest.main()
```

---

## ✅ 验收检查清单

- [ ] `BlockHeader.from_bytes()` 能正确解析 80 字节
- [ ] `BlockHeader.to_bytes()` 能正确序列化回 80 字节
- [ ] 创世区块解析后，各字段值正确
- [ ] 计算的区块哈希与 `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f` 一致
- [ ] `bits_to_target()` 能将 `0x1d00ffff` 转换为正确的目标值
- [ ] `validate_pow()` 能正确验证创世区块的有效性
- [ ] 修改 nonce 后，`validate_pow()` 返回 False

---

## 🔍 调试技巧

### 1. 打印十六进制

```python
def hex_dump(data: bytes, label: str = ""):
    """打印十六进制数据"""
    print(f"{label}: {data.hex()}")
```

### 2. 检查字节序

```python
def check_endianness():
    """检查平台字节序"""
    import sys
    print(f"平台字节序: {sys.byteorder}")
    # 比特币用小端序，但显示用大端序
```

### 3. 对比区块链浏览器

- [Blockchain.com 区块浏览器](https://www.blockchain.com/explorer)
- 搜索创世区块哈希，对比字段值

---

## 🚀 进阶挑战

完成基础功能后，可以尝试：

1. **解析完整区块**（含交易）
2. **实现区块浏览器 CLI**
3. **连接到比特币测试网**
4. **实现简单的区块验证器**

祝开发顺利！🎉
