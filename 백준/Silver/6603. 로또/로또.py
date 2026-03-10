# # import sys

# # input = sys.stdin.readline
# # n = str(input())

# # rst = ""
# # for s in n:
# #     if s.islower():
# #         rst += s.upper()
# #     else:
# #         rst += s.lower()

# # print(rst)

# text = """우린 오래 전 부터 어쩔 수 없는 거였어 우주 속을 혼자 떠돌며 많이 외로워 하다가어느 순간 태양과 달이 겹치게 될때면모든 것을 이해할 수 있을거야하늘에선 비만 내렸어뼈속까지 다 젖었어얼마 있다 비가 그쳤어대신 눈이 내리더니 영화속에 볼 수 있던 눈보라가 불 때너는 내가 처음 봤던 눈동자야
# 낯익은 거리들이 거울처럼 반짝여도
# 니가 건네주는 커피 위에 살얼음이 떠도
# 우리둘은 얼어붙지 않을거야
# 바다속의 모래까지 녹을꺼야
# 춤을 추며 절망이랑 싸울거야
# 얼어붙은 아스팔트 도시위로
# 숨이 막힐 것 같이 차가웠던 공기속에
# 너의 체온이 내게 스며들어 오고 있어
# 우리 둘은 얼어붙지 않을꺼야
# 바다속의 모래까지 녹을꺼야
# 춤을 추며 절망이랑 싸울꺼야
# 얼어붙은 아스팔트 도시위로
# 너와 나의 세대가 마지막이면 어떡해
# 또 다른 빙하기가 찾아오면은 어떡해
# 긴 세월을 변하지 않을 그런 사랑은 없겠지만
# 그 사랑을 기다려 줄 그런 사람을 찾는거야
# 긴 세월을 변하지 않을 그런 사랑은 없겠지만
# 그 사랑을 기다려 줄 그런 사람을 찾는거야"""

# print(text.replace(" ", "").replace("\n", ""))

import sys
import math

input = sys.stdin.readline

# fibos = [[0, 0] for x in range(0, 45)]
# fibos[0] = [1, 0]
# fibos[1] = [0, 1]

# n = int(input())
# for i in range(n):
#     num = int(input())
#     if fibos[num][0] + fibos[num][1] == 0:
#         for j in range(2, num+1):
#             fibos[j][0] = fibos[j-1][0] + fibos[j-2][0]
#             fibos[j][1] = fibos[j-1][1] + fibos[j-2][1]
#     print(fibos[num][0], fibos[num][1])

# humans = [[i for i in range(1, 15)]]
# n = int(input())

# for i in range(n):
#     k = int(input())
#     n = int(input())
#     if len(humans)-1 < n:
#         for k in range(len(humans)-1+1, k+1):
#             li = [xc for xc in humans[k-1]]
#             for m in range(1, 14):
#                 li[m] += li[m-1]
#             humans.append(li)
#     print(humans[k][n-1])



# n = int(input())

# gaesu = [0] * 10001

# for x in range(n):
#     gaesu[int(input())] += 1
    
# for i in range(10001):
#     if gaesu[i] != 0:
#         for j in range(gaesu[i]):
#             print\\\\\

# n = int(input())
# letters = list(input())
# le = len(letters)
# for _ in range(n-1):
#     txt = list(input())
#     for i in range(le):
#         if txt[i] != letters[i]:
#             letters[i] = "?"
            
# print("".join(letters))




# n = int(input())

# for i in range(n):
#     a, b = map(int, input().split())
#     total = pow(a, b, 10)

# n = int(input())
# result = 0

# sero = [0] * n
# left_d = [0] * (n*2)
# right_d = [0] * (n*2)

# def queen(line):
#     global result
#     if line == n:
#         result += 1
#         return
#     for x in range(n):
#         if sero[x] == left_d[x+line] == right_d[x-line] == 0:
#             sero[x] = left_d[x+line] = right_d[x-line] = 1
#             queen(line + 1)
#             sero[x] = left_d[x+line] = right_d[x-line] = 0

