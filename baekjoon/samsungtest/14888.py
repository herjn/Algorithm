#[연산자 끼워넣기]
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, rest, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(rest, max_)
        min_ = min(rest, min_)
        return

    else:
        if add:
            dfs(i+1, rest+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, rest-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, rest*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(rest/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_); print(min_)