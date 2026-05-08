from typing import Literal, TypedDict, TypeVar, Union


class Options(TypedDict):
    error: str


Rule = tuple[str, int | str, Options]


class SafeParseErrorResult(TypedDict):
    success: Literal[False]
    error: str


T = TypeVar("T")


class SafeParseSuccessResult[T](TypedDict):
    success: Literal[True]
    data: T

SafeParseResult  = Union[
    SafeParseErrorResult,
    SafeParseSuccessResult[T]
]