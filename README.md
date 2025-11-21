# MCP Server - Generic API Call Tools

A Model Context Protocol (MCP) server that provides generic HTTP API request tools for making GET and POST API calls with flexible authentication and configuration options.

## Overview

This MCP server exposes two powerful tools that allow you to make HTTP API requests to any endpoint with runtime configuration. Perfect for integrating external APIs into your MCP-enabled applications without hardcoding endpoints or credentials.

## Features

- **Generic GET and POST requests** - Call any REST API endpoint
- **Flexible API key authentication** - Optional API key support
- **Custom headers** - Add any headers dynamically via JSON
- **Runtime configuration** - All parameters passed at runtime, no hardcoding
- **Comprehensive responses** - Returns status code, headers, and response data
- **Error handling** - Proper exception handling with informative messages

## Tools

### 1. `api_get_request`

Makes a generic GET API call to any endpoint.

**Parameters:**
- `url` (required): Full URL for the API endpoint
- `api_key` (optional): API key for authentication (added as 'x-api-key' header)
- `headers_json` (optional): JSON string of additional headers
- `timeout` (optional): Request timeout in seconds (default: 30)

**Example:**
```json
{
  "url": "https://api.example.com/v1/users/123",
  "api_key": "your-api-key-here",
  "headers_json": "{\"x-FormId\": \"TestForm\", \"Accept\": \"application/json\"}",
  "timeout": 30
}
```

### 2. `api_post_request`

Makes a generic POST API call to any endpoint.

**Parameters:**
- `url` (required): Full URL for the API endpoint
- `body_json` (required): JSON string of the request body
- `api_key` (optional): API key for authentication (added as 'x-api-key' header)
- `headers_json` (optional): JSON string of additional headers
- `timeout` (optional): Request timeout in seconds (default: 30)

**Example:**
```json
{
  "url": "https://api.example.com/v1/users",
  "body_json": "{\"name\": \"John Doe\", \"email\": \"john@example.com\"}",
  "api_key": "your-api-key-here",
  "headers_json": "{\"x-FormId\": \"CreateUser\"}",
  "timeout": 30
}
```

## Installation

### Prerequisites
- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installing uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternative (using pip):**
```bash
pip install uv
```

After installation, verify uv is installed:
```bash
uv --version
```

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-server-deployment-local-ops
```

2. Install dependencies:
```bash
uv sync
```

## Usage

### Testing with MCP Inspector

Test the server locally using the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uv run mcp-server
```

This will:
1. Start the MCP server
2. Launch the inspector web interface
3. Open your browser to test the tools interactively

### Integrating with Claude Desktop

Add to your Claude Desktop configuration file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "generic-api-tools": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\path\\to\\mcp-server-deployment-local-ops",
        "run",
        "mcp-server"
      ]
    }
  }
}
```

Replace `C:\\path\\to\\mcp-server-deployment-local-ops` with your actual installation path.

**Directly running thru GitHub**

```json
{
  "mcpServers": {
    "generic-api-tools": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/techwithashish1/mcp-server-api-call.git",
        "mcp-server"
      ]
    }
  }
}
```

### Using with Other MCP Clients

This server can be integrated with any MCP-compatible client. Configure the client to run:

```bash
uv run mcp-server
```

from the project directory.

## Response Format

Both tools return a structured response:

```json
{
  "status_code": 200,
  "headers": {
    "content-type": "application/json",
    "...": "..."
  },
  "data": {
    "...": "actual API response data"
  }
}
```

## Use Cases

- **API Testing** - Test any REST API without writing code
- **Data Integration** - Pull data from external services
- **Webhook Interactions** - Send POST requests to webhooks
- **Multi-API Workflows** - Chain multiple API calls together
- **Dynamic API Exploration** - Explore APIs without hardcoding credentials

## Development

### Project Structure

```
mcp-server-deployment-local-ops/
├── src/
│   └── mcp_server/
│       ├── __init__.py
│       ├── __main__.py       # Entry point
│       └── api_call.py       # API tools implementation
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

### Dependencies

- `mcp[cli]>=1.22.0` - Model Context Protocol framework
- `requests>=2.32.5` - HTTP library for making API calls

## Error Handling

The tools handle various error scenarios:

- **Invalid JSON** - Returns error if headers_json or body_json is malformed
- **HTTP Errors** - Raises exception for non-2xx status codes
- **Timeouts** - Configurable timeout with default of 30 seconds
- **Network Issues** - Proper error messages for connection failures

## Security Considerations

- **API Keys** - Pass API keys at runtime, never commit them to code
- **HTTPS** - Use HTTPS URLs for secure communication
- **Validation** - Server validates JSON input before making requests
- **Timeout** - Requests timeout to prevent hanging connections

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

[Add support contact information here]
