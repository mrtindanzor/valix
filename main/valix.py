from main.shared.types import Options, SafeParseResult, SafeParseSuccessResult, SafeParseErrorResult
from main.string_validator.main import StringValidator 
from typing import TypeGuard

class Valix:
    def string(self, options: Options | None = None):
        return StringValidator(options=options) 
    
    def is_success[T](self, data: SafeParseResult[T]) -> TypeGuard[SafeParseSuccessResult[T]]:
        return data['success'] is True
    
    def is_error[T](self, data: SafeParseResult[T]) -> TypeGuard[SafeParseErrorResult]:
        return data['success'] is False
