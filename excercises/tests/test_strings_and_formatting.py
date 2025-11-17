from exercises.strings_and_formatting import greet_user, uppercase, count_characters

def test_greet_user():
    assert "Alice" in greet_user("Alice")

def test_uppercase():
    assert uppercase("python") == "PYTHON"

def test_count_characters():
    assert count_characters("test") == 4
