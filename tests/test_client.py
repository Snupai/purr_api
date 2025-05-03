from purr_api.PurrBot import Purr
import pytest
import requests
from unittest.mock import Mock, patch, ANY

def test_client_initialization():
    # Test that client can be initialized
    client = Purr()
    assert client is not None

def test_client_endpoints():
    # Test that endpoints are properly set
    client = Purr()
    # Test SFW image endpoints
    assert hasattr(client.img.sfw, 'neko')
    assert hasattr(client.img.sfw, 'kitsune')
    # Test SFW GIF endpoints
    assert hasattr(client.img.sfw, 'angry')
    assert hasattr(client.img.sfw, 'hug')
    # Test owoify endpoint
    assert hasattr(client, 'owoify')

def test_sfw_image_request(mocker):
    # Mock the requests.get method
    mock_response = Mock()
    mock_response.json.return_value = {
        "error": False,
        "response-code": 200,
        "link": "https://cdn.purrbot.site/img/sfw/neko/img/neko_001.jpg"
    }
    mocker.patch('purr_api.base.requests.get', return_value=mock_response)

    # Test the actual request
    client = Purr()
    result = client.img.sfw.neko.get()
    
    # Verify the result
    assert result == "https://cdn.purrbot.site/img/sfw/neko/img/neko_001.jpg"
    # Verify the request was made to the correct URL
    requests.get.assert_called_once_with(
        "https://api.purrbot.site/v2/img/sfw/neko/img",
        headers=ANY,
        timeout=ANY
    )

def test_sfw_gif_request(mocker):
    # Mock the requests.get method
    mock_response = Mock()
    mock_response.json.return_value = {
        "error": False,
        "response-code": 200,
        "link": "https://cdn.purrbot.site/img/sfw/angry/gif/angry_001.gif"
    }
    mocker.patch('purr_api.base.requests.get', return_value=mock_response)

    # Test the actual request
    client = Purr()
    result = client.img.sfw.angry.get()
    
    # Verify the result
    assert result == "https://cdn.purrbot.site/img/sfw/angry/gif/angry_001.gif"
    # Verify the request was made to the correct URL
    requests.get.assert_called_once_with(
        "https://api.purrbot.site/v2/img/sfw/angry/gif",
        headers=ANY,
        timeout=ANY
    )

def test_owoify_request(mocker):
    # Mock the requests.get method
    mock_response = Mock()
    mock_response.json.return_value = {
        "error": False,
        "response-code": 200,
        "text": "Hewwo, Wowwd!"
    }
    mocker.patch('purr_api.base.requests.get', return_value=mock_response)

    # Test the actual request
    client = Purr()
    result = client.owoify.get("Hello, World!")
    
    # Verify the result
    assert result == "Hewwo, Wowwd!"
    # Verify the request was made to the correct URL with encoded text
    requests.get.assert_called_once_with(
        "https://api.purrbot.site/v2/owoify/?text=Hello%2C%20World%21",
        headers=ANY,
        timeout=ANY
    )

def test_api_error_handling(mocker):
    # Mock the requests.get method to return an error
    mock_response = Mock()
    mock_response.json.return_value = {
        "error": True,
        "response-code": 404,
        "message": "Endpoint not found"
    }
    mocker.patch('purr_api.base.requests.get', return_value=mock_response)

    # Test error handling
    client = Purr()
    with pytest.raises(Exception) as exc_info:
        client.img.sfw.neko.get()
    
    # Verify the error message
    assert "API Error 404: Endpoint not found" in str(exc_info.value) 