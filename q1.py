from math import ceil
from rich.console import Console

c = Console()

"""
down pat:

A pat is a single letter or a string of letters which can be split into a left and right string (of at least 1 letter)
where: each is the reverse of a pat; and all the letters in the left string are later in the alphabet than all the
letters in the right string.

letters have to split

"""

#test change


def test(v1, v2):
    assert(v1) == v2, "Values should equal"


def alpha_values(left, right):
    left_min = min([ord(v.lower()) for v in left])

    for num in [ord(v.lower()) for v in right]:
        if left_min < num or left_min == num:
            return False

    return True
    #return min([ord(v.lower()) for v in left]) > ([ord(v.lower()) for v in right])


def down_pat(in_str: str):
    c.print(f"in_str: {in_str}")

    left = in_str[:ceil(len(in_str) / 2)]
    right = in_str[ceil(len(in_str) / 2):]

    if len(in_str) == 2 and alpha_values(left, right):
        return True

    if len(in_str) == 1:
        c.print(f"len 1, in_str: {in_str}")
        return True

    c.print(f"left: {left}\nright: {right}\nalpha: {alpha_values(left, right)}")

    if alpha_values(left, right) and not ((down_pat(left[::-1]) or down_pat(right[::-1]))):
        return True

    return False

c.clear()


while True:

    s1, s2 = input().strip().split(" ")
    c.clear()
    c.print("YES" if down_pat(s1) is True else "NO")
    input()
    c.print("YES" if down_pat(s2) is True else "NO")
    input()
    c.print("YES" if down_pat(s1 + s2) is True else "NO")
    print()

    print()
