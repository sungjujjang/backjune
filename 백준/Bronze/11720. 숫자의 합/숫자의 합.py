import sys
input = sys.stdin.readline

N = int(input())
num = str(input())

total = 0
for i in range(0, N):
    total += int(num[i])

print(total)