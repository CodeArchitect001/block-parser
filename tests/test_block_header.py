"""
BlockHeader 类测试
"""

import unittest
from src.block_header import BlockHeader


class TestBlockHeader(unittest.TestCase):
    """测试区块头解析和序列化"""
    
    # 创世区块头（80 字节，十六进制）
    GENESIS_HEADER_HEX = (
        "01000000"  # version = 1
        "0000000000000000000000000000000000000000000000000000000000000000"  # prev_hash
        "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"  # merkle_root
        "29ab5f49"  # timestamp = 1231006505
        "ffff001d"  # bits
        "1dac2b7c"  # nonce = 2083236893
    )
    
    def setUp(self):
        """测试前准备"""
        self.genesis_bytes = bytes.fromhex(self.GENESIS_HEADER_HEX)
    
    def test_parse_genesis_version(self):
        """测试解析创世区块版本号"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        self.assertEqual(header.version, 1)
    
    def test_parse_genesis_timestamp(self):
        """测试解析创世区块时间戳"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        self.assertEqual(header.timestamp, 1231006505)
    
    def test_parse_genesis_nonce(self):
        """测试解析创世区块 nonce"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        self.assertEqual(header.nonce, 2083236893)
    
    def test_parse_genesis_prev_hash(self):
        """测试解析创世区块前一哈希（应该全为 0）"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        # 创世区块的 prev_hash 应该全是 0
        self.assertEqual(header.prev_hash, bytes(32))
    
    def test_serialize_roundtrip(self):
        """测试序列化和反序列化一致性"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        serialized = header.to_bytes()
        self.assertEqual(self.genesis_bytes, serialized)
    
    def test_invalid_size(self):
        """测试非法大小的输入"""
        with self.assertRaises(ValueError):
            BlockHeader.from_bytes(bytes(79))  # 少 1 字节
        
        with self.assertRaises(ValueError):
            BlockHeader.from_bytes(bytes(81))  # 多 1 字节
    
    def test_to_dict(self):
        """测试转换为字典"""
        header = BlockHeader.from_bytes(self.genesis_bytes)
        data = header.to_dict()
        
        self.assertEqual(data['version'], 1)
        self.assertEqual(data['timestamp'], 1231006505)
        self.assertEqual(data['nonce'], 2083236893)
        
        # 检查哈希值是十六进制字符串
        self.assertEqual(len(data['prev_hash']), 64)  # 32 字节 = 64 个十六进制字符
        self.assertEqual(len(data['merkle_root']), 64)
    
    def test_equality(self):
        """测试相等性比较"""
        header1 = BlockHeader.from_bytes(self.genesis_bytes)
        header2 = BlockHeader.from_bytes(self.genesis_bytes)
        self.assertEqual(header1, header2)


if __name__ == '__main__':
    unittest.main()
