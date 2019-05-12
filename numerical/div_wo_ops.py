"""
This question was asked by ContextLogic.
Implement division of two positive integers without using
the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""


def div(a, b):
    """ Returns equivalent of a // b. O(a)
        int a > 0
        int b > 0. """
    div = 0
    while a >= b:
        a -= b
        div += 1
    return div


def div_bitwise(a, b):
    """ Returns equivalent of a // b. O(log(a))
        int a > 0
        int b > 0. """
    quotient = 0
    temp = 0
    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (b << i) <= a):
            temp += b << i
            quotient |= 1 << i
    return quotient


if __name__ == "__main__":
    print(div(200001, 40))
    print(div_bitwise(200001, 40))
