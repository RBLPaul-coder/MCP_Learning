import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

print("Server starting...", file=sys.stderr)

# 创建服务器
server = Server("calculatorA")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    print("list_tools called", file=sys.stderr)
    return [
        types.Tool(
            name="add",
            description="计算两个数字的和(加法)",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "第一个数字"},
                    "b": {"type": "number", "description": "第二个数字"}
                },
                "required": ["a", "b"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    print(f"call_tool called: {name}", file=sys.stderr)
    if name == "add":
        a = arguments["a"]
        b = arguments["b"]
        result = a + b
        return [types.TextContent(type="text", text=f"{a} + {b} = {result}")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    print("main() starting...", file=sys.stderr)
    try:
        async with stdio_server() as (read_stream, write_stream):
            print("stdio_server connected", file=sys.stderr)
            await server.run(read_stream, write_stream, server.create_initialization_options())
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        raise

def run():
    """PyPI 入口点"""
    print("Starting server...", file=sys.stderr)
    asyncio.run(main())

if __name__ == "__main__":
    run()
