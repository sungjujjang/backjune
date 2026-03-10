import sys
input = sys.stdin.readline

n = int(input())
rms = 1
i = 1


while True:
    if n <= rms:
        break
    rms += 6 * i
    i += 1
    # print(rms, i)
    
print(i)