# MCP Calculator

一个简单的计算器 MCP 服务器，提供加法功能。

## 功能

- `add`: 计算两个数字的和

## 安装
```bash
pip install mcp-calculatorA
```

## 使用

在 Claude Desktop 配置文件中添加：
```json
{
  "mcpServers": {
    "calculator": {
      "command": "mcp-calculatorA"
    }
  }
}
```