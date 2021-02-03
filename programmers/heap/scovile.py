import heapq
def solution(scoville, K):
    answer = -1
    count = 0
    check_flag = False
    heapq_scoville = heapq.heapify(scoville)
    while scoville[0] < K:
        min_first = heapq.heappop(scoville)
        min_second = heapq.heappop(scoville)
        heapq.heappush(scoville, min_first + (min_second * 2))
        if len(scoville) == 1 and scoville[0] < K:
            check_flag = True
            break
        count = count + 1
    if check_flag == False: 
        answer = count
    return answer
