#[잃어버린 괄호]- Silver 2
n = input().split('-') #-를 기준으로 해야 최솟값
num=[]
for i in n:
    cnt=0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

n=num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)