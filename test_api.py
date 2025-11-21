"""Test script for MCP server API tools."""

import json
from src.mcp_server.api_call import api_get_request, api_post_request


def test_get_request():
    """Test GET request with JSONPlaceholder API."""
    print("\n" + "="*60)
    print("TEST 1: GET Request - Fetch a single post")
    print("="*60)
    
    result = api_get_request(
        url="https://jsonplaceholder.typicode.com/posts/1",
        verify_ssl=False
    )
    
    print(f"Status Code: {result.get('status_code')}")
    print(f"Response Data: {json.dumps(result.get('data'), indent=2)}")
    
    if result.get('error'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return False
    else:
        print("✅ GET request successful!")
        return True


def test_get_request_with_headers():
    """Test GET request with custom headers."""
    print("\n" + "="*60)
    print("TEST 2: GET Request - With custom headers")
    print("="*60)
    
    result = api_get_request(
        url="https://jsonplaceholder.typicode.com/posts/2",
        headers_json='{"X-Custom-Header": "test-value"}',
        verify_ssl=False
    )
    
    print(f"Status Code: {result.get('status_code')}")
    print(f"Response Data: {json.dumps(result.get('data'), indent=2)}")
    
    if result.get('error'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return False
    else:
        print("✅ GET request with headers successful!")
        return True


def test_post_request():
    """Test POST request with JSONPlaceholder API."""
    print("\n" + "="*60)
    print("TEST 3: POST Request - Create a new post")
    print("="*60)
    
    result = api_post_request(
        url="https://jsonplaceholder.typicode.com/posts",
        body_json='{"title": "Test Post from MCP Server", "body": "This is a test post created by the MCP API server", "userId": 1}',
        verify_ssl=False
    )
    
    print(f"Status Code: {result.get('status_code')}")
    print(f"Response Data: {json.dumps(result.get('data'), indent=2)}")
    
    if result.get('error'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return False
    else:
        print("✅ POST request successful!")
        return True


def test_post_request_with_headers():
    """Test POST request with custom headers."""
    print("\n" + "="*60)
    print("TEST 4: POST Request - With custom headers")
    print("="*60)
    
    result = api_post_request(
        url="https://jsonplaceholder.typicode.com/posts",
        body_json='{"title": "Another Test", "body": "Testing with headers", "userId": 2}',
        headers_json='{"X-Test-Id": "test-123"}',
        verify_ssl=False
    )
    
    print(f"Status Code: {result.get('status_code')}")
    print(f"Response Data: {json.dumps(result.get('data'), indent=2)}")
    
    if result.get('error'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return False
    else:
        print("✅ POST request with headers successful!")
        return True


def test_get_list():
    """Test GET request that returns a list."""
    print("\n" + "="*60)
    print("TEST 5: GET Request - Fetch list of users")
    print("="*60)
    
    result = api_get_request(
        url="https://jsonplaceholder.typicode.com/users",
        verify_ssl=False
    )
    
    print(f"Status Code: {result.get('status_code')}")
    data = result.get('data', [])
    print(f"Number of users returned: {len(data) if isinstance(data, list) else 'N/A'}")
    if isinstance(data, list) and len(data) > 0:
        print(f"First user: {json.dumps(data[0], indent=2)}")
    
    if result.get('error'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return False
    else:
        print("✅ GET list request successful!")
        return True


def test_error_handling():
    """Test error handling with invalid JSON."""
    print("\n" + "="*60)
    print("TEST 6: Error Handling - Invalid JSON in headers")
    print("="*60)
    
    result = api_get_request(
        url="https://jsonplaceholder.typicode.com/posts/1",
        headers_json='{"invalid": json}',
        verify_ssl=False
    )
    
    if result.get('error'):
        print(f"✅ Error correctly caught: {result.get('error')}")
        print(f"Details: {result.get('details')}")
        return True
    else:
        print("❌ Should have caught invalid JSON error")
        return False


def main():
    """Run all tests."""
    print("\n" + "🚀 " + "="*56)
    print("🚀  MCP SERVER API CALL - COMPREHENSIVE TEST SUITE")
    print("🚀 " + "="*56)
    
    tests = [
        ("GET Request", test_get_request),
        ("GET with Headers", test_get_request_with_headers),
        ("POST Request", test_post_request),
        ("POST with Headers", test_post_request_with_headers),
        ("GET List", test_get_list),
        ("Error Handling", test_error_handling),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Test '{name}' threw exception: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {name}")
    
    print("\n" + "-"*60)
    print(f"Total: {passed}/{total} tests passed")
    print("="*60 + "\n")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
