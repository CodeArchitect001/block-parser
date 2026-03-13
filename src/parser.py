"""
区块解析器主类

提供高级接口用于解析区块头和验证。
"""

from .block_header import BlockHeader
from .hash_utils import calculate_block_hash, hash_to_hex
from .difficulty import bits_to_target, validate_pow


class BlockParser:
    """
    区块解析器
    
    提供解析区块头和验证的便捷方法。
    """
    
    # 创世区块哈希（用于验证）
    GENESIS_BLOCK_HASH = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    
    @staticmethod
    def parse_header(raw_bytes: bytes) -> BlockHeader:
        """
        解析区块头
        
        Args:
            raw_bytes: 80 字节的区块头数据
            
        Returns:
            BlockHeader 实例
        """
        return BlockHeader.from_bytes(raw_bytes)
    
    @classmethod
    def get_block_hash(cls, header: BlockHeader) -> str:
        """
        获取区块哈希（大端序显示格式）
        
        Args:
            header: 区块头对象
            
        Returns:
            64 字符的十六进制字符串（大端序）
        """
        # 序列化区块头
        header_bytes = header.to_bytes()
        
        # 计算哈希
        block_hash = calculate_block_hash(header_bytes)
        
        # 转换为大端序显示
        return hash_to_hex(block_hash, reverse=True)
    
    @classmethod
    def validate_header(cls, header: BlockHeader) -> bool:
        """
        验证区块头是否满足工作量证明
        
        Args:
            header: 区块头对象
            
        Returns:
            True 如果有效，False 否则
        """
        # 计算区块哈希
        header_bytes = header.to_bytes()
        block_hash = calculate_block_hash(header_bytes)
        
        # 获取目标值
        target = bits_to_target(header.bits)
        
        # 验证 PoW
        return validate_pow(block_hash, target)
    
    @classmethod
    def is_genesis_block(cls, header: BlockHeader) -> bool:
        """
        检查是否为创世区块
        
        Args:
            header: 区块头对象
            
        Returns:
            True 如果是创世区块
        """
        block_hash = cls.get_block_hash(header)
        return block_hash == cls.GENESIS_BLOCK_HASH
    
    @staticmethod
    def print_header(header: BlockHeader) -> None:
        """
        打印区块头信息
        
        Args:
            header: 区块头对象
        """
        print("=" * 60)
        print("区块头信息")
        print("=" * 60)
        
        data = header.to_dict()
        
        print(f"Version:     {data['version']}")
        print(f"Prev Hash:   {data['prev_hash']}")
        print(f"Merkle Root: {data['merkle_root']}")
        print(f"Timestamp:   {data['timestamp']}")
        print(f"Bits:        {data['bits']}")
        print(f"Nonce:       {data['nonce']}")
        
        print("-" * 60)
        print(f"区块哈希:    {BlockParser.get_block_hash(header)}")
        print(f"PoW 验证:    {'✓ 通过' if BlockParser.validate_header(header) else '✗ 失败'}")
        print("=" * 60)


def parse_block_header(raw_bytes: bytes) -> dict:
    """
    解析区块头的便捷函数
    
    Args:
        raw_bytes: 80 字节的区块头数据
        
    Returns:
        包含解析结果的字典
    """
    parser = BlockParser()
    header = parser.parse_header(raw_bytes)
    
    return {
        'header': header,
        'block_hash': parser.get_block_hash(header),
        'valid': parser.validate_header(header),
        'is_genesis': parser.is_genesis_block(header)
    }
