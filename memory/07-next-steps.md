# 记忆 07: 下一步行动（当前状态）

## 🎯 当前状态

**当前步骤**: 步骤1 ✅ 已完成  
**下一步**: 步骤2 ⏳ 待开始  
**日期**: 2026-03-13

---

## 📝 已完成（步骤1）

- [x] 创建 `go.mod`
- [x] 编写 `main.go` 输出 "Hello, Bitcoin!"
- [x] 验证能编译运行

---

## 🚀 下一步（步骤2）：定义 BlockHeader 结构体

### 任务概述
定义表示比特币区块头的 Go 结构体，确定每个字段的类型。

### 预计时间
30 分钟

### 具体任务

#### 1. 创建 block/header.go 文件
```bash
mkdir block
touch block/header.go
```

#### 2. 定义 BlockHeader 结构体
```go
package block

type BlockHeader struct {
    Version    uint32
    PrevHash   [32]byte    // 注意：这是数组不是切片！
    MerkleRoot [32]byte
    Timestamp  uint32
    Bits       [4]byte     // 或者 uint32，你自己决定
    Nonce      uint32
}
```

#### 3. 关键思考点
- 为什么 `PrevHash` 用 `[32]byte` 而不是 `[]byte`？
  - 提示：数组长度固定，切片长度可变
  - 哈希长度是固定的 32 字节
- `Bits` 用 `[4]byte` 还是 `uint32` 更好？
  - 提示：考虑后续计算难度目标的方式

#### 4. 验证代码能编译
```bash
go build ./...
# 应该没有错误
```

### 完成标志
- [ ] `BlockHeader` 结构体定义完成
- [ ] 能创建实例并打印
- [ ] 代码能编译通过

### 示例验证代码
```go
func main() {
    header := BlockHeader{
        Version:   1,
        Timestamp: 1231006505,
        Nonce:     2083236893,
    }
    fmt.Printf("%+v\n", header)
}
```

---

## 📚 预习资料

### 需要理解的概念
1. **Go 结构体语法** - [Go by Example - Structs](https://gobyexample.com/structs)
2. **数组 vs 切片** - [Go by Example - Arrays](https://gobyexample.com/arrays)
3. **比特币区块头字段含义** - 查看 `../visual-guides/block-header.html`

### 关键问题（先思考，再查资料）
1. 数组 `[32]byte` 和切片 `[]byte` 的区别是什么？
2. 为什么比特币的哈希用固定长度数组更合适？
3. `uint32` 能表示的最大值是多少？足够存储时间戳吗？

---

## 🆘 遇到问题怎么办

### 卡住了？
1. 先查 [Go 官方文档](https://pkg.go.dev/)
2. 写个小实验验证你的想法
3. 按格式提问（见 [08-templates.md](./08-templates.md)）

### 不确定设计对不对？
- 先实现一版，能编译就行
- 后续步骤会验证是否正确
- 不对再改，迭代优化

---

## ⏭️ 完成后的下一步

完成步骤2后，进入 **步骤3：实现 ParseHeader 函数**

预览：
- 实现 `ParseHeader([]byte) (BlockHeader, error)`
- 使用 `encoding/binary` 包解析小端序
- 处理错误情况（长度检查）

---

**准备好了吗？明天开始步骤2！** 💪
