def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():       # opening brackets
            stack.append(char)
        elif char in mapping:              # closing brackets
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack  # True if stack is empty (all brackets matched)
