"""
哈希工具函数

比特币使用双 SHA256 哈希算法。
"""

import hashlib


def double_sha256(data: bytes) -> bytes:
    """
    计算双 SHA256 哈希
    
    比特币标准：对数据计算两次 SHA256
    hash = SHA256(SHA256(data))
    
    Args:
        data: 输入数据（任意长度）
        
    Returns:
        32 字节的哈希值
        
    Example:
        >>> result = double_sha256(b"Hello Bitcoin")
        >>> len(result)
        32
    """
    # 第一次 SHA256
    first_hash = hashlib.sha256(data).digest()
    
    # 第二次 SHA256
    second_hash = hashlib.sha256(first_hash).digest()
    
    return second_hash


def calculate_block_hash(block_header: bytes) -> bytes:
    """
    计算区块哈希
    
    区块哈希 = 区块头的双 SHA256 哈希
    
    注意：
        - 计算时区块头保持小端序（原始字节序）
        - 结果显示时要翻转成大端序
    
    Args:
        block_header: 80 字节的区块头数据
        
    Returns:
        32 字节的区块哈希（小端序）
        
    Example:
        >>> header = bytes.fromhex("01000000...")
        >>> block_hash = calculate_block_hash(header)
        >>> # 显示时翻转
        >>> print(block_hash[::-1].hex())
    """
    if len(block_header) != 80:
        raise ValueError(f"区块头必须是 80 字节，实际 {len(block_header)} 字节")
    
    return double_sha256(block_header)


def hash_to_hex(hash_bytes: bytes, reverse: bool = True) -> str:
    """
    将哈希字节转换为十六进制字符串
    
    Args:
        hash_bytes: 32 字节的哈希值
        reverse: 是否翻转字节序（显示用大端序）
        
    Returns:
        64 字符的十六进制字符串
    """
    if reverse:
        return hash_bytes[::-1].hex()
    return hash_bytes.hex()


def hex_to_hash(hex_string: str, reverse: bool = True) -> bytes:
    """
    将十六进制字符串转换为哈希字节
    
    Args:
        hex_string: 64 字符的十六进制字符串
        reverse: 是否翻转字节序
        
    Returns:
        32 字节的哈希值
    """
    hash_bytes = bytes.fromhex(hex_string)
    if reverse:
        return hash_bytes[::-1]
    return hash_bytes
