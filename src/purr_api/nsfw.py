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
        
    class _Blowjob(BaseEndpoint):
        """NSFW blowjob GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "blowjob")

        def get(self) -> str:
            """Get a random NSFW blowjob GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Cum(BaseEndpoint):
        """NSFW cum GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "cum")

        def get(self) -> str:
            """Get a random NSFW cum GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Fuck(BaseEndpoint):
        """NSFW fuck GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "fuck")

        def get(self) -> str:
            """Get a random NSFW fuck GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Neko(BaseEndpoint):
        """NSFW neko images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "neko")

        def get(self, type: Literal["img", "gif"] = "img") -> str:
            """Get a random NSFW neko image.

            Args:
                type (Literal["img", "gif"]): The type of image to get.

            Returns:
                str: URL to the image.
            """
            response = self._make_request(type)
            return self._handle_response(response)
    
    class _Pussylicking(BaseEndpoint):
        """NSFW pussylicking GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "pussylicking")

        def get(self) -> str:
            """Get a random NSFW pussylicking GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Solo(BaseEndpoint):
        """NSFW female solo GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "solo")

        def get(self) -> str:
            """Get a random NSFW solo GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Solo_Male(BaseEndpoint):
        """NSFW male solo GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "solo_male")

        def get(self) -> str:
            """Get a random NSFW male solo GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
    
    class _Threesome_fff(BaseEndpoint):
        """NSFW threesome GIFs with 3 female characters."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "threesome_fff")

        def get(self) -> str:
            """Get a random NSFW threesome GIF with 3 female characters.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Threesome_ffm(BaseEndpoint):
        """NSFW threesome GIFs with 2 female characters and 1 male character."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "threesome_ffm")

        def get(self) -> str:
            """Get a random NSFW threesome GIF with 2 female characters and 1 male character.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
        
    class _Threesome_mmf(BaseEndpoint):
        """NSFW threesome GIFs with 2 male characters and 1 female character."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "threesome_mmf")

        def get(self) -> str:
            """Get a random NSFW threesome GIF with 2 male characters and 1 female character.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Yaoi(BaseEndpoint):
        """NSFW yaoi GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "yaoi")

        def get(self) -> str:
            """Get a random NSFW yaoi GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Yuri(BaseEndpoint):
        """NSFW yuri GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "yuri")

        def get(self) -> str:
            """Get a random NSFW yuri GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)
