import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
pan = []
min_paint = 64
 
for _ in range(N):
    pan.append(input())

for i in range(N-7):
    for j in range(M-7):
        w = 0
        bl = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if pan[a][b] != 'B':
                        w += 1
                    if pan[a][b] != 'W':
                        bl += 1
                else:
                    if pan[a][b] != 'W':
                        w += 1
                    if pan[a][b] != 'B':
                        bl += 1
 
        if min_paint > w:
            min_paint = w
        if min_paint > bl:
            min_paint = bl
 
print(min_paint)