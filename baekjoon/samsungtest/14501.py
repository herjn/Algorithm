#[퇴사]
N = int(input())
work = []
max_pay = [0] * N

for _ in range(N):
    work.append(list(map(int, input().split())))
   
for i in range(N-1, -1, -1): 
    day = work[i][0]
    pay = work[i][1]
     #남은 기간보다 상담일이 길 경우
    if day > N - i:
        if i != N-1:  
            max_pay[i] = max_pay[i+1] #이전 최댓값 저장
        continue

    #마지막 날 하루 상담    
    if i == N-1: 
        max_pay[i] = pay 
    # 현재 일을 시작하면 마지막에 끝나는 경우
    elif i + day == N: 
        max_pay[i] = max(pay, max_pay[i+1])
    else:
        #현재 일을 맡을 경우 or 맡지 않을 경우
        max_pay[i] = max(pay + max_pay[i + day], max_pay[i+1])
        
print(max_pay[0]) 