# queen(0)
# print(result)




# if -32768 <= n <= 32767:
#     print("short")
# elif -2147483648 <= n <= 2147483647:
#     print("int")
# else:
#     print("long long")
# L, C = map(int, input().split())
# chars = input().split()
# chars.sort()
# # print(chars)
# used = [0] * C

# ans = 0

# def check(string):
#     aeiou = 0
#     jaum = 0
#     for c in string:
#         if c in ['a', 'e', 'i', 'o', 'u']:
#             aeiou += 1
#         else:
#             jaum += 1
#     if jaum >= 2 and aeiou >= 1:
#         return True
#     return False
        

# def password(strings, last_idx):
#     if len(strings) == L and check(strings):
#        print(strings)
#        return
#     for i in range(last_idx+1, C):
#         if used[i] == 0:
#             used[i] = 1
#             password(strings+chars[i], i)
#             used[i] = 0

# password("", -1)

# while True:
#     A, B = map(int, input().split())
#     if A == B == 0:
#         break

# R1, S = map(int, input().split())
# print(2*S - R1)

# N, M = map(int, input().split())
# pan = []
# min_paint = 64
 
# for _ in range(N):
#     pan.append(input())

# for i in range(N-7):
#     for j in range(M-7):
#         w = 0
#         bl = 0
 
#         for a in range(i, i+8):
#             for b in range(j, j+8):
#                 if (a + b) % 2 == 0:
#                     if pan[a][b] != 'B':
#                         w += 1
#                     if pan[a][b] != 'W':
#                         bl += 1
#                 else:
#                     if pan[a][b] != 'W':
#                         w += 1
#                     if pan[a][b] != 'B':
#                         bl += 1
 
#         if min_paint > w:
#             min_paint = w
#         if min_paint > bl:
#             min_paint = bl
 
# print(min_paint)

# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(3)
#     else:
#         print(4)

# StokuList = [list(map(int, input().split())) for _ in range(9)]

# BlankList = []
# for y in range(9):
#     for x in range(9):
#         if StokuList[y][x] == 0:
#             BlankList.append((y, x))

# def Stoku(idx):
#     if len(BlankList) <= idx:
#         for row in StokuList:
#             print(*row)
#         sys.exit()

#     y, x = BlankList[idx]

#     used = set()
#     for i in range(9):
#         used.add(StokuList[y][i])
#         used.add(StokuList[i][x])

#     sy = (y // 3) * 3
#     sx = (x // 3) * 3
#     for i in range(sy, sy + 3):
#         for j in range(sx, sx + 3):
#             used.add(StokuList[i][j])

#     values = [v for v in range(1, 10) if v not in used]

#     for value in values:
#         StokuList[y][x] = value
#         Stoku(idx + 1)
#         StokuList[y][x] = 0

# Stoku(0)

# total = int(input())
# n = int(input())
# for i in range(n):
#     m, n = map(int, input().split())
#     total -= m*n

# print("Yes" if total == 0 else "No")

# n = int(input())
# poses = []
# for i in range(n):
#     x, y = map(int, input().split())
#     poses.append([x, y])

# poses.sort(key=lambda x: (x[0], x[1]))
# for x, y in poses:
#     print(x, y)

# yaks = list(map(int, input().split()))
# yaks.sort()

# print(yaks[0] * yaks[-1])

sys.setrecursionlimit(1000000)

# memo = [-1] * 10001

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     if memo[n] == -1:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]

# n = int(input())
# print(fibo(n))

# def pisano(num):
#     answer = 1
#     mod1, mod2 = 1,2
#     while True:
#         if mod1%num == 1 and mod2%num == 1:
#             break
#         answer += 1
#         mod1, mod2 = mod2, (mod1+mod2)%num
#     return answer

# t = int(input())

# for _ in range(t):
#     n,m = map(int, input().split())
#     ans = pisano(m)
#     print(n, ans)

# 주기 : 1500000

# memo = [-1] * 1500001

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     if memo[n] == -1:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]

