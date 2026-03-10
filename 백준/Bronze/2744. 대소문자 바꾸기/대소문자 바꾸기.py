import sys

input = sys.stdin.readline
n = str(input())

rst = ""
for s in n:
    if s.islower():
        rst += s.upper()
    else:
        rst += s.lower()

print(rst)