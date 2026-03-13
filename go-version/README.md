# 比特币区块头解析器 - Go 版本

> ⚠️ **重要提示**：这是你自己的练习项目，不要复制任何现成代码！

---

## 🎯 学习目标

通过手动实现这个项目，掌握：
1. Go 语言基础（类型系统、结构体、方法）
2. 二进制数据处理（byte slices、encoding/binary）
3. 密码学基础（crypto/sha256）
4. 测试编写（testing 包）

---

## 📁 项目结构（建议）

```
go-version/
├── go.mod                    # Go模块文件
├── main.go                   # 入口文件（CLI）
├── block/
│   ├── header.go            # BlockHeader结构体
│   ├── hash.go              # 哈希工具
│   └── difficulty.go        # 难度计算
├── parser/
│   └── parser.go            # 解析器主逻辑
└── block_test.go            # 测试文件
```

---

## 📚 你需要提前学习的Go知识

### 1. 基础语法（1小时）
```go
// 变量声明
var x uint32 = 1
y := 1  // 短变量声明

// 结构体
type Person struct {
    Name string
    Age  int
}

// 方法
func (p Person) SayHello() {
    fmt.Println("Hello, I'm", p.Name)
}

// 数组 vs Slice
var arr [32]byte          // 固定长度数组
slice := make([]byte, 32) // 动态切片
```

### 2. 二进制处理（重点！）
```go
import "encoding/binary"

// 小端序解码（Little Endian）
data := []byte{0x01, 0x00, 0x00, 0x00}
var num uint32
binary.Read(bytes.NewReader(data), binary.LittleEndian, &num)
// num 应该等于 1

// 大端序解码
binary.Read(bytes.NewReader(data), binary.BigEndian, &num)
// num 应该等于 16777216 (0x01000000)
```

### 3. SHA256哈希
```go
import "crypto/sha256"

// 计算哈希
hash := sha256.Sum256(data)  // 返回 [32]byte

// 双SHA256
first := sha256.Sum256(data)
second := sha256.Sum256(first[:])  // [:] 将数组转为切片
```

---

## 📝 实现步骤（按这个顺序）

### 步骤 1: 初始化项目（10分钟）

**任务**：
1. 创建目录 `go-version`
2. 运行 `go mod init blockparser`
3. 创建文件 `main.go`，确保能编译运行

**检查点**：
```bash
cd go-version
go run main.go
# 应该输出 "Hello, Bitcoin!"
```

---

### 步骤 2: 定义 BlockHeader 结构体（30分钟）

**任务**：在 `block/header.go` 中定义：

```go
type BlockHeader struct {
    Version    uint32
    PrevHash   [32]byte    // 固定长度数组！
    MerkleRoot [32]byte
    Timestamp  uint32
    Bits       [4]byte     // 或者 uint32，你自己决定
    Nonce      uint32
}
```

**需要思考**：
- 为什么 PrevHash 用 `[32]byte` 而不是 `[]byte`？
- Bits 应该用什么类型？

**检查点**：
```go
header := BlockHeader{
    Version: 1,
    // 其他字段...
}
fmt.Printf("%+v\n", header)
```

---

### 步骤 3: 实现 ParseHeader 函数（1小时）

**任务**：实现从 `[]byte` 解析区块头

**提示**：
```go
func ParseHeader(data []byte) (BlockHeader, error) {
    if len(data) != 80 {
        return BlockHeader{}, errors.New("invalid length")
    }
    
    var h BlockHeader
    
    // 解析 Version (前4字节，小端序)
    // 使用 binary.LittleEndian.Uint32()
    
    // 解析 PrevHash (接下来32字节)
    // 直接复制: copy(h.PrevHash[:], data[4:36])
    
    // 继续其他字段...
    
    return h, nil
}
```

**测试数据**：
```go
// 创世区块头（前8字节）
genesis := []byte{
    0x01, 0x00, 0x00, 0x00,  // version = 1 (小端序)
    0x00, 0x00, 0x00, 0x00,  // timestamp的前4字节
}
```

