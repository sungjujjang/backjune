n = int(input())
result = 0

sero = [0] * n
left_d = [0] * (n*2)
right_d = [0] * (n*2)

def queen(line):
    global result
    if line == n:
        result += 1
        return
    for x in range(n):
        if sero[x] == left_d[x+line] == right_d[x-line] == 0:
            sero[x] = left_d[x+line] = right_d[x-line] = 1
            queen(line + 1)
            sero[x] = left_d[x+line] = right_d[x-line] = 0

queen(0)
print(result)