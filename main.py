#!/usr/bin/env python3
"""
比特币区块头解析器 - 命令行工具

Usage:
    python main.py --hex <hex_string>
    python main.py --file <binary_file>
    python main.py --test  # 运行测试

Example:
    python main.py --hex 0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c
"""

import argparse
import sys
from src.parser import BlockParser


def main():
    parser = argparse.ArgumentParser(
        description='比特币区块头解析器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 解析十六进制区块头
  python main.py --hex 01000000...
  
  # 从二进制文件解析
  python main.py --file block_header.bin
  
  # 运行测试
  python main.py --test
        """
    )
    
    parser.add_argument('--hex', metavar='HEX', help='十六进制格式的区块头（160 个字符）')
    parser.add_argument('--file', metavar='FILE', help='二进制区块头文件')
    parser.add_argument('--test', action='store_true', help='运行测试用例')
    
    args = parser.parse_args()
    
    # 如果没有参数，显示帮助
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    # 运行测试
    if args.test:
        import unittest
        loader = unittest.TestLoader()
        start_dir = 'tests'
        suite = loader.discover(start_dir)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        return
    
    # 从十六进制解析
    if args.hex:
        try:
            raw_bytes = bytes.fromhex(args.hex)
            process_header(raw_bytes)
        except ValueError as e:
            print(f"错误: 无效的十六进制字符串 - {e}")
            sys.exit(1)
        return
    
    # 从文件解析
    if args.file:
        try:
            with open(args.file, 'rb') as f:
                raw_bytes = f.read()
            process_header(raw_bytes)
        except FileNotFoundError:
            print(f"错误: 文件未找到 - {args.file}")
            sys.exit(1)
        except IOError as e:
            print(f"错误: 无法读取文件 - {e}")
            sys.exit(1)
        return


def process_header(raw_bytes: bytes):
    """
    处理区块头数据
    
    Args:
        raw_bytes: 区块头字节数据
    """
    print()
    
    # 检查大小
    if len(raw_bytes) != 80:
        print(f"⚠️  警告: 区块头应该是 80 字节，实际 {len(raw_bytes)} 字节")
        print()
    
    try:
        # 解析区块头
        header = BlockParser.parse_header(raw_bytes)
        
        # 打印详细信息
        BlockParser.print_header(header)
        
        # 检查是否为创世区块
        if BlockParser.is_genesis_block(header):
            print("\n🌟 这是比特币创世区块！")
        
    except Exception as e:
        print(f"❌ 解析失败: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
