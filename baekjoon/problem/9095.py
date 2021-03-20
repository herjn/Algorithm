#[1,2,3 더하기]- Silver 3
test=int(input())
ipt_lst=[]
for i in range(test):
    ipt_lst.append(int(input()))

dp=[1,2,4]
for i in range(3,max(ipt_lst)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in ipt_lst:
    print(dp[i-1]) #방법의 수 