**检查点**：
```bash
go test -v
# 应该看到测试通过
```

---

### 步骤 4: 实现双 SHA256（30分钟）

**任务**：在 `block/hash.go` 中实现

**要求**：
```go
func DoubleSHA256(data []byte) []byte {
    // 实现双SHA256
}

func CalculateBlockHash(header BlockHeader) string {
    // 1. 将header序列化为[]byte
    // 2. 计算DoubleSHA256
    // 3. 翻转字节序（小端序→大端序）
    // 4. 返回十六进制字符串
}
```

**验证标准**：
- 创世区块哈希 = `000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`

---

### 步骤 5: 实现难度计算（1小时）

**任务**：在 `block/difficulty.go` 中实现

**公式**：
```
Target = Coefficient * 256^(Exponent - 3)
```

**提示**：
```go
func BitsToTarget(bits [4]byte) *big.Int {
    // 系数 = 前3字节（小端序）
    coefficient := binary.LittleEndian.Uint32(append(bits[:3], 0))
    
    // 指数 = 最后1字节
    exponent := bits[3]
    
    // 计算: coefficient * 256^(exponent-3)
    // 使用 math/big 包
}
```

---

### 步骤 6: 整合测试（30分钟）

**任务**：编写完整测试

**测试用例**：
1. 解析创世区块
2. 验证哈希计算正确
3. 验证PoW通过
4. 修改nonce后PoW失败

---

## 🔍 常见错误（先自己踩坑再看）

<details>
<summary>点击展开（先自己尝试后再看）</summary>

### 错误 1: 字节序搞反了
```go
// 错误：用大端序解析
version := binary.BigEndian.Uint32(data[0:4])  // 得到 16777216

// 正确：用小端序
version := binary.LittleEndian.Uint32(data[0:4])  // 得到 1
```

### 错误 2: 数组切片混淆
```go
var arr [32]byte
slice := data[4:36]

// 错误：不能直接赋值
arr = slice  // 编译错误！

// 正确：使用copy
copy(arr[:], slice)
```

### 错误 3: 哈希比较时没翻转
```go
hash := DoubleSHA256(data)  // 小端序字节
hashInt := new(big.Int).SetBytes(hash)  // 错误！应该翻转

// 正确：先翻转再比较
for i, j := 0, len(hash)-1; i < j; i, j = i+1, j-1 {
    hash[i], hash[j] = hash[j], hash[i]
}
```

</details>

---

## 📖 学习资源

### Go 官方文档
- [A Tour of Go](https://go.dev/tour/) - 快速入门（1小时）
- [Go by Example](https://gobyexample.com/) - 示例大全

### 关键包文档
- [encoding/binary](https://pkg.go.dev/encoding/binary) - 二进制处理
- [crypto/sha256](https://pkg.go.dev/crypto/sha256) - SHA256
- [math/big](https://pkg.go.dev/math/big) - 大整数运算

### 参考项目（只看接口，不看实现）
- [btcd](https://github.com/btcsuite/btcd) - 比特币Go实现
  - 只看 `wire/blockheader.go` 的接口定义
  - 不要看具体实现！

---

## ✅ 完成标准

你必须能够：
1. ✅ 独立实现所有功能（不参考AI代码）
2. ✅ 通过全部测试用例
3. ✅ 能够解释每一行代码的原理
4. ✅ 能够处理错误情况（非法输入等）

---

## 🆘 求助指南

当你卡住时：
1. **先查官方文档**（pkg.go.dev）
2. **写个小实验**验证你的想法
3. **可以问我**，但要说清楚：
   - 你想做什么
   - 你尝试了哪些方法
   - 遇到了什么错误

**不要问**："这段代码怎么写？"
**可以问**："我用 binary.LittleEndian 解析出来是错的，是不是理解错字节序了？"

---

## 🚀 开始吧！

第一步：创建项目并输出 "Hello, Bitcoin!"

完成后告诉我，我会给你下一步的指导。

加油！💪
