# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 0507 14:46 - 15:02
# dict mapping 
# 없으면 continue 

def solution(name, yearning, photo):
    mapped = {name:yearning for name, yearning in zip(name, yearning)}

    result = []
    for i in range(len(photo)):
        count = 0
        for j in range(len(photo[i])):
            try:
                count += mapped[photo[i][j]]
            except:
                continue
            
        result.append(count)
    
    return result
  
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 시간복잡도 통과
# forward, backward dict를 따로 만들어서 backward는 각 id마다 관측시 +1되도록 

def solution(id_list, report, k):
    # 중복 미리제거한 report생성
    report = list(set(report))
    # 공백기준 원소나누기
    report = [r.split(' ') for r in report]
    
    # report에서 각 사람별 신고당한 횟수와 누굴 신고했는지 담겨있는 dict
    
    
    forward = {} # forward = [신고한 사람1, 신고한사람2,..]
    backward = {} # backward = 신고당한 횟수 
    for id in id_list:
        forward[id] = []
        backward[id] = 0
    
    for r in report:
        forward[r[0]].append(r[1]) # 누굴 신고했는지 append
        backward[r[1]] += 1 # 신고당한 횟수 +1 
    
    result = []
    for id in id_list: # id = muzi
        ban = len([cand for cand in forward[id] if backward[cand] >= k])
        result.append(ban)    
    
    
    return result
