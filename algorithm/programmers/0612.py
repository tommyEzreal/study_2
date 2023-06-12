# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    out = len(t) - len(p) + 1

    count = 0
    for i in range(out):
        sliced = t[i:i+len(p)]
        if int(sliced) <= int(p):
            count += 1
    return count
 
    
    
    
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    last_index = {}
    for i in range(len(s)):
        if s[i] not in last_index:
            answer.append(-1)
        else:
            answer.append(i - last_index[s[i]])
        last_index[s[i]] = i
    
    return answer
  
