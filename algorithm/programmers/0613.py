# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

#0613 15:35 - 
def solution(nums):
    sorted = []
    for i in nums:
        if i not in sorted:
            sorted.append(i)
    if len(nums)/2 > len(sorted):
        answer = len(sorted)
    else:
        answer = len(nums)/2
    return answer

# 중복제거,
# 4/2 = 2번 뽑기 , 서로다른 3개 : max=2 
# 6/2 = 3번 뽑기, 서로다른 3개 : max=3 
# 6/2= 3번 뽑기, 서로다른 2개: max=2 
# len(nums)/2 번뽑기, 
# if len(nums)/2 > len(sorted) : max = len(sorted) 
# elif len(nums)/2 <= len(sorted) : max = len(nums)/2



# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if a==b:
        answer = a
    elif a < b:
        for i in range(a,b+1):
            answer+=i
    else:
        for i in range(b, a+1):
            answer += i
    
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/133502


def solution(ingredient):
    stack = []
    count = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            count += 1
            for _ in range(4):
                stack.pop()
    return count
