import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline().rstrip

alpha = "abcdefghijklmnopqrstuvwxyz"

st = input()
for c in alpha:
    print(st.find(c), end=" ")