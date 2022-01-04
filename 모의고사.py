def solution(answers):
    SuFoJa1 = [1, 2, 3, 4, 5] # 5
    SuFoJa2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    SuFoJa3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    score = [[1,0],[2,0],[3,0]]
    
    
    for i in range(0,len(answers)):
        if SuFoJa1[i % 5] == answers[i]:
            score[0][1] += 1
        
        if SuFoJa2[i % 8] == answers[i]:
            score[1][1] += 1
        
        if SuFoJa3[i % 10] == answers[i]:
            score[2][1] += 1
        
    max_value = []
    for key, value in score:
        max_value.append(value)
    max_value.sort()

    answer = []
    i = 0
    for key,value in score:
        if score[i][1] == max_value[2]:
            answer.append(key)
        i += 1
            
    return answer