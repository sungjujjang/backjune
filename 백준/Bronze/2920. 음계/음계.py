import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline().rstrip

a = list(map(int, input().split()))

if a[0] > a[1]:
    updown = -1 # -1 내려감 1 올라감
else:
    updown = 1

for i in range(1,8):
    if a[i] - a[i-1] != updown:
        print("mixed")
        break
    if i == 7:
        if updown == -1:
            print("descending")
        else:
            print("ascending")