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
    if string.isdigit():
        return True
    return False  

def five(pattern_five):
    if pattern_five == 0:
        return True
    return False  

def five_another(pattern_five_another):
    if pattern_five_another == 0:
        return True
    else:
        return False 

def five_dummy(pattern_five_dummy):
    if pattern_five_dummy == 0:
        return True
    return "False" 

def five_dummy2(pattern_five_dummy2):
    if pattern_five_dummy2 == 0:
        return 1
    return 0  

def two(val):
    """
    2. Conjoining conditions using nested if statements rather than the "and" operator.
    """
    if val < 10:
        if val > 0:
            return 0
    return 1
def two2(val):
    """
    2. Conjoining conditions using nested if statements rather than the "and" operator.
    """
    if val < 10:
        if val > 0:
            if val == 1:
                return 0
    return 1
def two_dummy(val):
    """
    2. Conjoining conditions using nested if statements rather than the "and" operator.
    """
    if val < 10:
        if val > 0:
            if val == 1:
                return 0
        print(2)
    return 1

def two_dummy1(val):
    """
    2. Conjoining conditions using nested if statements rather than the "and" operator.
    """
    if val < 10:
        print()
        if val > 0:
            if val == 1:
                return 0
    elif val < 15:
        if val < 30:
            return 2
    return 1
print(type(True) is bool)
