class PurrBotError(Exception):
    """Base exception for PurrBot API errors."""
    pass

class APIError(PurrBotError):
    """Raised when the API returns an error response."""
    def __init__(self, response_code: int, message: str):
        self.response_code = response_code
        self.message = message
        super().__init__(f"API Error {response_code}: {message}")

class NetworkError(PurrBotError):
    """Raised when there's a network-related error."""
    pass

class InvalidEndpointError(PurrBotError):
    """Raised when trying to access an invalid endpoint."""
    pass 