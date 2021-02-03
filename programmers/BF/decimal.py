import math
import itertools

# 소수인지 판별해주는 함수
def is_decimal(n):
    if n < 2: return False
    to = int(math.sqrt(n)) + 1
    for i in range(2, to):
        if n % i == 0: return False
    return True

def solution(number):
    candidate = set()
    for i in range(len(number)):
        numbers = set(map(int, map(''.join, itertools.permutations(number, i+1))))
        candidate |= numbers # 합집합

    answer = 0
    candidate = list(candidate) # 리스트 변환
    for n in candidate:
        if is_decimal(n):
            answer += 1
    return answer

# 더 간단한 코드 
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a