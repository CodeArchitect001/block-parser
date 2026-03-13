# 记忆 05: 问题记录与解决

## ✅ 已解决的问题

### 问题 1: Python 版本的字节序混淆
- **现象**: 哈希比较时结果不正确
- **原因**: 区块哈希是小端序存储，比较大小时需要翻转成大端序
- **解决**: `validate_pow` 函数中先翻转再比较
- **经验**: 存储是小端序，显示/比较是大端序

### 问题 2: Bits 格式理解错误
- **现象**: 难度目标计算错误
- **原因**: 混淆了系数和指数的字节序
- **解决**: 系数是 3 字节小端序，指数是 1 字节原样
- **公式**: `Target = Coefficient * 256^(Exponent-3)`

---

## 🐛 待解决问题

- 无

---

## 💡 常见错误预警

### Go 语言常见错误

#### 错误 1: 字节序搞反了
```go
// 错误：用大端序解析
version := binary.BigEndian.Uint32(data[0:4])  // 得到 16777216

// 正确：用小端序
version := binary.LittleEndian.Uint32(data[0:4])  // 得到 1
```

#### 错误 2: 数组切片混淆
```go
var arr [32]byte
slice := data[4:36]

// 错误：不能直接赋值
arr = slice  // 编译错误！

// 正确：使用copy
copy(arr[:], slice)
```

#### 错误 3: 哈希比较时没翻转
```go
hash := DoubleSHA256(data)  // 小端序字节
hashInt := new(big.Int).SetBytes(hash)  // 错误！应该翻转

// 正确：先翻转再比较
for i, j := 0, len(hash)-1; i < j; i, j = i+1, j-1 {
    hash[i], hash[j] = hash[j], hash[i]
}
```

---

## 📝 踩坑记录模板

```markdown
### 问题 X: 标题
- **日期**: YYYY-MM-DD
- **现象**: 具体错误表现
- **原因**: 根本原因分析
- **解决**: 解决方案
- **预防**: 如何避免再次发生
```
