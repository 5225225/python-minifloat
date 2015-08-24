from decimal import Decimal


def notstr(instr):
    instr = instr.replace("1", "z")
    instr = instr.replace("0", "1")
    instr = instr.replace("z", "0")
    return instr


def bintodec(floatnum):
    x = Decimal("0")
    floatnum = floatnum.replace(".", "")
    sign, floatnum = floatnum[0], floatnum[1:]
    if sign == "1":
        floatnum = notstr(floatnum)

    # This code assumes that there is only one digit before the decimal point.
    for index, item in enumerate(floatnum):
        if item == "1":
            x += Decimal("2")/2**(index+1)
    if sign == "1":
        x = -x
    return x


def minifloat(inputstr):
    sign, exp, mant = inputstr.split(" ")
    sign = bool(sign)
    exp = int(exp, 2) - Decimal(15)
    mant = bintodec(mant)

    return mant * Decimal(2)**exp


print(minifloat("0 01111 0000000000"))
