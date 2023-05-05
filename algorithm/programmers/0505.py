# https://school.programmers.co.kr/learn/courses/30/lessons/132267

# 0505 15:50 - 16:04
def solution(a, b, n):
    count = 0
    while n>=a:
        A = (n // a)*b 
        B = n % a
        count += A
        n = A+B

    answer = count
    return answer
  
  
# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    rank = {} #{player:rank}
    for i,player in enumerate(players):
        rank[player] = i

    for call in callings:
        called, target = rank[call], rank[call]-1
        rank[players[called]] = target
        rank[players[target]] = called
        
        #players 순서 한번에 바꿔주기 
        players[called], players[target] = players[target], players[called]
    
    answer = players
    return players
