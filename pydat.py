"""
This is test code for my linter
"""

def ex(a):
    print(a)

def ex1(a,b):
    if ex(a,b):
        return True
    return False

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

def two1(val):
    """
    基本
    まず二つの条件が結合できるか
    """
    if val < 10:
        if val > 0:
            return 0
    return 1
def two2(val):
    """
    任意個数結合できるか
    """
    if val < 10:
        if val > 0:
            if val == 1:
                return 0
    return 1
def two3(val):
    """
    elifの場合は正しく修正できるか
    """
    if val < 10:
        pass
    elif val < 15:
        if val < 30:
            return 2
    return 1
def two_dummy1(val):
    """
    if以外の異物が入っていた場合正しく弾けるか
    """
    if val < 10:
        if val == 1:
            return 0
        print(2)
    return 1

def two_dummy2(val):
    """
    入れ子内のifがelseを持っていた場合正しく弾けるか
    """
    if val < 10:
        if val == 1:
            return 0
        else:
            print()
            return 5
    return 1

def two4(val):
    """
    二つの入れ子の３つ目のifがelseを持っていた場合上の二つだけを結合できるか
    """
    if val < 10:
        if val > 0:
            if val == 1:
                return 0
            else:
                print()

def two5(val):
    """
    elif内でifの入れ子がある場合正しくelifではなくifで修正できるか
    """
    if val < 10:
        print()
    elif val < 15:
        print()
        if val < 30:
            if val == 31:
                return 2
    return 1
def two6(val):
    """
    長い条件文を改行できるか
    """
    if val < 10:
        if val < 15:
            if val < 30:
                if val == 31:
                    if isinstance(val, float):
                        if isinstance(val, int):
                            if isinstance(val, str):
                                return 2
    return 1

def one(val,val2):
    """
    1. For exclusive cases, writing a series of if statements rather than using else if.
    """
    if val == 11:
        print("2")
    if val < 13 and val >= 10 and val != 11:
        print("1")
    if val != 11 and val < 15 and val >= 10 and val >= 13:
        print(3)
    return 0
def elif_ex(val):
    if val == 1:
        pass
    elif val == 2:
        pass
    elif val == 3:
        pass
    else:
        pass
def one_another(var):
    """
    docstring
    """
    if var == 1 or var == 2:
        print(1)
    if not (var == 1 or var == 2) and var == 3:
        print(2)
