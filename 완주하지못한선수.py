
def solution(participant, completion):
    answer = ""
    
    completion.sort()
    participant.sort()

    completion.append('null')
    
    for i in range(len(participant)):

        if completion[i] == 'null':
            answer = participant[i]
            break

        if participant[i] != completion[i]:
            answer = participant[i]
            break
        
    return answer