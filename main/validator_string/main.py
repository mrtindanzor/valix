from main.shared.errors import ValixError
from main.shared.types import SafeParseResult
from main.string_validator.main_rule import Rule, add_to_rules
from main.string_validator.parse import parse_rules
from main.string_validator.rules import (
    EndsWithRule,
    IncludesRule,
    LengthRule,
    LowerRule,
    MaxRule,
    MinRule,
    StartsWithRule,
    StringTypeRule,
    UpperRule,
)


class StringValidator:
    def __init__(self, rules: list[Rule] | None = None, error: str | None = None):
        self.rules: list[Rule] = add_to_rules(StringTypeRule(error), rules or [])

    def min(self, min_len: int, error: str | None = None):
        filtered_rules = add_to_rules(MinRule(min_len, error), self.rules)
        return StringValidator(filtered_rules)

    def max(self, max_len: int, error: str | None = None):
        filtered_rules = add_to_rules(MaxRule(max_len, error), self.rules)
        return StringValidator(filtered_rules)

    def length(self, length: int, error: str | None = None):
        filtered_rules = add_to_rules(LengthRule(length, error), self.rules)
        return StringValidator(filtered_rules)

    def startswith(self, word: str, error: str | None = None):
        filtered_rules = add_to_rules(StartsWithRule(word, error), self.rules)
        return StringValidator(filtered_rules)

    def endswith(self, word: str, error: str | None = None):
        filtered_rules = add_to_rules(EndsWithRule(word, error), self.rules)
        return StringValidator(filtered_rules)

    def includes(self, word: str, error: str | None = None):
        filtered_rules = add_to_rules(IncludesRule(word, error), self.rules)
        return StringValidator(filtered_rules)

    def lower(self):
        filtered_rules = add_to_rules(LowerRule(), self.rules)
        return StringValidator(filtered_rules)

    def upper(self):
        filtered_rules = add_to_rules(UpperRule(), self.rules)
        return StringValidator(filtered_rules)

    def safe_parse(self, data: object) -> SafeParseResult[str]:
        return parse_rules(data, self.rules)

    def parse(self, data: object) -> str:
        results = parse_rules(data, self.rules)
        if results.success is True:
            return results.data

        raise ValixError(results.error)
