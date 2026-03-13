"""
集成测试

测试完整的工作流程。
"""

import unittest
from src.block_header import BlockHeader
from src.hash_utils import calculate_block_hash, hash_to_hex
from src.difficulty import bits_to_target, validate_pow
from src.parser import BlockParser


class TestIntegration(unittest.TestCase):
    """集成测试"""
    
    def setUp(self):
        """准备创世区块数据"""
        # 创世区块头（80 字节）
        self.genesis_hex = (
            "01000000"  # version = 1
            "0000000000000000000000000000000000000000000000000000000000000000"  # prev_hash
            "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"  # merkle_root
            "29ab5f49"  # timestamp = 1231006505
            "ffff001d"  # bits = 0x1d00ffff
            "1dac2b7c"  # nonce = 2083236893
        )
        self.genesis_bytes = bytes.fromhex(self.genesis_hex)
    
    def test_full_workflow_genesis(self):
        """测试完整的创世区块工作流程"""
        print("\n=== 集成测试：创世区块 ===")
        
        # 1. 解析区块头
        print("1. 解析区块头...")
        header = BlockHeader.from_bytes(self.genesis_bytes)
        self.assertEqual(header.version, 1)
        print(f"   [OK] Version: {header.version}")
        
        # 2. 序列化验证
        print("2. 验证序列化...")
        serialized = header.to_bytes()
        self.assertEqual(serialized, self.genesis_bytes)
        print("   [OK] 序列化/反序列化一致")
        
        # 3. 计算区块哈希
        print("3. 计算区块哈希...")
        block_hash = calculate_block_hash(self.genesis_bytes)
        hash_hex = hash_to_hex(block_hash, reverse=True)
        print(f"   区块哈希: {hash_hex}")
        
        # 验证哈希正确
        expected_hash = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
        self.assertEqual(hash_hex, expected_hash)
        print("   [OK] 哈希值正确")
        
        # 4. 计算目标值
        print("4. 计算难度目标...")
        target = bits_to_target(header.bits)
        print(f"   目标值: 0x{target:064x}")
        
        # 验证目标值正确
        expected_target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
        self.assertEqual(target, expected_target)
        print("   [OK] 目标值正确")
        
        # 5. 验证 PoW
        print("5. 验证 PoW...")
        is_valid = validate_pow(block_hash, target)
        self.assertTrue(is_valid)
        print("   [OK] PoW 验证通过")
        
        # 6. 使用 BlockParser 高级接口
        print("6. 使用 BlockParser 接口...")
        parser = BlockParser()
        
        # 解析
        parsed_header = parser.parse_header(self.genesis_bytes)
        self.assertEqual(parsed_header, header)
        
        # 获取哈希
        parser_hash = parser.get_block_hash(parsed_header)
        self.assertEqual(parser_hash, hash_hex)
        
        # 验证
        is_valid_parser = parser.validate_header(parsed_header)
        self.assertTrue(is_valid_parser)
        
        # 检查创世区块
        is_genesis = parser.is_genesis_block(parsed_header)
        self.assertTrue(is_genesis)
        print("   [OK] BlockParser 接口正常")
        
        print("\n=== All tests passed! ===\n")
    
    def test_modified_nonce_fails(self):
        """测试修改 nonce 后验证失败"""
        print("\n=== 测试：修改 nonce 后应失败 ===")
        
        # 解析创世区块
        header = BlockHeader.from_bytes(self.genesis_bytes)
        
        # 修改 nonce
        original_nonce = header.nonce
        header.nonce = original_nonce + 1
        print(f"原始 nonce: {original_nonce}")
        print(f"修改后 nonce: {header.nonce}")
        
        # 计算新哈希
        new_hash = calculate_block_hash(header.to_bytes())
        new_hash_hex = hash_to_hex(new_hash, reverse=True)
        print(f"新区块哈希: {new_hash_hex}")
        
        # 获取目标值
        target = bits_to_target(header.bits)
        
        # 验证应该失败
        is_valid = validate_pow(new_hash, target)
        self.assertFalse(is_valid)
        print("   [OK] 修改后 PoW 验证失败（符合预期）")
        
        print()
    
    def test_modified_timestamp_fails(self):
        """测试修改时间戳后验证失败"""
        print("\n=== 测试：修改时间戳后应失败 ===")
        
        # 解析创世区块
        header = BlockHeader.from_bytes(self.genesis_bytes)
        
        # 修改时间戳
        header.timestamp += 1
        
        # 验证应该失败
        parser = BlockParser()
        is_valid = parser.validate_header(header)
        self.assertFalse(is_valid)
        print("   [OK] 修改时间戳后 PoW 验证失败（符合预期）")
        
        print()


class TestParser(unittest.TestCase):
    """测试 BlockParser 类"""
    
    def setUp(self):
        self.genesis_hex = (
            "01000000"
            "0000000000000000000000000000000000000000000000000000000000000000"
            "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
            "29ab5f49"
            "ffff001d"
            "1dac2b7c"
        )
        self.genesis_bytes = bytes.fromhex(self.genesis_hex)
    
    def test_parse_header(self):
        """测试解析区块头"""
        header = BlockParser.parse_header(self.genesis_bytes)
        self.assertIsInstance(header, BlockHeader)
    
    def test_get_block_hash(self):
        """测试获取区块哈希"""
        header = BlockParser.parse_header(self.genesis_bytes)
        hash_hex = BlockParser.get_block_hash(header)
        
        self.assertEqual(len(hash_hex), 64)
        self.assertEqual(hash_hex, "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f")
    
    def test_validate_header(self):
        """测试验证区块头"""
        header = BlockParser.parse_header(self.genesis_bytes)
        self.assertTrue(BlockParser.validate_header(header))
    
    def test_is_genesis_block(self):
        """测试识别创世区块"""
        header = BlockParser.parse_header(self.genesis_bytes)
        self.assertTrue(BlockParser.is_genesis_block(header))
    
    def test_is_not_genesis_block(self):
        """测试识别非创世区块"""
        header = BlockParser.parse_header(self.genesis_bytes)
        header.nonce += 1  # 修改使其不是创世区块
        self.assertFalse(BlockParser.is_genesis_block(header))


if __name__ == '__main__':
    unittest.main(verbosity=2)
