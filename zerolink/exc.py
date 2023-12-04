class APIError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class AuthenticationError(Exception):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "No API key. Please run `zerolink key` or set the ZEROLINK_API_KEY environment variable"
