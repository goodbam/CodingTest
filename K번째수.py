def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        
        q = commands[i][0]
        w = commands[i][1]
        e = commands[i][2]
        
        a = array[q-1: w]
        a.sort()
        answer.append(a[e-1])
        
    return answer