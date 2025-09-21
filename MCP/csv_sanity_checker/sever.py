from mcp.server.fastmcp import FastMCP
import pandas as pd
from file_functions import File

mcp = FastMCP("Kill")

@mcp.tool()
def Exploratory_analysis(file_path:str):
    'performs exploratory data analysis'
    file=File(file_location=file_path)
    return file.discribe_df()

if __name__ == "__main__":
    mcp.run()