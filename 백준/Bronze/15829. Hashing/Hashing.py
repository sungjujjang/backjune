import sys
input = sys.stdin.readline

def getint(c):
	return ord(c)-96

l = int(input())
c = input()

total = 0
for i in range(0, l):
	total += getint(c[i]) * (31 ** i)

print(total % 1234567891)