#[이전 순열]- Silver 3
import sys
n = int(input())
bef = [x for x in sys.stdin.readline().split()]

# k의 최댓값 찾기
k = -1
for i in range(len(bef)-1):
    if bef[i]>bef[i+1]:
        k = i

#오름차순인 경우
if k == -1:
    print(-1)
else:
    for j in range(k+1,len(bef)):
        if bef[j]<bef[k]:
            a = j
    
    bef[k], bef[a] = bef[a], bef[k]
    und = bef[k:1]
    und.sort(reverse=True)
    ans = bef[:k+1] + und
    
    for i in ans:
        print(i, end=' ')
    print()