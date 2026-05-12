from main.validator_number.rules import (
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

Rule = (
    NumberTypeRule
    | MinRule
    | MaxRule
    | GTRule
    | GTEqRule
    | LTRule
    | LTEqRule
    | PositiveRule
    | NegativeRule
)


def add_to_rules(current_rule: Rule, rules: list[Rule]):
    if any(isinstance(rule, type(current_rule)) for rule in rules):
        return rules

    return rules + [current_rule]
