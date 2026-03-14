# 记忆 07: 下一步行动（当前状态）

## 🎯 当前状态

**当前步骤**: 步骤2 🟡 进行中
**下一步**: 完成 MerkleRoot 字段赋值
**日期**: 2026-03-14

---

## 📝 已完成（步骤1 + 步骤2 部分）

**步骤1** ✅
- [x] 创建 `go.mod`
- [x] 编写 `main.go` 输出 "Hello, Bitcoin!"
- [x] 验证能编译运行

**步骤2** 🟡 进行中
- [x] 创建 `block/header.go` 文件
- [x] 定义 `Header` 结构体（6个字段）
- [x] 学会导入本地包 `blockparser/block`
- [x] 学会用 `hex.DecodeString` 解码十六进制字符串
- [ ] 把 `[]byte` 转成 `[32]byte` 并赋值给结构体字段

---

## 🚀 下一步：完成哈希字段赋值

### 当前位置
你已经学会了用 `hex.DecodeString` 把十六进制字符串转成 `[]byte`。

### 下一个任务
把 `[]byte` 转成 `[32]byte` 并赋值给结构体。

### 代码提示
```go
// 1. 解码十六进制字符串
data, err := hex.DecodeString("4a5e1e4b...")
if err != nil {
    fmt.Println("Error:", err)
    return
}

// 2. 把 []byte 转成 [32]byte
var hash [32]byte
copy(hash[:], data)  // hash[:] 把数组转成切片

// 3. 赋值给结构体
h := block.Header{
    Version:    1,
    MerkleRoot: hash,  // 现在可以赋值了
    Timestamp:  1231006505,
    Bits:       0x1d00ffff,
    Nonce:      2083236893,
}
```

### 完成标志
- [ ] MerkleRoot 能正确赋值并打印
- [ ] PrevHash 也用同样方式赋值（全是 0 的哈希）
- [ ] 整个创世区块 Header 能完整打印

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
