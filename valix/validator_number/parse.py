from typing import cast

from valix.shared.types import (
    SafeParseErrorResult,
    SafeParseResult,
    SafeParseSuccessResult,
)
from valix.validator_number.main_rule import Rule
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
from valix.validator_number.validate import ValidateNumber


def parse_number_rules(data: object, rules: list[Rule]) -> SafeParseResult[int | float]:
    validate = ValidateNumber()
    number_rule = cast(NumberTypeRule, rules[0])
    type_results = validate.type(data, number_rule)
    if isinstance(type_results, SafeParseErrorResult):
        return type_results

    data = type_results
    error_results: SafeParseErrorResult | None = None

    for rule in rules[1:]:
        if error_results:
            return error_results

        match rule:
            case MinRule():
                error_results = validate.min(data, rule)

            case MaxRule():
                error_results = validate.max(data, rule)

            case GTRule():
                error_results = validate.gt(data, rule)

            case GTEqRule():
                error_results = validate.gte(data, rule)

            case LTRule():
                error_results = validate.lt(data, rule)

            case LTEqRule():
                error_results = validate.lte(data, rule)

            case PositiveRule():
                error_results = validate.positive(data, rule)

            case NegativeRule():
                error_results = validate.negative(data, rule)

    return SafeParseSuccessResult(data) if not error_results else error_results
