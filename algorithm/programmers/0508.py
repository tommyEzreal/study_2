# https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3 
# 0508 10:39 - 11:10

def solution(n, m, section):
    end,count = 0,0
    for i in range(len(section)):
        if end >= section[i]:
            continue
        end = section[i] + m - 1
        count +=1 
        if end >= n:
            break

    answer = count
    return answer

# n = 구역의 수 
# m = 붓의 길이 
# section 칠해야하는 영역

# 순서대로 리스트를 돌며 한번의 붓칠이 다음 원소까지를 포함하는지 여부를 탐색
# if n = 9/ m=4 / [1,5,9] / 1+4 -1 = 4 / 4+4-1 = 8 / 8+4-1 = 11 >= 9(n) break
# if n = 8 / m =4 / [2,3,6] / 2 + 4 -1 = 5, >= [i+1] continue  / 5+4 -1 = 8 >= n break
# if n = 5 / m =4 / [1,3] / 1 + 4 -1 = 4, >= [i+1]continue / >=n break
