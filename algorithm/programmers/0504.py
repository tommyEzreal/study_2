# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):

    rates = {}
    for i in range(N):

        rate = stages.count(i+1)
        if rate == 0:
            rates[i+1] = 0
            continue
        rate = rate / len([j for j in stages if j >= i+1])

        rates[i+1] = rate


    srted_res = sorted(rates.items(), key = (lambda x: x[1]), reverse=True)
    answer = [res[0] for res in srted_res]

    return answer
  
  
# https://school.programmers.co.kr/learn/courses/30/lessons/131705 

def solution(number):
    
    count = 0
    for i in range(0,len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] ==0:
                    count+=1
                    
    answer = count
    return answer
