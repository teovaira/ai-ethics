"""
Exercise 00 - Part B: Palindrome Checker
Implementation following Track B approach - attempt first, then improve with AI feedback.
"""

def is_palindrome(s):
    """
    Check if a string is a palindrome (simple version - letters only).

    Args:
        s (str): The string to check

    Returns:
        bool: True if palindrome, False otherwise
    """
    # Use two pointers, one from start and one from end
    left = 0
    right = len(s) - 1

    # Keep comparing characters moving towards middle
    while left < right:
        # If any characters don't match, not a palindrome
        if s[left] != s[right]:
            return False
        # Move pointers closer to middle
        left += 1
        right -= 1

    # If we reached here, all characters matched
    return True


def is_palindrome_advanced(s):
    """
    Check if a string is a palindrome with all variations integrated:
    - Case-insensitive
    - Ignores spaces
    - Ignores punctuation

    Args:
        s (str): The string to check

    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove all non-alphanumeric characters and make lowercase
    cleaned = ""
    for char in s.lower():
        if char.isalnum():
            cleaned += char

    # Use two pointers, one from start and one from end
    left = 0
    right = len(cleaned) - 1

    # Keep comparing characters moving towards middle
    while left < right:
        # If any characters don't match, not a palindrome
        if cleaned[left] != cleaned[right]:
            return False
        # Move pointers closer to middle
        left += 1
        right -= 1

    # If we reached here, all characters matched
    return True
