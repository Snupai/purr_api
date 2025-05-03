"""Safe for work endpoints for the PurrBot API."""
from typing import Optional
from .base import BaseEndpoint

class SfwEndpoint(BaseEndpoint):
    """Safe for work endpoints for images and GIFs."""

    def __init__(self, parent_base_url: str):
        """Initialize SFW endpoints.

        Args:
            parent_base_url (str): The parent base URL for this endpoint.
        """
        super().__init__(parent_base_url, "sfw")
        self.angry = self._Angry(self._base_url)
        self.background = self._Background(self._base_url)
        self.bite = self._Bite(self._base_url)
        self.blush = self._Blush(self._base_url)
        self.comfy = self._Comfy(self._base_url)
        self.cry = self._Cry(self._base_url)
        self.cuddle = self._Cuddle(self._base_url)
        self.dance = self._Dance(self._base_url)
        self.eevee = self._Eevee(self._base_url)
        self.feed = self._Feed(self._base_url)
        self.fluff = self._Fluff(self._base_url)
        self.holo = self._Holo(self._base_url)
        self.hug = self._Hug(self._base_url)
        self.icon = self._Icon(self._base_url)
        self.kiss = self._Kiss(self._base_url)
        self.kitsune = self._Kitsune(self._base_url)
        self.lick = self._Lick(self._base_url)
        self.neko = self._Neko(self._base_url)
        self.pat = self._Pat(self._base_url)
        self.poke = self._Poke(self._base_url)
        self.pout = self._Pout(self._base_url)
        self.senko = self._Senko(self._base_url)
        self.ship = self._Ship(self._base_url)
        self.slap = self._Slap(self._base_url)
        self.smile = self._Smile(self._base_url)
        self.tail = self._Tail(self._base_url)
        self.tickle = self._Tickle(self._base_url)

    class _Angry(BaseEndpoint):
        """Angry reaction GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "angry")

        def get(self) -> str:
            """Get a random angry GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Background(BaseEndpoint):
        """Background images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "background")

        def get(self) -> str:
            """Get a random background image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Bite(BaseEndpoint):
        """Biting GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "bite")

        def get(self) -> str:
            """Get a random biting GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Blush(BaseEndpoint):
        """Blushing GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "blush")

        def get(self) -> str:
            """Get a random blushing GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Comfy(BaseEndpoint):
        """Comfy GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "comfy")

        def get(self) -> str:
            """Get a random comfy GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Cry(BaseEndpoint):
        """Crying GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "cry")

        def get(self) -> str:
            """Get a random crying GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Cuddle(BaseEndpoint):
        """Cuddling GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "cuddle")

        def get(self) -> str:
            """Get a random cuddling GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Dance(BaseEndpoint):
        """Dancing GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "dance")

        def get(self) -> str:
            """Get a random dancing GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Eevee(BaseEndpoint):
        """Eevee images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "eevee")

        def get(self, type: Literal["img", "gif"] = "img") -> str:
            """Get a random Eevee image.

            Args:
                type (Literal["img", "gif"]): The type of image to get.

            Returns:
                str: URL to the image.
            """
            response = self._make_request(type)
            return self._handle_response(response)

    class _Feed(BaseEndpoint):
        """Feeding GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "feed")

        def get(self) -> str:
            """Get a random feeding GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Fluff(BaseEndpoint):
        """Fluffing GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "fluff")

        def get(self) -> str:
            """Get a random fluffing GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Holo(BaseEndpoint):
        """Holo images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "holo")

        def get(self) -> str:
            """Get a random Holo image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Hug(BaseEndpoint):
        """Hugging GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "hug")

        def get(self) -> str:
            """Get a random hugging GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Icon(BaseEndpoint):
        """Icon images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "icon")

        def get(self) -> str:
            """Get a random icon image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Kiss(BaseEndpoint):
        """Kissing GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "kiss")

        def get(self) -> str:
            """Get a random kissing GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Kitsune(BaseEndpoint):
        """Kitsune images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "kitsune")

        def get(self) -> str:
            """Get a random kitsune image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Lick(BaseEndpoint):
        """Licking GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "lick")

        def get(self) -> str:
            """Get a random licking GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Neko(BaseEndpoint):
        """Neko images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "neko")

        def get(self, type: Literal["img", "gif"] = "img") -> str:
            """Get a random neko image.

            Args:
                type (Literal["img", "gif"]): The type of image to get.

            Returns:
                str: URL to the image.
            """
            response = self._make_request(type)
            return self._handle_response(response)

    class _Pat(BaseEndpoint):
        """Patting GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "pat")

        def get(self) -> str:
            """Get a random patting GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Poke(BaseEndpoint):
        """Poking GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "poke")

        def get(self) -> str:
            """Get a random poking GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Pout(BaseEndpoint):
        """Pouting GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "pout")

        def get(self) -> str:
            """Get a random pouting GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Senko(BaseEndpoint):
        """Senko images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "senko")

        def get(self) -> str:
            """Get a random Senko image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Ship(BaseEndpoint):
        """Shipping images."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "ship")

        def get(self) -> str:
            """Get a random shipping image.

            Returns:
                str: URL to the image.
            """
            response = self._make_request("img")
            return self._handle_response(response)

    class _Slap(BaseEndpoint):
        """Slapping GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "slap")

        def get(self) -> str:
            """Get a random slapping GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Smile(BaseEndpoint):
        """Smiling GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "smile")

        def get(self) -> str:
            """Get a random smiling GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Tail(BaseEndpoint):
        """Tail wagging GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "tail")

        def get(self) -> str:
            """Get a random tail wagging GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response)

    class _Tickle(BaseEndpoint):
        """Tickling GIFs."""
        def __init__(self, parent_base_url: str):
            super().__init__(parent_base_url, "tickle")

        def get(self) -> str:
            """Get a random tickling GIF.

            Returns:
                str: URL to the GIF.
            """
            response = self._make_request("gif")
            return self._handle_response(response) 