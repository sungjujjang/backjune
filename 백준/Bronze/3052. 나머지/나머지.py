import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

li = set()

for i in range(0,10):
    li.add(int(input()) % 42)
    
print(len(li))