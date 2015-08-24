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


def calctwos(instr):
    mant, exp = instr.split(" ")
    mant = bintodec(mant)

    sign, exp = exp[0], exp[1:]
    if sign == "1":
        exp = notstr(exp)

    exp = int(exp, 2)
    if sign == "1":
        exp = -exp

    return mant * Decimal(2)**exp


def minifloat(instr):
    sign, mant, exp = instr.split(" ")
    mant += "1."
    mant = bintodec(mant)
    exp = int(exp, 2)
    exp = exp - 15

    print("Sign: {}".format(sign))
    print("Mant: {}".format(mant))
    print("Exp: {}".format(exp))

    return mant * Decimal(2)**exp

print(calctwos("0101110010 000110"))
print(calctwos("1010101000 000100"))
print(calctwos("0110000000 111111"))
print(calctwos("1010000000 111101"))
