import sys

input = sys.stdin.readline

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n

A = input()
B = input()
C = input()

LI = [A, B, C]

nexts = 0
for i in LI:
    if nexts != 0:
        nexts += 1
        continue
    i = i.replace("\n", "")
    if i.isdigit():
        nexts = int(i) + 1

print(fb(nexts))