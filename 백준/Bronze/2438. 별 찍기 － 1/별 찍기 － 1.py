import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    for j in range(0, i):
        print("*", end="")
    print()