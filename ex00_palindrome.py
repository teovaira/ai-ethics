"""
Exercise 00 - Part B: Palindrome Checker
This file contains the palindrome implementation following Track B approach.
The Right Way: Attempt independently first, then use AI strategically.
"""

# TODO: Implement your basic palindrome checker here
# Remember: Try this yourself BEFORE asking AI!
#
# Steps to follow:
# 1. Write pseudocode first (in ex00_ai_ethics_coder.md)
# 2. Implement your solution here
# 3. Test with multiple cases
# 4. Debug any issues yourself
# 5. Add comments explaining your logic
# 6. ONLY THEN ask AI to review and suggest improvements

def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): The string to check

    Returns:
        bool: True if palindrome, False otherwise

    TODO: Implement this function yourself first!
    Example approach:
    - Handle empty strings
    - Convert to same case
    - Compare characters from both ends moving inward
    """
    pass


# TODO: Part C Variation 1 - Ignore spaces and punctuation
def is_palindrome_ignore_punctuation(s):
    """
    Check if a string is a palindrome, ignoring spaces and punctuation.

    Args:
        s (str): The string to check

    Returns:
        bool: True if palindrome, False otherwise

    TODO: Implement this variation yourself!
    Hint: You might need to filter out non-alphanumeric characters
    """
    pass


# TODO: Part C Variation 2 - Case-insensitive
def is_palindrome_case_insensitive(s):
    """
    Check if a string is a palindrome, ignoring case.

    Args:
        s (str): The string to check

    Returns:
        bool: True if palindrome, False otherwise

    TODO: Implement this variation yourself!
    Example: "Racecar" should return True
    """
    pass


# TODO: Part C Variation 3 - Return position where palindrome fails
def palindrome_fail_position(s):
    """
    If string is not a palindrome, return the position where it fails.
    If it is a palindrome, return -1.

    Args:
        s (str): The string to check

    Returns:
        int: Position where palindrome check fails, or -1 if it's a palindrome

    TODO: Implement this variation yourself!
    Example: "racecxr" should return 4 (where 'x' doesn't match)
    """
    pass


# Test cases - Add your own test cases here!
if __name__ == "__main__":
    # TODO: Write test cases to verify your implementations
    # Example structure:

    print("Testing basic palindrome checker:")
    # test_cases = [
    #     ("racecar", True),
    #     ("hello", False),
    #     ("A man a plan a canal Panama", True),  # This might fail in basic version
    #     ("", True),  # Edge case - is empty string a palindrome?
    # ]

    # for text, expected in test_cases:
    #     result = is_palindrome(text)
    #     status = "✓" if result == expected else "✗"
    #     print(f"{status} is_palindrome('{text}') = {result} (expected {expected})")

    print("\nTODO: Add your test cases here!")
    print("Remember: Write tests, run them, fix bugs, understand why it works.")
    print("This is how you learn - not by copying working code!")
