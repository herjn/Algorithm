#완전탐색 문제 level 1
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result


def solution(answers):
    answer=[]
    c1=0;c2=0;c3=0
    pattern1 = [1,2,3,4,5]*2000
    pattern2 = [2,1,2,3,2,4,2,5]*1250
    pattern3 = [3,3,1,1,2,2,4,4,5,5]*1000

    for v1,v2,v3,ans in zip(pattern1,pattern2,pattern3,answers):
        if v1==ans: c1+=1
        if v2==ans: c2+=1
        if v3==ans: c3+=1
    
    list=[c1,c2,c3]
    max_list=max(list)
    for i,s in enumerate(list):
        if s == max_list:
           answer.append(i+1)

    return answer