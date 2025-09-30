# main.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent


async def main():
    server_params = StdioServerParameters(
        command="python",
        # 👇 Replace with the absolute path to your server file
        args=[r"C:\Users\ASUS\OneDrive\Desktop\code\agentic ai\MCP\dry_run\server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Load tools from the MCP server
            tools = await load_mcp_tools(session)
            print("Loaded tools:", tools)

            # Create and run the agent
            agent = create_react_agent("openai:gpt-4.1", tools)
            response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            print("Agent response:", response)


if __name__ == "__main__":
    asyncio.run(main())
