from mcp_server.server import run_server

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_server())
    print('Shutting down the server')