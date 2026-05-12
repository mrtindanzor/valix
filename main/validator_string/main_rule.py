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

Rule = (
    StringTypeRule
    | MaxRule
    | MinRule
    | LengthRule
    | StartsWithRule
    | EndsWithRule
    | IncludesRule
    | LowerRule
    | UpperRule
)


def add_to_rules(current_rule: Rule, rules: list[Rule]):
    if any(isinstance(rule, type(current_rule)) for rule in rules):
        return rules

    return rules + [current_rule]
