from dataclasses import dataclass
from typing import Literal, TypedDict, TypeVar, Union


class Options(TypedDict):
    error: str


Rule = tuple[str, int | str, Options]


@dataclass
class SafeParseErrorResult:
    error: str
    success: Literal[False] = False


T = TypeVar("T")


@dataclass
class SafeParseSuccessResult[T]:
    data: T
    success: Literal[True] = True


SafeParseResult = Union[SafeParseErrorResult, SafeParseSuccessResult[T]]
