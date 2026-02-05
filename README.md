# MCP Calculator

一个简单的计算器 MCP (Model Context Protocol) 服务器，为 Claude 提供计算功能。

## 功能

| 工具 | 描述 | 参数 |
|------|------|------|
| `add` | 计算两个数字的和 | `a`: 第一个数字, `b`: 第二个数字 |

## 安装

### 从源码安装（开发模式）

```bash
# 克隆仓库
git clone https://github.com/yourusername/mcp-calculatorA.git
cd mcp-calculatorA

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -e .
```

### 从 PyPI 安装

```bash
pip install mcp-calculatorA
```

## 配置

### Claude Code

编辑 `~/.claude/claude_mcp_settings.json`:

```json
{
  "mcpServers": {
    "calculatorA": {
      "command": "/path/to/venv/bin/python",
      "args": ["-m", "mcp_calculatora"]
    }
  }
}
```

### Claude Desktop

编辑配置文件:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "calculatorA": {
      "command": "mcp-calculatorA"
    }
  }
}
```

## 使用示例

配置完成后，Claude 可以直接调用计算器功能：

```
用户: 计算 55 + 99
Claude: [调用 add 工具] 55 + 99 = 154
```

## 项目结构

```
mcp-calculatorA/
├── mcp_calculatora/
│   ├── __init__.py
│   └── server.py      # MCP 服务器实现
├── pyproject.toml     # 项目配置
└── README.md
```

## 开发

```bash
# 运行服务器（测试）
python -m mcp_calculatora
```

## 许可证

MIT License