def solution(n, lost, reserve):
    rese = set(reserve)-set(lost)
    losts = set(lost)-set(reserve) 
    for i in rese:
        if i-1 in losts:
            losts.remove(i-1)
        elif i+1 in losts:
            losts.remove(i+1)
            
    return n-len(losts)

# 문제에서 lost와 reserve는 중복되지 않는다고 나와있으므로 set 연산을 해도 그대로이다
# 만약 중복될 경우를 대비해 중복을 제거해준다

