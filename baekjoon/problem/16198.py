#[에너지 모으기]- Silver 1
import sys
def energy(s):
    global maxs
    # 첫 구슬과 마지막 구슬만 남았을 때의 총합 - 최대값 비교
    if(len(marble)==2):
        if(s>maxs):
            maxs=s
        return
    else:
        for i in range(1,len(marble)-1):
            # 선택한 구슬 전후 값 저장
            ene = marble[i-1] * marble[i+1]
            temp = marble[i]
            # 선택한 구슬 제거
            del marble[i]
            energy(s + ene)
            # 위에서 제거했던 구슬 해당 위치 다시 넣기
            marble.insert(i,temp)

n = int(sys.stdin.readline())
marble = list(map(int,sys.stdin.readline().split()))
maxs = 0
energy(0)
print(maxs)
    