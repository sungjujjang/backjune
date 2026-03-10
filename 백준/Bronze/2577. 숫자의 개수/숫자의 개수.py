import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

tc = str(a*b*c)
apa = "0123456789"

for c in apa:
    print(tc.count(c))
