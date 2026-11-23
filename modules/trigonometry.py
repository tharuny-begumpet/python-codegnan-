import math

def sin1(angle, unit="degrees"):
    if unit.lower() == "degrees":
        angle = math.radians(angle)
    return math.sin(angle)


def cos1(angle, unit="degrees"):
    if unit.lower() == "degrees":
        angle = math.radians(angle)
    return math.cos(angle)


def tan1(angle, unit="degrees"):
    if unit.lower() == "degrees":
        angle = math.radians(angle)
    return math.tan(angle)