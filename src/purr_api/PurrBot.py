"""Main module for the PurrBot API wrapper."""
from typing import Optional
import requests
from .sfw import SfwEndpoint
from .nsfw import NsfwEndpoint
from .owoify import OwoifyEndpoint

class Purr:
    """Main class for interacting with the PurrBot API.
    
    This class provides access to all PurrBot API endpoints through a simple interface.
    
    Example:
        >>> purr = Purr()
        >>> # Get a random angry GIF
        >>> angry_gif = purr.img.sfw.angry.get()
        >>> print(angry_gif)
        'https://cdn.purrbot.site/img/sfw/angry/gif/angry_001.gif'
    """

    def __init__(self):
        """Initialize the PurrBot API wrapper."""
        self._base_url = "https://api.purrbot.site/v2"
        self.img = self._Img(self._base_url)
        self.owoify = OwoifyEndpoint(self._base_url)

    class _Img:
        """Image endpoints for both SFW and NSFW content."""

        def __init__(self, parent_base_url: str):
            """Initialize image endpoints.

            Args:
                parent_base_url (str): The parent base URL for this endpoint.
            """
            self._base_url = f"{parent_base_url}/img"
            self.sfw = SfwEndpoint(self._base_url)
            self.nsfw = NsfwEndpoint(self._base_url)

    class _Owoify:
        def __init__(self, parent_base_url):
            self._base_url = f"{parent_base_url}/owoify"

        def get(self):
            response = requests.get(f"{self._base_url}/gif")
            response = response.json()
            if not response["error"]:
                return response["text"]
            else:
                return "Error: " + response["response-code"]
            

