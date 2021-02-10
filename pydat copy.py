"""
This is test code for my linter
"""

def six(string):
    if string.isdigit():
        return True
    return False

def five(pattern_five):
    if pattern_five == 0:
        return True
    return False

def two(val):
    if val < 10:
        if val > 0:
            return 0
    return 1
def one(val,val2):
    if val == 11:
        print("2")
    if val < 13 and val >= 10 and val != 11:
        print("1")
    if val != 11 and val < 15 and val >= 10 and val >= 13:
        print(3)
    return 0