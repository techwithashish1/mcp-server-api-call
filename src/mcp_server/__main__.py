"""Entry point for MCP server application."""

from mcp_server.api_call import mcp


def main():
    """Entry point for the MCP server application."""
    mcp.run()

if __name__ == "__main__":
    main()
