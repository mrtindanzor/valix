from typing import TypeVar

from main.shared.types import SafeParseErrorResult
from main.string_validator.rules import (
    EndsWithRule,
    IncludesRule,
    LengthRule,
    MaxRule,
    MinRule,
    StartsWithRule,
    StringTypeRule,
)

T = TypeVar("T")


class ValidateString:
    def type[T](self, data: object, rule: StringTypeRule):
        if not isinstance(data, str):
            print(rule)
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)

            rule_type = type(data)
            return SafeParseErrorResult(
                error=f'Expected string but received "{rule_type}"'
            )

        return data

    def min(self, data: str, rule: MinRule):
        if len(data) < rule.min_len:
            return SafeParseErrorResult(error=rule.error_message)

    def max(self, data: str, rule: MaxRule):
        if len(data) > rule.max_len:
            return SafeParseErrorResult(error=rule.error_message)

    def length(self, data: str, rule: LengthRule):
        if not len(data) == rule.length:
            return SafeParseErrorResult(error=rule.error_message)

    def startswith(self, data: str, rule: StartsWithRule):
        print(data, rule.word, data.startswith(rule.word))
        if not data.startswith(rule.word):
            return SafeParseErrorResult(error=rule.error_message)

    def endswith(self, data: str, rule: EndsWithRule):
        if not data.endswith(rule.word):
            return SafeParseErrorResult(error=rule.error_message)

    def includes(self, data: str, rule: IncludesRule):
        if data.find(rule.word) == -1:
            return SafeParseErrorResult(error=rule.error_message)

    def lower(self, data: str):
        return data.lower()

    def upper(self, data: str):
        return data.upper()
