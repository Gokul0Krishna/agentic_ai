import os
import subprocess
from langchain_community.chat_models import ChatOllama  # <-- New Import
from langchain_mcp_adapters.tools.tool import MCPTool
from langchain_mcp_adapters.server_runners import StdioServerRunner
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

def main():
    # agent_client.py (Modified LLM section)

    # ... (MCP Server Setup remains the same)

    # The path to our local MCP server file
    MCP_SERVER_FILE = "mcp_server.py"

    # Create a runner for the server (unchanged)
    server_runner = StdioServerRunner(
        subprocess_command=["python", MCP_SERVER_FILE]
    )
    mcp_tool = MCPTool(server_runner=server_runner, name="math")
    mcp_tools = mcp_tool.list_tools()
    print(f"Loaded MCP Tools: {[t.name for t in mcp_tools]}")


    # --- 2. Set up the LangGraph Agent with Llama 3.2 ---

    # Define the LLM using ChatOllama
    llm = ChatOllama(
        model="llama3.2", # <-- Specify the Llama 3.2 model pulled with Ollama
        temperature=0,
        # Ollama typically runs on this local address
        base_url="http://localhost:11434" 
    )

    # NOTE: For tool-calling agents, the local model (Llama 3.2)
    # MUST be capable and often explicitly fine-tuned for tool/function calling.
    # Llama models often use a specific structured prompt format for this, 
    # which LangChain/Ollama's integration handles.

    # Create the agent using the prebuilt ReAct executor
    agent_executor = create_react_agent(
        model=llm,
        tools=mcp_tools,  # Pass the MCP tools here
        checkpointer=MemorySaver(),
    )

    # ... (Agent run logic remains the same)


if __name__ == "__main__":
    main()
