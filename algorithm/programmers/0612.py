# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    out = len(t) - len(p) + 1

    count = 0
    for i in range(out):
        sliced = t[i:i+len(p)]
        if int(sliced) <= int(p):
            count += 1
    return count
  
  
  
