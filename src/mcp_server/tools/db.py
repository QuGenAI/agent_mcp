import sqlite3

# from mcp.server.fastmcp import FastMCP

# mcp = FastMCP("SQLite Explorer")


# @mcp.resource("schema://main")
def get_schema() -> str:
    """Provide the database schema as a resource"""
    conn = sqlite3.connect("database.db")
    try:
        schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table'").fetchall()
        return "\n".join(sql[0] for sql in schema if sql[0])
    except sqlite3.Error as e:
        return f"\nError: {str(e)}"
    

# @mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely"""
    conn = sqlite3.connect("database.db")
    try:
        result = conn.execute(sql).fetchall()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        return f"Error: {str(e)}"