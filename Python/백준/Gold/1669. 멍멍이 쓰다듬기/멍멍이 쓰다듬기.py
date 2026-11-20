
import sys
import math

X, Y = map(int, sys.stdin.readline().split())
D = Y - X

if D == 0:
    print(0)
else:
    n = math.isqrt(D)

    if D == n * n:
        print(2 * n - 1)
    elif D <= n * (n + 1):
        print(2 * n)
    else:
        print(2 * n + 1)
