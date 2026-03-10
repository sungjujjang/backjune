import sys
input = sys.stdin.readline

def hap(n):
    total = 0
    st = str(n)
    for c in st:
        total += int(c)
    return total

n = int(input())

maker = 0
for i in range(0, n):
    if i + hap(i) == n:
        maker = i
        break

print(maker)