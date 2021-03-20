#[소수의 곱]- Gold 2
import heapq

if __name__ == '__main__':
    n,k=map(int,input().split())
    prime=list(map(int,input().split()))

    pq = []
    for num in prime:
        heapq.heappush(pq,num)

    for i in range(n): 
        num = heapq.heappop(pq)
        for j in range(k): 
            new_num = num * prime[j]
            heapq.heappush(pq, new_num)

            if num%prime[j] == 0:  
                break
    else:
        print(num)