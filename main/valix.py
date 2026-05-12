from typing import TypeGuard

from main.shared.types import (
    SafeParseErrorResult,
    SafeParseResult,
    SafeParseSuccessResult,
)
from main.string_validator.main import StringValidator
from main.validator_number.main import NumberValidator


class Valix:
    def string(self, error: str | None = None):
        return StringValidator(rules=[], error=error)

    def number(self, error: str | None = None):
        return NumberValidator(rules=[], error=error)

    def is_success[T](
        self, data: SafeParseResult[T]
    ) -> TypeGuard[SafeParseSuccessResult[T]]:
        return data.success is True

    def is_error[T](self, data: SafeParseResult[T]) -> TypeGuard[SafeParseErrorResult]:
        return data.success is False
