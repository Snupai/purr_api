"""NSFW endpoints for the PurrBot API."""
from typing import Optional
from .base import BaseEndpoint

class NsfwEndpoint(BaseEndpoint):
    """NSFW endpoints for images and GIFs."""

    def __init__(self, parent_base_url: str):
        """Initialize NSFW endpoints.

        Args:
            parent_base_url (str): The parent base URL for this endpoint.
        """
        super().__init__(parent_base_url, "nsfw")
        self.anal = self._Anal(self._base_url)

    class _Anal(BaseEndpoint):
        """NSFW anal GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "anal")

        def get(self) -> str:
            """Get a random NSFW anal GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response) 