def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if high_index < 0:
        return True
    if word[low_index] != word[high_index]:
        return False
    if low_index == high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
