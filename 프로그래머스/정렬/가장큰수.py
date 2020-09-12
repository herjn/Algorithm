# 내 코드
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3,reverse=True)
    answer = str(int(".join(numbers)))
    return answer

# 다른 사람 코드
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 
    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

# 접근법
# 1. lambda()
m = lambda x:x**2 / m(8)=64 의 흐름

# 2. map()
두개의 인자를 가지는데, map(str,numbers)는
numbers의 모든 요소들을 str을 통해 string으로 바꿔줌

# 3. set()
집합 자료형 / list에서 중복을 빼고 출력해주는 함수
