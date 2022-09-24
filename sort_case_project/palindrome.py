def is_palindrome(string: str):
    if not isinstance(string, str):
        raise ValueError("'string' must be an instance of 'str'")
            
    characters: list[str] = list(string)
    characters.reverse()
    reversed_string: str = "".join(characters)
    return string == reversed_string