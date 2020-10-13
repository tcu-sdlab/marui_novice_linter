"""
This is test code for my linter
"""
# def ex(a,b):
#     if "a".isdigit:
#         return True
#     return False

# def ex1(a,b):
#     if ex(a,b):
#         return True
#     return False

def six(string):
    """
    6. The previous pattern for conditions with method calls instead of operators.
    """
    if string.isdigit():
        return True
    return False  # Unnecessary "else" after "return" (no-else-return)

def five(pattern_five):
    """
    5.  Returning a boolean value by checking a condition
        with an operator (e.g., ==, >, <) by using an if statement
        and explicitly returning true or false rather than simply returning the condition.
    """
    if pattern_five == 0:
        return True
    return False  # Unnecessary "else" after "return" (no-else-return)

def five_another(pattern_five_another):
    """
    5.  Returning a boolean value by checking a condition
        with an operator (e.g., ==, >, <) by using an if statement
        and explicitly returning true or false rather than simply returning the condition.
    """
    if pattern_five_another == 0:
        return True
    else:
        return False  # Unnecessary "else" after "return" (no-else-return)

def five_dummy(pattern_five_dummy):
    """
    5.  Returning a boolean value by checking a condition
        with an operator (e.g., ==, >, <) by using an if statement
        and explicitly returning true or false rather than simply returning the condition.
    """
    if pattern_five_dummy == 0:
        return True
    return "False"  # Unnecessary "else" after "return" (no-else-return)
