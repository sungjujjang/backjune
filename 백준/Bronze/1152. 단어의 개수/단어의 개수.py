import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline().rstrip

alpha = "abcdefghijklmnopqrstuvwxyz"

st = input()
print(len(st.strip().split()))