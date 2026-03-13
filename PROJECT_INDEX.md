# 项目记忆索引

> 按需加载记忆文件，避免上下文消耗

**当前状态**: 步骤1完成 | **分支**: `feature/go-implementation` | **日期**: 2026-03-13

---

## 📚 记忆文件索引

### 🎯 核心信息（必看）
| 文件 | 内容 | 何时查看 |
|------|------|----------|
| [memory/01-basic-info.md](./memory/01-basic-info.md) | 项目基本信息、目标 | 项目开始时 |
| [memory/07-next-steps.md](./memory/07-next-steps.md) | 当前步骤、下一步行动 | **每次编码前查看** |
| [memory/04-concepts.md](./memory/04-concepts.md) | 关键概念速查 | 遇到概念问题时 |

### 📋 进度跟踪
| 文件 | 内容 | 何时查看 |
|------|------|----------|
| [memory/03-roadmap.md](./memory/03-roadmap.md) | 完整学习路线图 | 规划学习时 |
| [memory/06-daily-log.md](./memory/06-daily-log.md) | 每日学习记录 | 回顾时 |

### 🔧 技术参考
| 文件 | 内容 | 何时查看 |
|------|------|----------|
| [memory/02-branches.md](./memory/02-branches.md) | 分支结构说明 | 切换分支时 |
| [memory/05-issues.md](./memory/05-issues.md) | 问题记录与解决 | 遇到相似问题时 |
| [memory/08-templates.md](./memory/08-templates.md) | 提问模板、检查清单 | 求助前 |

---

## 🚀 快速开始（现在该做什么）

**当前步骤**: 步骤1 ✅ 已完成  
**下一步**: [步骤2 - 定义 BlockHeader 结构体](./memory/07-next-steps.md)

### 今天已完成的
- [x] 创建 `go.mod`
- [x] 编写 `main.go` 输出 "Hello, Bitcoin!"
- [x] 验证能编译运行

### 明天要做的
查看 [memory/07-next-steps.md](./memory/07-next-steps.md) 了解详细任务

---

## 💡 使用指南

### 场景1：开始编码前
1. 打开 `memory/07-next-steps.md` - 看当前步骤
2. 打开 `memory/04-concepts.md` - 查相关概念
3. 开始编码

### 场景2：遇到问题时
1. 打开 `memory/05-issues.md` - 看是否已有解决方案
2. 打开 `memory/08-templates.md` - 按格式提问

### 场景3：记录今日学习
1. 打开 `memory/06-daily-log.md` - 添加今日记录
2. 更新 `memory/07-next-steps.md` - 标记完成任务

---

## 📝 文件创建命令

```bash
# 创建记忆目录
mkdir memory

# 初始化项目
cd go-version
go mod init blockparser

# 创建主文件
echo 'package main

import "fmt"

func main() {
    fmt.Println("Hello, Bitcoin!")
}' > main.go

# 运行
go run main.go
```

---

**提示**: 本文件是索引，详细内容请点击对应链接查看。
