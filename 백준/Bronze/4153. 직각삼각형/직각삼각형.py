import sys
input = sys.stdin.readline

while True:
    l = list(map(int, input().split()))
    a, b, c = sorted(l)
    if a + b + c == 0:
        break
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")
