"""Base module for PurrBot API endpoints."""
import requests
from typing import Optional, Dict, Any
from .exceptions import APIError, NetworkError

class BaseEndpoint:
    """Base class for all PurrBot API endpoints."""

    def __init__(self, parent_base_url: str, endpoint: str = "") -> None:
        """Initialize a base endpoint.

        Args:
            parent_base_url (str): The parent base URL for this endpoint
            endpoint (str, optional): The specific endpoint path. Defaults to "".
        """
        self._base_url = f"{parent_base_url.rstrip('/')}/{endpoint.lstrip('/')}" if endpoint else parent_base_url
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json"
        }

    def _make_request(self, path: str = "") -> Dict[str, Any]:
        """Make a request to the API and return the JSON response.

        Args:
            path (str, optional): Additional path to append to the base URL. Defaults to "".

        Returns:
            Dict[str, Any]: The JSON response from the API.

        Raises:
            NetworkError: If there's a network-related error.
            APIError: If the API returns an error response.
        """
        try:
            url = f"{self._base_url.rstrip('/')}/{path.lstrip('/')}" if path else self._base_url
            response = requests.get(url.rstrip("/"), headers=self._headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get("error", False):
                raise APIError(
                    response_code=data.get("response-code", 0),
                    message=data.get("message", "Unknown API error")
                )
            return data
            
        except requests.RequestException as e:
            raise NetworkError(f"Failed to connect to API: {str(e)}")

    def _handle_response(self, response: Dict[str, Any]) -> str:
        """Handle the API response and return the appropriate value.

        Args:
            response (Dict[str, Any]): The JSON response from the API.

        Returns:
            str: The link or text from the response.
        """
        return response.get("link") or response.get("text", "") 