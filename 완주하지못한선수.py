
def solusion (completion,participant):
    answer =""
    
    completion.sort()
    participant.sort()

    for i in range(len(participant)):
    
        if not completion:
            answer = participant[0]
            break

        if participant[0] == completion[0]:
            del participant[0]
            del completion[0]
            print(participant)
            print(completion)
        else:
            answer = participant[0]
    
    return answer