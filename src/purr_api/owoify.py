"""Text transformation endpoints for the PurrBot API."""
from typing import Dict, Any
from urllib.parse import quote
from .base import BaseEndpoint

class OwoifyEndpoint(BaseEndpoint):
    """Endpoint for owoifying text."""

    def __init__(self, parent_base_url: str):
        """Initialize the owoify endpoint.

        Args:
            parent_base_url (str): The parent base URL for this endpoint.
        """
        super().__init__(parent_base_url, "/owoify")

    def get(self, text: str) -> str:
        """Owoify the given text.

        Args:
            text (str): The text to owoify.

        Returns:
            str: The owoified text.

        Example:
            >>> purr = Purr()
            >>> purr.owoify.get("Hello, World!")
            'Hewwo, Wowwd!'
        """
        response = self._make_request(f"?text={quote(text)}")
        return self._handle_response(response) 