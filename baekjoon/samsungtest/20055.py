#[컨베이어 벨트 위의 로봇]
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
n *= 2

rotate = 0 # 지금까지 벨트 회전 횟수
dur = list(map(int, input().split())) # i번 칸의 내구도 
robot = [0] * n # i번 칸 위의 로봇의 번호 (단, 없으면 0)

while dur.count(0) < k :
    # 1단계 : 벨트가 회전 / dur + robot 한칸씩 밀어줌
    rotate += 1
    dur.insert(0, dur.pop())
    robot.insert(0, robot.pop())
    robot[n//2-1] = 0 # 내리는 위치 로봇 삭제

    # 2단계 : 로봇 한칸씩 움직임
    arr = []
    for i in range(n):
        if robot[i] > 0 :
            arr.append((robot[i],i))
        
    arr = sorted(arr)
    for (r,i) in arr:
        if robot[i+1] == 0 and dur[i+1] > 0 :
            robot[i] = 0
            robot[i+1] = r
            dur[i+1] -= 1
    robot[n//2-1] = 0

    # 3단계 : 올라가는 위치에 로봇을 올린다.
    if dur[0] > 0 :
        dur[0] -= 1
        robot[0] = rotate+1

print(rotate)
