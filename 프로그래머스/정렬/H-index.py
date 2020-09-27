#내코드
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


#다른사람 코드
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
