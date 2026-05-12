from dataclasses import dataclass, field


@dataclass
class StringTypeRule:
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = "Expected a string"


@dataclass
class MaxRule:
    max_len: int
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Must be at most {self.max_len} characters"


@dataclass
class MinRule:
    min_len: int
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Must be at least {self.min_len} characters."


@dataclass
class LengthRule:
    length: int
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Must be {self.length} characters."


@dataclass
class StartsWithRule:
    word: str
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f'Must start with "{self.word}".'


@dataclass
class EndsWithRule:
    word: str
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f'Must end with "{self.word}".'


@dataclass
class IncludesRule:
    word: str
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f'Must include "{self.word}".'


@dataclass
class LowerRule:
    kind = "lower"


@dataclass
class UpperRule:
    kind = "upper"
