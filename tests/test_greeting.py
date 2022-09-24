import pytest

from unittest.mock import MagicMock, Mock
from sort_case_project.greeting import greet, greet2

@pytest.fixture
def greeting_string():
    return "Vadim", "Hi, Vadim"

# Dependency injection
def test_greet(greeting_string: Tuple(str, str)):
    name, expected_result = greeting_string
    returned_value: None = None
    
    # def mock_print(string):
    #     nonlocal returned_value
    #     returned_value: Unknown = string
    
    greet(name, mock_print)
    assert returned_value == "Hi, Vadmim!"
    
def test_greet2(greeting_string: Tuple(str, str)):
    name, expected_result = greeting_string
    mock_print: MagicMock = MagicMock()
    with patch("builtins.print", mock_print):
        greet2(name)
    mock_print.assert_called_once_with(expected_result)
    