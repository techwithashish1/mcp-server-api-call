"""Generic API request tools for MCP server."""

import json
from typing import Optional
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GenericAPITool")

@mcp.tool()
def api_get_request(
    url: str,
    api_key: Optional[str] = None,
    headers_json: Optional[str] = None,
    timeout: int = 30
) -> dict:
    """
    Makes a generic GET API call.
    
    Args:
        url: The full URL for the API endpoint
        api_key: Optional API key for authentication (will be added to headers as 'x-api-key')
        headers_json: Optional JSON string of additional headers (e.g., '{"x-test-id": "Test", "Accept": "application/json"}')
        timeout: Request timeout in seconds (default: 30)
        
    Returns:
        dict: JSON response from the API including status_code, headers, and data
        
    Raises:
        requests.exceptions.RequestException: If the API call fails
    """
    try:
        # Build headers
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        # Add API key if provided
        if api_key:
            headers['x-api-key'] = api_key      
        # Add custom headers if provided
        if headers_json:
            custom_headers = json.loads(headers_json)
            headers.update(custom_headers)        
        # Make GET request
        response = requests.get(url, headers=headers, timeout=timeout)        
        # Raise an error for bad status codes
        response.raise_for_status()        
        # Return JSON response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "data": response.json()
        }        
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in headers_json parameter: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"API GET request failed: {e}")
        raise


@mcp.tool()
def api_post_request(
    url: str,
    body_json: str,
    api_key: Optional[str] = None,
    headers_json: Optional[str] = None,
    timeout: int = 30
) -> dict:
    """
    Makes a generic POST API call.
    
    Args:
        url: The full URL for the API endpoint
        body_json: JSON string of the request body (e.g., '{"name": "John", "age": 30}')
        api_key: Optional API key for authentication (will be added to headers as 'x-api-key')
        headers_json: Optional JSON string of additional headers (e.g., '{"x-test-id": "Test"}')
        timeout: Request timeout in seconds (default: 30)
        
    Returns:
        dict: JSON response from the API including status_code, headers, and data
        
    Raises:
        requests.exceptions.RequestException: If the API call fails
    """
    try:
        # Build headers
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        # Add API key if provided
        if api_key:
            headers['x-api-key'] = api_key
        # Add custom headers if provided
        if headers_json:
            custom_headers = json.loads(headers_json)
            headers.update(custom_headers)
        # Parse request body
        body = json.loads(body_json)
        # Make POST request
        response = requests.post(url, headers=headers, json=body, timeout=timeout)
        # Raise an error for bad status codes
        response.raise_for_status()
        # Return JSON response
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "data": response.json()
        }
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in parameters: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"API POST request failed: {e}")
        raise
