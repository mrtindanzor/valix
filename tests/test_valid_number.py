from valix import v 

def test_valid_number():
    num_validator = v.number()
    results = num_validator.safe_parse(5)
    assert results.success is True
    assert results.data == 5

def test_invalid_number(): 
    num_validator = v.number("Value must be a number")
    results = num_validator.safe_parse("a")
    assert results.success is False
    assert results.error == "Value must be a number"
    
def test_min_number():
    num_validator = v.number().min(5, "Value must be greater than or equal to 5")
    results = num_validator.safe_parse(2)
    assert results.success is False
    assert results.error == "Value must be greater than or equal to 5"

def test_max_number():
    num_validator = v.number().max(5, "Value must be less than or equal to 5")
    results = num_validator.safe_parse(7)
    assert results.success is False
    assert results.error == "Value must be less than or equal to 5"
 