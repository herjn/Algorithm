test=int(input())

for _ in range(test):
    x,y=map(int,input().split())
    distance=y-x
    cnt=0 #이동 횟수
    move=1  #cnt별 이동 가능한 거리
    move_sum=0  #이동한 거리의 합

    while move_sum<distance:
        cnt+=1
        move_sum+=move 
        if cnt%2==0: 
            move+=1  
    print(cnt)