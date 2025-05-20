from .tools.calc import Calculator
from .tools.db import get_schema, query_data
from .tools.dir import FileSystem
from mcp.server.fastmcp import FastMCP
import signal
import sys
import time

def signal_handler(sig, frame):
    print("Shutting down server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def setup_server():
    # Set up the server with the necessary tools and options
    mcp_serve = FastMCP("MCR-Server")
    mcp_serve.add_tool(fn=Calculator.add, name="add",description="use this tool if you need take a sum of two numbers")
    mcp_serve.add_tool(fn=Calculator.subtract, name="subtract",description="use this tool if you need take a subtract of two numbers")
    mcp_serve.add_tool(fn=Calculator.multiply, name="multiply",description="use this tool if you need take a multiply of two numbers")
    mcp_serve.add_tool(fn=Calculator.divide, name="divide",description="use this tool if you need take a divide of two numbers")
    mcp_serve.add_tool(fn=Calculator.power, name="power",description="use this tool if you need take a power of two numbers")
    mcp_serve.add_tool(fn=Calculator.sqrt, name="sqrt",    description="use this tool if you need take a square root of a number")
    mcp_serve.add_tool(fn=get_schema, name="get_schema",description="use this tool if you need to get the schema of a database")
    mcp_serve.add_tool(fn=query_data, name="query_data",description="use this tool if you need to query data from a database")
    mcp_serve.add_tool(fn=FileSystem.get_files, name="get_files",description="use this tool if you need to get the files in a directory")
    mcp_serve.add_tool(fn=FileSystem.get_file_size, name="get_file_size",description="use this tool if you need to get the size of a file")
    mcp_serve.add_tool(fn=FileSystem.get_file_extension, name="get_file_extension",description="use this tool if you need to get the extension of a file")
    mcp_serve.add_tool(fn=FileSystem.merge_files, name="merge_files",  description="use this tool if you need to merge two files")
    mcp_serve.add_tool(fn=FileSystem.copy_file, name="copy_file",description="use this tool if you need to copy a file")
    # mcp_serve.add_tool(fn=move_file,name="move_file")
    return mcp_serve


def run_server():
    try:
        print("Starting MCP server...")
        mcp_serve = setup_server()
        mcp_serve.run(transport="stdio")
        
        print("Server started successfully.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

if __name__ == "__main__":
    try:
        print("Starting MCP server starting...")
        import asyncio
        asyncio.run(run_server())
        print("Server started successfully.")
        # import asyncio
        # asyncio.run(run_server())
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)



