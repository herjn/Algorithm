def solution(priorities, location):
  from collections import deque
  answer = 0
  deq = deque([(v,i) for i,v in enumerate(priorities)])

  while len(deq) > 0:
      item = deq.popleft()
      #print(item)
      if max(deq)[0] > item[0]:
          deq.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer