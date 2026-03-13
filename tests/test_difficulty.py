"""
难度计算测试
"""

import unittest
from src.difficulty import bits_to_target, target_to_bits, validate_pow


class TestDifficulty(unittest.TestCase):
    """测试难度目标计算"""
    
    def test_bits_to_target_genesis(self):
        """测试创世区块 bits 转换"""
        # 创世区块 bits: 0x1d00ffff
        # 小端序存储: ffff001d
        bits = bytes.fromhex("ffff001d")
        
        target = bits_to_target(bits)
        
        # 创世区块目标值（已知的正确值）
        # 系数: 0x00ffff = 65535
        # 指数: 0x1d = 29
        # target = 65535 * 256^(29-3) = 65535 * 256^26
        expected = 0x00000000ffff0000000000000000000000000000000000000000000000000000
        
        self.assertEqual(target, expected)
    
    def test_bits_to_target_formula(self):
        """测试 bits 转换公式"""
        # 简单的 bits 值
        # 系数: 0x123456 = 1193046
        # 指数: 0x03 = 3
        # target = 1193046 * 256^(3-3) = 1193046
        bits = bytes.fromhex("56341203")
        
        target = bits_to_target(bits)
        expected = 0x123456
        
        self.assertEqual(target, expected)
    
    def test_target_to_bits_roundtrip(self):
        """测试 target 到 bits 的往返转换"""
        # 从 bits 开始
        original_bits = bytes.fromhex("ffff001d")
        target = bits_to_target(original_bits)
        
        # 转换回来
        converted_bits = target_to_bits(target)
        
        self.assertEqual(original_bits, converted_bits)
    
    def test_target_to_bits_genesis(self):
        """测试创世区块目标值转 bits"""
        # 创世区块目标值
        target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
        
        bits = target_to_bits(target)
        
        self.assertEqual(bits.hex(), "ffff001d")
    
    def test_validate_pow_genesis(self):
        """测试创世区块 PoW 验证"""
        from src.hash_utils import calculate_block_hash
        
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
        
        # 计算区块哈希
        block_hash = calculate_block_hash(header_bytes)
        
        # 创世区块目标值
        target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
        
        # 应该通过验证
        self.assertTrue(validate_pow(block_hash, target))
    
    def test_validate_pow_fail(self):
        """测试不通过的 PoW 验证"""
        # 一个很大的哈希值（肯定大于目标值）
        large_hash = bytes([0xff] * 32)
        
        # 很小的目标值
        small_target = 0x0000000000000000000000000000000000000000000000000000000000000001
        
        # 应该不通过
        self.assertFalse(validate_pow(large_hash, small_target))
    
    def test_validate_pow_edge_case(self):
        """测试边界情况"""
        # 哈希值刚好等于目标值（应该失败，必须严格小于）
        target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
        
        # 构造一个等于目标值的哈希（小端序存储）
        # 存储为小端序，所以与大端序目标值相同的哈希需要翻转
        hash_bytes = target.to_bytes(32, 'big')[::-1]
        
        # 应该失败（必须严格小于）
        self.assertFalse(validate_pow(hash_bytes, target))
    
    def test_bits_invalid_size(self):
        """测试非法大小的 bits"""
        with self.assertRaises(ValueError):
            bits_to_target(bytes(3))
        
        with self.assertRaises(ValueError):
            bits_to_target(bytes(5))
    
    def test_pow_invalid_hash_size(self):
        """测试非法大小的哈希"""
        with self.assertRaises(ValueError):
            validate_pow(bytes(31), 100)
        
        with self.assertRaises(ValueError):
            validate_pow(bytes(33), 100)


if __name__ == '__main__':
    unittest.main()
