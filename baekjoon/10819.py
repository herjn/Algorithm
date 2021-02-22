#[차이를 최대로]- Silver 2
#DFS 풀이
from sys import stdin
def dfs(depth):
    global answer
    if depth==n:
        answer.append([nums[i] for i in check])
    else:
        for i in range(n):
            if i in check:
                continue
            check[depth]=i
            dfs(depth+11)
            check[depth]=-1

if __name__ == '__main__':
    answer=[]
    n = int(stdin.readline())
    nums = sorted(list(map(int,stdin.readline().split())))
    check = [-1]*n
    dfs(0)
    min=0
    for case in answer:
        sum_case = 0
        for i in range(n-1):
            sum_case += abs(case[i]-case[i+1])
        min=max(min, sum_case)
    print(min)
 

# itertools 풀이
from itertools import permutations
N = int(input())
cases = permutations(sorted(list(map(int, input().split()))))
answer = 0

for case in cases:
    sum_case = 0
    for i in range(N - 1):
        sum_case += abs(case[i]-case[i+1])
    answer=max(answer,sum_case)
print(answer)