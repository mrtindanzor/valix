# pyrefly: ignore [missing-import]

from valix.shared.errors import ValixError
from valix.shared.types import SafeParseResult
from valix.validator_number.main_rule import Rule, add_to_rules
from valix.validator_number.parse import parse_number_rules
from valix.validator_number.rules import (
    GTEqRule,
    GTRule,
    LTEqRule,
    LTRule,
    MaxRule,
    MinRule,
    NegativeRule,
    NumberTypeRule,
    PositiveRule,
)


class NumberValidator:
    def __init__(self, rules: list[Rule], error: str | None = None):
        self.rules = add_to_rules(NumberTypeRule(error=error), rules=rules)

    def min(self, min: int | float, error: str | None = None):
        filter_rules = add_to_rules(MinRule(min=min, error=error), self.rules)
        return NumberValidator(filter_rules)

    def max(self, max: int | float, error: str | None = None):
        filter_rules = add_to_rules(MaxRule(max=max, error=error), self.rules)
        return NumberValidator(filter_rules)

    def gt(self, gt: int | float, error: str | None = None):
        filter_rules = add_to_rules(GTRule(gt=gt, error=error), self.rules)
        return NumberValidator(filter_rules)

    def gte(self, gte: int | float, error: str | None = None):
        filter_rules = add_to_rules(GTEqRule(gte=gte, error=error), self.rules)
        return NumberValidator(filter_rules)

    def lt(self, lt: int | float, error: str | None = None):
        filter_rules = add_to_rules(LTRule(lt=lt, error=error), self.rules)
        return NumberValidator(filter_rules)

    def lte(self, lte: int | float, error: str | None = None):
        filter_rules = add_to_rules(LTEqRule(lte=lte, error=error), self.rules)
        return NumberValidator(filter_rules)

    def positive(self, error: str | None = None):
        filter_rules = add_to_rules(PositiveRule(error=error), self.rules)
        return NumberValidator(filter_rules)

    def negative(self, error: str | None = None):
        filter_rules = add_to_rules(NegativeRule(error=error), self.rules)
        return NumberValidator(filter_rules)

    def safe_parse(self, data: object) -> SafeParseResult[int | float]:
        return parse_number_rules(data, self.rules)

    def parse(self, data: object) -> int | float:
        result = self.safe_parse(data)
        if result.success is True:
            return result.data

        raise ValixError(result.error)
