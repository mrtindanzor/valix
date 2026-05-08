from main.shared.types import (
    Options,
    SafeParseErrorResult,
    SafeParseSuccessResult,
    SafeParseResult,
    Rule,
)
from main.string_validator.utils.options_builder import options_builder
from main.string_validator.utils.parse import ValidateString


class StringValidator:
    def __init__(self, rules: list[Rule] | None = None, options: Options | None = None):
        error = "Expected type string"
        new_options = options_builder(options, error)
        self.rules: list[Rule] = rules or [("type", "string", new_options)]

    def min(self, min_len: int, options: Options | None = None):
        error = f"Must be at least {min_len} characters"
        new_options = options_builder(options, error)

        return StringValidator(self.rules + [("min", min_len, new_options)])

    def max(self, max_len: int, options: Options | None = None):
        error = f"Must be at most {max_len} characters"
        new_options = options_builder(options, error)

        return StringValidator(self.rules + [("max", max_len, new_options)])

    def safe_parse(
        self, data: object
    ) -> SafeParseResult[str]:
        rules = self.rules
        validator = ValidateString()

        operator, _v, options = rules[0]
        textResult = validator.variable(data, options.get("error"))

        if not isinstance(textResult, str):
            return textResult

        text = textResult

        result: SafeParseErrorResult | None = None

        for operator, value, options in rules[1:]:
            if result:
                break

            error = options.get("error")
            match operator:
                case "min":
                    if isinstance(value, int):
                        print(error)
                        result = validator.min(text, value, error)

                case "max":
                    if isinstance(value, int):
                        print(error)
                        result = validator.max(text, value, error)
                case _:
                    pass
                
        if result:
            return result

        return SafeParseSuccessResult(success=True, data=text)
