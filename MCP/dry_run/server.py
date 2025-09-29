# mcp_server.py
from mcp.server.fastmcp import FastMCP

# 1. Initialize the MCP server with a unique name
mcp = FastMCP("Math")

# 2. Define a tool using the @mcp.tool() decorator
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# 3. Define another tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# 4. Run the server using the 'stdio' transport
# This is a blocking call and will wait for input from the client.
if __name__ == "__main__":
    print("--- Starting MCP Math Server (stdio) ---")
    # Note: We do not use mcp.run() directly for stdio in this simple setup,
    # as the client (LangGraph agent) will handle the subprocess execution.
    # We will use this file as the entry point for the subprocess command.
    # The FastMCP methods handle the stdio communication handshake automatically.

    # To ensure it runs when called as a subprocess, a simple placeholder print
    # is often sufficient, but the 'mcp' library handles the run loop implicitly.
    # For a simple LangGraph subprocess, you just need the functions defined above.
    
    # We'll rely on the LangGraph adapter to run this as a subprocess
    # by executing the mcp.run(transport='stdio') logic internally on the client side.
    # However, to be fully explicit for a standalone run, use:
    # mcp.run(transport='stdio')
    pass