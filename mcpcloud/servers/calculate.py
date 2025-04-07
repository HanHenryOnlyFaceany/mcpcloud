from mcp.server.fastmcp import FastMCP

# Initialize MCP server with version and description
mcp = FastMCP(
    name="add-server",
    version="0.1.0",
    description="A simple calculator server that provides basic arithmetic operations"
)

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    计算两个整数的和。

    Args:
        a: 第一个整数。
        b: 第二个整数。

    Returns:
        两个整数的和。
    """
    return a + b

if __name__ == "__main__":
    print(f"Running MCP server version")
    mcp.run(transport='stdio')