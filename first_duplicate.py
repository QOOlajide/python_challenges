def first_duplicate(s):
    """
    Function to return the first duplicate character in a given string.
    
    Thought Process:
    - We're trying to find the first character that appears more than once.
    - This means we need to keep track of characters we've already seen.
    - A dictionary is ideal for this because it allows for fast O(1) lookup.
    
    Edge Cases Considered:
    - If the input is an empty string: there are no duplicates ➝ return None.
    - If the input is one character long: duplicates are not possible ➝ return None.
    - Case sensitivity matters ('A' and 'a' are treated as different).
    - Supports any type of character, including symbols and numbers.
    """
    
    # Step 1: Handle the edge case of an empty string or single character
    if len(s) < 2:
        return None

    # Step 2: Initialize an empty dictionary to track seen characters
    seen = {}

    # Step 3: Iterate through each character in the string
    for char in s:
        # If we've seen it before, return it as the first duplicate
        if char in seen:
            return char
        # Otherwise, mark it as seen
        seen[char] = True

    # Step 4: If we never find a duplicate, return None
    return None


# Optional test cases (commented out for documentation-style submission)
# print(first_duplicate("abcdefa"))  # ➝ 'a'
# print(first_duplicate(""))         # ➝ None
# print(first_duplicate("a"))        # ➝ None
# print(first_duplicate("abA"))      # ➝ None (case-sensitive)
# print(first_duplicate("abcb"))     # ➝ 'b'
