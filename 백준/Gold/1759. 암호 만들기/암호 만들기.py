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
L, C = map(int, input().split())
chars = input().split()
chars.sort()
# print(chars)
used = [0] * C

ans = 0

def check(string):
    aeiou = 0
    jaum = 0
    for c in string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            aeiou += 1
        else:
            jaum += 1
    if jaum >= 2 and aeiou >= 1:
        return True
    return False
        

def password(strings, last_idx):
    if len(strings) == L and check(strings):
       print(strings)
       return
    for i in range(last_idx+1, C):
        if used[i] == 0:
            used[i] = 1
            password(strings+chars[i], i)
            used[i] = 0

password("", -1)