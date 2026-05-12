from valix import v 


def test_valid_string():
    string_validator = v.string()
    results = string_validator.safe_parse("hello")
    assert results.success is True
    assert results.data == "hello"

def test_invalid_string():
    string_validator = v.string("Value must be a string")
    results = string_validator.safe_parse(123)
    assert results.success is False
    assert results.error == "Value must be a string"
    
def test_min_string():
    string_validator = v.string().min(5, "Value must be at least 5 characters long")
    results = string_validator.safe_parse("hello")
    assert results.success is True
    assert results.data == "hello"
    
def test_max_string():
    string_validator = v.string().max(5, "Value must be at most 5 characters long")
    results = string_validator.safe_parse("hello")
    assert results.success is True
    assert results.data == "hello"
    
def test_length_string():
    string_validator = v.string().length(5, "Value must be exactly 5 characters long")
    results = string_validator.safe_parse("hello")
    assert results.success is True
    assert results.data == "hello"
    
def test_startswith_string():
    string_validator = v.string().startswith("hello", "Value must start with 'hello'")
    results = string_validator.safe_parse("hello world")
    assert results.success is True
    assert results.data == "hello world"
    
def test_endswith_string():
    string_validator = v.string().endswith("world", "Value must end with 'world'")
    results = string_validator.safe_parse("hello world")
    assert results.success is True
    assert results.data == "hello world"
    
def test_includes_string():
    string_validator = v.string().includes("world", "Value must include 'world'")
    results = string_validator.safe_parse("hello world")
    assert results.success is True
    assert results.data == "hello world"
    
def test_lower_string():
    string_validator = v.string().lower()
    results = string_validator.safe_parse("HELLO WORLD")
    assert results.success is True
    assert results.data == "hello world"
    
def test_upper_string():
    string_validator = v.string().upper()
    results = string_validator.safe_parse("hello world")
    assert results.success is True
    assert results.data == "HELLO WORLD"
