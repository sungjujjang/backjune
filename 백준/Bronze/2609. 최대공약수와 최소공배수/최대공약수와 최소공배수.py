import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

g = gcd(a, b)

print(g)
print(int((a*b)/g))