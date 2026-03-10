import sys
sys.setrecursionlimit(10**6)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1, 1):
        if n % i == 0:
            return False
    return True
    
N = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())
i = 0
for num in nums:
    if is_prime(num):
        i += 1
print(i)