# n = int(input())
# print(fibo(n%1500000) % 1000000)

# n = int(input())

# memo = [0, 1]
# pisa = n%1500000
# for i in range(2, pisa+1):
#     memo.append((memo[i-1] + memo[i-2]) % 1000000)
# print(memo[pisa])

# h, m = map(int, input().split())
# timer = int(input())
# timer_h = timer // 60
# timer_m = timer % 60

# m += timer_m
# h = (h + timer_h + (m//60)) % 24
# m %= 60

# print(h, m)
import math

# def is_pal(n):
#     n = str(n)
#     return n[::-1] == n

# #1905년

# n = int(input())
# if n == 1:
#     print(1)
#     sys.exit()

# ans = -1
# total_end = int("9" * n)
# start = "1" + "0" * (n//2 - 1)
# pal = -1
# # print(start, total_end)
# while pal != total_end:
#     for i in range(0, 10):
#         pal = int(start + str(i) + start[::-1])
#         # print(pal)
#         if is_pal(math.isqrt(pal)):
#             if is_pal(pal * pal):
#                 ans = pal
#                 break
#     start = str(int(start) + 1)
# print(1905 + ans

# def ispalen(s):
#     return s == s[::-1]

# n = int(input())

# start_l = (n + 1) // 2

# for i in range(10 ** (start_l - 1), 10 ** start_l):
#     s = str(i)
#     r = int(s + s[-2::-1])   # 팰린드롬 r
    
#     X = r * r
#     Xs = str(X)
    
#     if len(Xs) != n:
#         continue
#     if not ispalen(Xs):
#         continue
#     if not ispalen(str(X * X)):
#         continue

#     print(X + 1905)
#     break
# else:
#     print(-1)

# n = int(input())
# if n == 1:
#     print(1906)
# else:
#     m = (n - 3) // 2
#     print(1905 + int("1" + "0" * m + "2" + "0" * m + "1"))

# n, r, c = map(int, input().split())
# man = (r + c) % 2
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if (i+j) % 2 == man:
#             print("v", end="")
#         else:
#             print(".", end="")
#     print()

# values = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
# result = 0
# for i in range(2):
#     color = input().rstrip()
#     n = values.index(color)
#     result = (result + n) * 10
# result //= 10
# color = input().rstrip()
# n = values.index(color)
# result *= 10 ** n
# print(result)

# N, K = map(int, input().split())
# banaang = []
# dp = [[0] * (K+1) for _ in range(N+1)]
# for _ in range(N):
#     banaang.append(list(map(int, input().split())))

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         item = banaang[i-1]
#         if j >= item[0]:
#             dp[i][j] = max(dp[i - 1][j], item[1] + dp[i - 1][j - item[0]])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[N][K])
# t = int(input())
# for _ in range(t):
#     problems = input()
#     strik = 0
#     ans = 0
#     for problem in problems:
#         if problem == "O":
#             strik += 1
#             ans += strik
#         else:
#             strik = 0
#     print(ans)
# t = int(input())
# for x in range(t):
#     dp = [[1] * 2001] + [[0] * 2001 for _ in range(10)]
#     n, m = map(int, input().split())
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             dp[i][j] = dp[i][j-1] + dp[i-1][j // 2]

#     print(dp[n][m])

# def lotto(idx):
#     global result, S
#     news = S[idx:]
#     if len(news) < 6 - len(result):
#         return
#     if len(result) == 6:
#         print(*result)
#         return
#     for i in range(len(news)):
#         result.append(news[i])
#         lotto(i)
#         del result[-1]

# S = list(map(int, input().split()))
# k = S[0]
# del S[0]
# result = []
# lotto(0)

def lotto(s, result, index, k):
    if len(result) == 6:
        print(*result)
        return
    for i in range(index, k):
        lotto(s, result + [s[i]], i + 1, k)

while True:
    S = list(map(int, input().split()))
    k = S[0]
    if k == 0:
        break
    del S[0]
    lotto(S, [], 0, k)
    print()
