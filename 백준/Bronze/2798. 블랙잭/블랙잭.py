import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

li = []

for on in A:
    for tw in A:
        if on == tw:
            continue
        for th in A:
            if tw == th or th == on:
                continue
            li.append(on+tw+th)

MX = 0
for i in li:
    if i > M:
        continue
    if M - i < M - MX:
        MX = i

print(MX)