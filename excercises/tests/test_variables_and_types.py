from exercises.variables_and_types import describe_variable

def test_describe_variable_int():
    result = describe_variable(10)
    assert "int" in result
    assert "10" in result
