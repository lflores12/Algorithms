#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# 1 cookie

# 1

# 1 way

# 2 cookies

# 1,1
# 2

# 2 ways

# 3 cookies

# 1,1,1,
# 1,2
# 2,1
# 3

# 4 ways


# 4 cookies

# 1,1,1,1,
# 1,1,2
# 1,2,1
# 2,1,1
# 2,2
# 3,1
# 1,3

# 7 ways

# 5 cookies

# 1,1,1,1,1
# 1,1,1,2
# 1,1,2,1
# 1,2,1,1
# 2,1,1,1
# 2,2,1
# 2,1,2
# 1,2,2
# 3,1,1
# 1,3,1
# 1,1,3
# 3,2
# 2,3


[1, 1, 2, 4, 7, 13, 24, 44]


def eating_cookies(n, cache=None):
    if not cache:
        cache = [0] * (n+1)
    if cache[n] != 0:
        return cache[n]
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
