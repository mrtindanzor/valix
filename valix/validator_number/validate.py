from valix.shared.types import SafeParseErrorResult
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


class ValidateNumber:
    def type(
        self, data: object, rule: NumberTypeRule
    ) -> SafeParseErrorResult | int | float:
        if not isinstance(data, (int, float)):
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                rule_type = type(data)
                return SafeParseErrorResult(
                    error=f"Expected a number but received {rule_type}"
                )

        return data

    def min(self, data: int | float, rule: MinRule) -> SafeParseErrorResult | None:
        if data < rule.min:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number greater than or equal to {rule.min}"
                )

    def max(self, data: int | float, rule: MaxRule) -> SafeParseErrorResult | None:
        if data > rule.max:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number less than or equal to {rule.max}"
                )

    def gt(self, data: int | float, rule: GTRule) -> SafeParseErrorResult | None:
        if data <= rule.gt:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number greater than {rule.gt}"
                )

    def gte(self, data: int | float, rule: GTEqRule) -> SafeParseErrorResult | None:
        if data < rule.gte:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number greater than or equal to {rule.gte}"
                )

    def lt(self, data: int | float, rule: LTRule) -> SafeParseErrorResult | None:
        if data >= rule.lt:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number less than {rule.lt}"
                )

    def lte(self, data: int | float, rule: LTEqRule) -> SafeParseErrorResult | None:
        if data > rule.lte:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(
                    error=f"Expected a number less than or equal to {rule.lte}"
                )

    def positive(
        self, data: int | float, rule: PositiveRule
    ) -> SafeParseErrorResult | None:
        if data <= 0:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(error="Expected a positive number")

    def negative(
        self, data: int | float, rule: NegativeRule
    ) -> SafeParseErrorResult | None:
        if data > 0:
            if rule.error:
                return SafeParseErrorResult(error=rule.error_message)
            else:
                return SafeParseErrorResult(error="Expected a negative number")
