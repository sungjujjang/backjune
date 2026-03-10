import sys
sys.setrecursionlimit(10**6)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

n, r = map(int, sys.stdin.readline().split())
print(int(fact(n)/(fact(r)*fact(n - r))))