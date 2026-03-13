"""
比特币区块头类

区块头固定 80 字节，包含 6 个字段：
- Version (4 bytes)
- PrevHash (32 bytes)
- MerkleRoot (32 bytes)
- Timestamp (4 bytes)
- Bits (4 bytes)
- Nonce (4 bytes)
"""

import struct
from typing import Dict


class BlockHeader:
    """
    比特币区块头 (80 bytes)
    
    Attributes:
        version: 区块版本号 (int)
        prev_hash: 前一区块哈希 (32 bytes, 小端序)
        merkle_root: 默克尔根 (32 bytes, 小端序)
        timestamp: Unix 时间戳 (int)
        bits: 难度目标紧凑格式 (4 bytes)
        nonce: 随机数 (int)
    """
    
    SIZE = 80  # 区块头固定大小
    
    def __init__(self, version: int, prev_hash: bytes, merkle_root: bytes,
                 timestamp: int, bits: bytes, nonce: int):
        """
        初始化区块头
        
        Args:
            version: 区块版本号
            prev_hash: 前一区块哈希（32 字节，小端序）
            merkle_root: 默克尔根（32 字节，小端序）
            timestamp: Unix 时间戳
            bits: 难度目标（4 字节）
            nonce: 随机数
        """
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
        
        字节布局（小端序）:
            [0:4]   Version
            [4:36]  PrevHash
            [36:68] MerkleRoot
            [68:72] Timestamp
            [72:76] Bits
            [76:80] Nonce
        
        Args:
            raw_bytes: 80 字节的区块头数据
            
        Returns:
            BlockHeader 实例
            
        Raises:
            ValueError: 如果数据长度不是 80 字节
        """
        if len(raw_bytes) != cls.SIZE:
            raise ValueError(f"区块头必须是 {cls.SIZE} 字节，实际 {len(raw_bytes)} 字节")
        
        # 解析 Version (4 bytes, little-endian)
        version = struct.unpack('<I', raw_bytes[0:4])[0]
        
        # 解析 PrevHash (32 bytes)
        # 注意：存储是小端序，但通常保持原样
        prev_hash = raw_bytes[4:36]
        
        # 解析 MerkleRoot (32 bytes)
        merkle_root = raw_bytes[36:68]
        
        # 解析 Timestamp (4 bytes, little-endian)
        timestamp = struct.unpack('<I', raw_bytes[68:72])[0]
        
        # 解析 Bits (4 bytes)
        bits = raw_bytes[72:76]
        
        # 解析 Nonce (4 bytes, little-endian)
        nonce = struct.unpack('<I', raw_bytes[76:80])[0]
        
        return cls(version, prev_hash, merkle_root, timestamp, bits, nonce)
    
    def to_bytes(self) -> bytes:
        """
        将区块头序列化为 80 字节
        
        Returns:
            80 字节的区块头数据
        """
        result = bytearray()
        
        # Version (4 bytes, little-endian)
        result.extend(struct.pack('<I', self.version))
        
        # PrevHash (32 bytes)
        result.extend(self.prev_hash)
        
        # MerkleRoot (32 bytes)
        result.extend(self.merkle_root)
        
        # Timestamp (4 bytes, little-endian)
        result.extend(struct.pack('<I', self.timestamp))
        
        # Bits (4 bytes)
        result.extend(self.bits)
        
        # Nonce (4 bytes, little-endian)
        result.extend(struct.pack('<I', self.nonce))
        
        return bytes(result)
    
    def to_dict(self) -> Dict:
        """
        转换为字典格式（方便显示）
        
        注意：哈希值翻转成大端序显示（符合人类阅读习惯）
        
        Returns:
            包含区块头字段的字典
        """
        return {
            'version': self.version,
            'prev_hash': self.prev_hash[::-1].hex(),      # 翻转显示
            'merkle_root': self.merkle_root[::-1].hex(),  # 翻转显示
            'timestamp': self.timestamp,
            'bits': self.bits.hex(),
            'nonce': self.nonce
        }
    
    def __repr__(self) -> str:
        return (f"BlockHeader("
                f"version={self.version}, "
                f"timestamp={self.timestamp}, "
                f"nonce={self.nonce})")
    
    def __eq__(self, other) -> bool:
        """比较两个区块头是否相等"""
        if not isinstance(other, BlockHeader):
            return False
        return (self.version == other.version and
                self.prev_hash == other.prev_hash and
                self.merkle_root == other.merkle_root and
                self.timestamp == other.timestamp and
                self.bits == other.bits and
                self.nonce == other.nonce)
