# main.py
import os
import subprocess
from langchain_community.chat_models import ChatOllama
from langchain_mcp_adapters.tools import MCPTool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


def main():
    # Path to your local MCP server file
    MCP_SERVER_FILE = "server.py"

    # Start MCP server as a subprocess (stdio transport)
    server_process = subprocess.Popen(
        ["python", MCP_SERVER_FILE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )

    # Create MCPTool with raw stdio pipes
    mcp_tool = MCPTool(
        name="math",
        description="Math MCP tool",
        stdin=server_process.stdin,
        stdout=server_process.stdout,
    )

    # Wrap into list for agent
    mcp_tools = [mcp_tool]

    print(f"Loaded MCP Tools: {[t.name for t in mcp_tools]}")

    # --- 2. Set up the LangGraph Agent with Llama 3.2 (Ollama) ---

    llm = ChatOllama(
        model="llama3.2",  # Llama 3.2 model pulled via Ollama
        temperature=0,
        base_url="http://localhost:11434"
    )

    # Create the ReAct agent
    agent_executor = create_react_agent(
        model=llm,
        tools=mcp_tools,
        checkpointer=MemorySaver(),
    )

    # Example run
    result = agent_executor.invoke({"messages": [("user", "What is 2+2?")]})
    print("Agent result:", result)


if __name__ == "__main__":
    main()
