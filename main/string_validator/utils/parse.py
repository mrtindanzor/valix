from main.shared.types import SafeParseErrorResult
from typing import TypeVar

T = TypeVar("T")

class ValidateString:
    def variable[T](self, data: object, error: str) -> SafeParseErrorResult | str:
        if not isinstance(data, str):
            return SafeParseErrorResult(success=False, error=error)

        return data

    def min(
        self, text: str, min_len: int, error: str
    ) -> SafeParseErrorResult | None:
        if len(text) < min_len:
            return SafeParseErrorResult(success=False, error=error)

    def max(
        self, text: str, max_len: int, error: str
    ) -> SafeParseErrorResult | None:
        if len(text) > max_len:
            return SafeParseErrorResult(success=False, error=error)
