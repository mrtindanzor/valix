 
from dataclasses import dataclass, field

@dataclass
class NumberTypeRule:
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = "Expected a number"

@dataclass
class MinRule:
    min: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number greater than {self.min}"

@dataclass
class MaxRule:
    max: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number less than {self.max}"

@dataclass
class GTRule:
    gt: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number greater than {self.gt}"

@dataclass
class GTEqRule:
    gte: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number greater than or equal to {self.gte}"

@dataclass
class LTEqRule:
    lte: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number less than or equal to {self.lte}"

@dataclass
class LTRule:
    lt: int | float
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a number less than {self.lt}"

@dataclass
class PositiveRule:
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a positive number"

@dataclass
class NegativeRule:
    error: str | None = None
    error_message: str = field(init=False)

    def __post_init__(self):
        if self.error:
            self.error_message = self.error
        else:
            self.error_message = f"Expected a negative number"

