from math import sqrt

"""_____________________________________________________________________________________________________________________
Functions that convert from decimal, binary, octal and hexadecimal"""


# Decimal
def dec(num):  # Decimal to decimal¿¿??
    return num


def dec2(num):  # Decimal to binary
    num = int(num)
    return bin(num)[2:]


def dec8(num):  # Decimal to octal
    num = int(num)
    return oct(num)[2:]


def dec16(num):  # Decimal to hexadecimal
    num = int(num)
    return hex(num)[2:].upper()


# Binary
def bin_(num):  # Binary to decimal
    n = str(int(str(num), 2))
    return n


def bin8(num):  # Binary to octal
    n = int(str(num), 2)
    m = str(oct(n))
    return m[2:]


def bin16(num):  # Binary to hexadecimal
    n = int(str(num), 2)
    m = str(hex(n))
    return m[2:].upper()


# Octal
def oct_(num):  # Octal to decimal
    n = str(int(str(num), 8))
    return n


def oct2(num):  # Octal to binary
    n = int(str(num), 8)
    m = str(bin(n))
    return m[2:]


def oct16(num):  # Octal to hexadecimal
    n = int(str(num), 8)
    m = str(hex(n))
    return m[2:].upper()


# Hexadecimal
def hex_(num):  # Hexadecimal to decimal
    n = str(int(str(num), 16))
    return n


def hex2(num):  # Hexadecimal to binary
    n = int(str(num), 16)
    m = str(bin(n))
    return m[2:]


def hex8(num):  # Hexadecimal to octal
    n = int(str(num), 16)
    m = str(oct(n))
    return m[2:]
"""__________________________________________________________________________________________________________________"""

def square_root(num):
    num = "sqrt(" + str(num) + ")"
    try:
        result = eval(num)
        if result == int(result):
            shown = str(int(result))
        else:
            shown = str(round(result, 4))
    except:
        shown = "SyntaxError"
    return shown


def elevate_2_f(num):
    num = str(num) + "**2"
    try:
        result = eval(num)
        if result == int(result):
            shown = str(int(result))
        else:
            shown = str(round(result, 4))
    except:
        shown = "SyntaxError"
    return shown


def percentage_f(num):
    num = str(num) + "/100"
    try:
        result = eval(num)
        if result == int(result):
            shown = str(int(result))
        else:
            shown = str(round(result, 4))
    except:
        shown = "SyntaxError"
    return shown


def elevate_3_f(num):
    num = str(num) + "**3"
    try:
        result = eval(num)
        if result == int(result):
            shown = str(int(result))
        else:
            shown = str(round(result, 4))
    except:
        shown = "SyntaxError"
    return shown


def negate_f(num):
    try:
        num = str(num)
        if "mod" not in num:
            if "x" not in num:
                if "\u00F7" not in num:
                    if num[0] != "0":
                        if num[0] == "-":
                            num = num.replace("-", "")
                            shown = str(num)
                            return shown
                        elif num[0] != "-":
                            shown = "-" + str(num)
                            return shown
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    except:
        return num

def absolute_f(num):
    try:
        shown = str(abs(int(num)))
        return shown
    except:
        pass


def factorial_f(num):
    try:
        num = int(num)
        if num == 0 or num == 1:
            shown = 1
        elif num > 1:
            shown = num * factorial_f(num-1)
    except:
        shown = "SyntaxError"
    return shown

def calculate_f(calculation):
    if "m" in calculation and "o" in calculation and "d" in calculation:
        calculation = calculation.replace("o", "")
        calculation = calculation.replace("d", "")
        calculation = calculation.replace("m", "%")
    else:
        pass
    if "x" in calculation:
        calculation = calculation.replace('x', '*')
    else:
        pass
    if "\u00F7" in calculation:
        calculation = calculation.replace('\u00F7', '/')
    else:
        pass
    if "\u00B2" in calculation:
        calculation = calculation.replace('\u00B2', '**2')
    else:
        pass
    if "\u2212" in calculation:
        calculation = calculation.replace("\u2212", '-')
    else:
        pass
    if "^" in calculation:
        calculation = calculation.replace("^", '**')
    else:
        pass
    try:
        x = eval(calculation)
        if x == int(x):
            shown = str(int(x))
        else:
            if len(str(x)) > 8:
                if len(str(x)) > 12:
                    shown = str(round(x,12))
                else:
                    shown = str(round(x,5))
            else:
                if "e" in str(x):
                    x = str(x).replace("e", "x10^")
                if "+" in str(x):
                    x = str(x).replace("+", "")
                else:
                    shown = str(x)
    except ZeroDivisionError:
        shown = "Indeterminate value"
    except SyntaxError:
        shown = "SyntaxError"
    except NameError:
        shown = "SyntaxError"
    except ValueError:
        shown = "ValueError"
    return shown

"""__________________________________________________________________________________________________________________"""

def ml2l(value):
    x = str(float(value)/1000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x
def ml2m(value):
    x = str(float(value)/1000000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x
def l2ml(value):
    x = str(float(value)*1000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x
def l2m(value): #
    x = str(float(value)/1000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x
def m2ml(value):
    x = str(float(value)*1000000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x
def m2l(value):
    x = str(float(value)*1000)
    if x[(len(x)) - 2] == "." and x[(len(x)) - 1] == "0":
        x = x[:(len(x)) - 2]
    else:
        pass
    return x

"""__________________________________________________________________________________________________________________"""
def conversion_op(value, op1, op2):
    if op1==op2:
        return value
    else:
        value = int(value)
        if op1 == "Millimeters":
            value = value / 1000
        elif op1 == "Centimeters":
            value = value / 100
        elif op1 == "Kilometers":
            value = value * 1000
        elif op1 == "Inches":
            value = value / 39.37
        elif op1 == "Feet":
            value = value / 3.281
        else:
            pass
        if op2 == "Millimeters":
            result = value * 1000
        elif op2 == "Centimeters":
            result = value * 100
        elif op2 == "Kilometers":
            result = value / 100
        elif op2 == "Inches":
            result = value * 39.37
        elif op2 == "Feet":
            result = value * 3.281
        else:
            result = value
        return str(result)


