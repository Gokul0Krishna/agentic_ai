from mcp.server.fastmcp import FastMCP
import pandas as pd

mcp = FastMCP("Kill")

@mcp.tool
def Null_checker(df:pd.DataFrame):
    'checks for null values in a dataframe'
    null_count = df.isnull().sum()
    if null_count.sum()>0:
        return null_count.abs()
    else:
        return False