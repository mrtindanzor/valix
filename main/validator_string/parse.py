from typing import cast

from main.shared.types import (
    SafeParseErrorResult,
    SafeParseResult,
    SafeParseSuccessResult,
)
from main.string_validator.main_rule import Rule
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
from main.string_validator.validate import ValidateString


def parse_rules(input_data: object, rules: list[Rule]) -> SafeParseResult[str]:
    validate = ValidateString()
    string_rule = cast(StringTypeRule, rules[0])

    type_results = validate.type(input_data, string_rule)
    if not isinstance(type_results, str):
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

            case LengthRule():
                error_results = validate.length(data, rule)

            case StartsWithRule():
                error_results = validate.startswith(data, rule)

            case EndsWithRule():
                error_results = validate.endswith(data, rule)

            case IncludesRule():
                error_results = validate.includes(data, rule)

            case LowerRule():
                data = validate.lower(data)

            case UpperRule():
                data = validate.upper(data)

    return SafeParseSuccessResult(data) if not error_results else error_results
