from dataclasses import dataclass


@dataclass
class ValixError(Exception):
    error: str
