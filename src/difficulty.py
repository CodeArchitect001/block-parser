"""
难度目标计算

比特币使用 compact bits 格式存储难度目标，需要展开为 256 位目标值。
"""


def bits_to_target(bits: bytes) -> int:
    """
    将 compact bits 转换为目标值
    
    Bits 格式（4 字节）:
        [系数 3 字节（小端序）][指数 1 字节]
    
    计算公式:
        Target = Coefficient * 256^(Exponent - 3)
               = Coefficient * 2^(8 * (Exponent - 3))
    
    Args:
        bits: 4 字节的 bits 值
        
    Returns:
        目标值（大整数，最大 2^256-1）
        
    Example:
        >>> # 创世区块的 bits: 0x1d00ffff
        >>> bits = bytes.fromhex("ffff001d")
        >>> target = bits_to_target(bits)
        >>> hex(target)
        '0xffff0000000000000000000000000000000000000000000000000000...'
    """
    if len(bits) != 4:
        raise ValueError(f"Bits 必须是 4 字节，实际 {len(bits)} 字节")
    
    # 指数是最后一个字节
    exponent = bits[3]
    
    # 系数是前 3 字节（小端序）
    coefficient = int.from_bytes(bits[0:3], 'little')
    
    # 计算目标值
    # Target = Coefficient * 256^(Exponent - 3)
    target = coefficient * (256 ** (exponent - 3))
    
    return target


def target_to_bits(target: int) -> bytes:
    """
    将目标值转换为 compact bits
    
    这是 bits_to_target 的逆运算。
    
    Args:
        target: 目标值（大整数）
        
    Returns:
        4 字节的 bits 值
        
    Example:
        >>> target = 0xffff0000000000000000000000000000000000000000000000000000...
        >>> bits = target_to_bits(target)
        >>> bits.hex()
        'ffff001d'
    """
    # 转换为十六进制字符串（去掉 '0x' 前缀）
    hex_str = format(target, 'x')
    
    # 确保是偶数长度
    if len(hex_str) % 2 == 1:
        hex_str = '0' + hex_str
    
    # 计算指数
    # 字节数 = len(hex_str) / 2
    # 但是 compact 格式有 3 字节的系数，所以指数 = 字节数
    byte_length = len(hex_str) // 2
    
    if byte_length <= 3:
        # 目标值很小，可以直接放入系数
        coefficient = target
        exponent = 3
    else:
        # 提取系数（前 6 个十六进制字符 = 3 字节）
        coefficient = int(hex_str[0:6], 16)
        exponent = byte_length
        
        # 如果系数大于 0x7fffff，需要调整
        if coefficient > 0x7fffff:
            coefficient //= 256
            exponent += 1
    
    # 打包：系数（3 字节，小端序）+ 指数（1 字节）
    result = bytearray()
    result.extend(coefficient.to_bytes(3, 'little'))
    result.append(exponent)
    
    return bytes(result)


def validate_pow(block_hash: bytes, target: int) -> bool:
    """
    验证工作量证明
    
    规则：
        将 block_hash 解释为大端序整数，必须小于 target
    
    Args:
        block_hash: 32 字节的区块哈希（小端序存储）
        target: 难度目标值
        
    Returns:
        True 如果满足难度目标，False 否则
        
    Example:
        >>> block_hash = calculate_block_hash(header)
        >>> target = bits_to_target(header.bits)
        >>> if validate_pow(block_hash, target):
        ...     print("有效的区块！")
    """
    if len(block_hash) != 32:
        raise ValueError(f"区块哈希必须是 32 字节，实际 {len(block_hash)} 字节")
    
    # 区块哈希存储为小端序，但比较大小时需要翻转成大端序
    hash_int = int.from_bytes(block_hash[::-1], 'big')
    
    # 检查是否小于目标值
    return hash_int < target


def get_difficulty(bits: bytes) -> float:
    """
    获取相对难度
    
    难度 = 最大目标值 / 当前目标值
    
    创世区块的难度定义为 1.0
    
    Args:
        bits: 4 字节的 bits 值
        
    Returns:
        相对难度值
    """
    # 创世区块的目标值
    max_target = 0x00000000ffff0000000000000000000000000000000000000000000000000000
    
    current_target = bits_to_target(bits)
    
    return max_target / current_target


def format_target(target: int) -> str:
    """
    格式化目标值为易读字符串
    
    Args:
        target: 目标值
        
    Returns:
        格式化的十六进制字符串（64 位，带前导零）
    """
    return format(target, '064x')
