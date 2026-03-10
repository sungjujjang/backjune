import sys
input = sys.stdin.readline

n = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

total = 0

for i in range(0,6):
    total += sizes[i] // T
    if sizes[i] % T != 0:
        total += 1
    
print(total)
print(n//P, n%P)