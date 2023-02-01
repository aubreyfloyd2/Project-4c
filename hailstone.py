# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 1/31/2023
# Description: Function that takes a positive integer parameter as the initial number of a
#              hailstone sequence and returns how many steps it takes to reach 1.

def hailstone(x):
    """Returns how many steps it takes to reach 1 from initial integer"""
    count = 0
    while x > 1:
        count += 1
        if x % 2 == 1:
            x = int(x * 3 + 1)
        else:
            x = int(x // 2)
    return count

# print(hailstone(1000))