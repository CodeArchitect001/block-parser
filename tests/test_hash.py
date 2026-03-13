"""
哈希函数测试
"""

import unittest
import hashlib
from src.hash_utils import double_sha256, calculate_block_hash, hash_to_hex
from src.block_header import BlockHeader


class TestHashUtils(unittest.TestCase):
    """测试哈希工具函数"""
    
    def test_double_sha256_length(self):
        """测试双 SHA256 输出长度"""
        data = b"Hello Bitcoin"
        result = double_sha256(data)
        self.assertEqual(len(result), 32)
    
    def test_double_sha256_consistency(self):
        """测试双 SHA256 一致性"""
        data = b"Test data"
        result1 = double_sha256(data)
        result2 = double_sha256(data)
        self.assertEqual(result1, result2)
    
    def test_double_sha256_different_input(self):
        """测试不同输入产生不同输出"""
        result1 = double_sha256(b"input1")
        result2 = double_sha256(b"input2")
        self.assertNotEqual(result1, result2)
    
    def test_double_sha256_manual(self):
        """手动验证双 SHA256"""
        data = b"test"
        
        # 手动计算
        first = hashlib.sha256(data).digest()
        expected = hashlib.sha256(first).digest()
        
        # 使用函数
        result = double_sha256(data)
        
        self.assertEqual(result, expected)
    
    def test_calculate_block_hash_genesis(self):
        """测试计算创世区块哈希"""
        # 创世区块头
        genesis_hex = (
            "01000000"
            "0000000000000000000000000000000000000000000000000000000000000000"
            "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
            "29ab5f49"
            "ffff001d"
            "1dac2b7c"
        )
        header_bytes = bytes.fromhex(genesis_hex)
        
        # 计算哈希
        block_hash = calculate_block_hash(header_bytes)
        
        # 转换为十六进制（大端序显示）
        hash_hex = hash_to_hex(block_hash, reverse=True)
        
        # 创世区块哈希（已知的正确值）
        expected_hash = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
        
        self.assertEqual(hash_hex, expected_hash)
    
    def test_calculate_block_hash_invalid_size(self):
        """测试非法大小的区块头"""
        with self.assertRaises(ValueError):
            calculate_block_hash(bytes(79))
        
        with self.assertRaises(ValueError):
            calculate_block_hash(bytes(81))
    
    def test_hash_to_hex(self):
        """测试哈希转十六进制"""
        hash_bytes = bytes([0x12, 0x34, 0x56, 0x78] + [0] * 28)
        
        # 翻转显示
        hex_reversed = hash_to_hex(hash_bytes, reverse=True)
        self.assertEqual(hex_reversed, "00" * 28 + "78563412")
        
        # 不翻转
        hex_normal = hash_to_hex(hash_bytes, reverse=False)
        self.assertEqual(hex_normal, "12345678" + "00" * 28)


if __name__ == '__main__':
    unittest.main()
