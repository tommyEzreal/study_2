# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):

    # Starting_point
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                current_point = [i,j]
                break
    
    for route in routes:
        local_point = [current_point[0], current_point[1]] # 객체 초기화 

        for i in range(int(route[-1])):
            
            if route[0] == "E":
                if local_point[1]+1 > len(park[0])-1: # range break
                    local_point = [current_point[0], current_point[1]]
                    break
                
                elif park[local_point[0]][local_point[1] + 1] == "X" : # X break
                    local_point = [current_point[0], current_point[1]]
                    break 
                else:
                    local_point[1]+=1

                
            elif route[0] == "W":
                if local_point[1]-1 < 0:
                    local_point = [current_point[0], current_point[1]]
                    break

                elif park[local_point[0]][local_point[1] -1]=="X" :
                    local_point = [current_point[0], current_point[1]]
                    break
                else: 
                    local_point[1] -= 1


            elif route[0] == "S":
                if local_point[0]+1 > len(park)-1:
                    local_point = [current_point[0], current_point[1]]
                    break

                elif park[local_point[0]+1][local_point[1]]=="X" :
                    local_point = [current_point[0], current_point[1]]
                    break
                else: 
                    local_point[0] += 1


            else:
                if local_point[0]-1 < 0:
                    local_point = [current_point[0], current_point[1]]
                    break

                elif park[local_point[0]-1][local_point[1]]=="X":
                    local_point = [current_point[0], current_point[1]]
                    break
                else: 
                    local_point[0] -= 1
        
        current_point = [local_point[0],local_point[1]]

    answer = current_point

    return answer
