# [시험감독]
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split())) 
# 총감독,부감독
b,c =  map(int, input().split())

# 감독관 최소 수
ans = n
for num in arr:
    # 각 반에 감독관 1명 씩 계산
    num -= b

    if num < 0 :
        continue
    
    # 남는 학생들에 대해  부감독관을 넣음
    if num % c == 0:
        ans += num // c
    
    else :
        ans += num // c + 1

print(ans)
