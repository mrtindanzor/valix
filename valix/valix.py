from typing import TypeGuard
from valix.shared.types import (
    SafeParseErrorResult,
    SafeParseResult,
    SafeParseSuccessResult,
) 
from valix.validator_string.main import StringValidator
from valix.validator_number.main import NumberValidator


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
