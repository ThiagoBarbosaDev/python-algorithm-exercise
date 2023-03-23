def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    for index, character in enumerate(word):
        if character != word[-index - 1]:
            return False
    return True
