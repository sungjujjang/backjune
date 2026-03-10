import sys
import math

mi, mx = map(int, sys.stdin.readline().split())
gili = mx - mi + 1
li = [False] * gili

for i in range(2, int(math.sqrt(mx)) + 1):
    square = i * i

    start = ((mi + square - 1) // square) * square

    for j in range(start, mx + 1, square):
        li[j - mi] = True
print(li.count(False))

