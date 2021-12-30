
def solution(lottos,win_nums):
    anwer=[0,0]
    
    anwerNum = 0
    lostNum = 0

    for i in range(0,6):
        if  lottos[i] == 0:
            lostNum += 1
        else:
            for j in range(0,6):
                if  lottos[i] == win_nums[j]:
                    anwerNum += 1
                    break
    
    max = anwerNum + lostNum
    min = anwerNum

    if  max == 6:
        anwer[0] = 1
    elif max == 5:
        anwer[0] = 2
    elif max == 4:
        anwer[0] = 3
    elif max == 3:
        anwer[0] = 4
    elif max == 2:
        anwer[0] = 5
    elif max == 1:
        anwer[0] = 6
    elif max == 0:
        anwer[0] = 6    
        
    
    if min == 6:
        anwer[1] = 1
    elif min ==5:
        anwer[1] = 2
    elif min ==4:
        anwer[1] = 3
    elif min ==3:
        anwer[1] = 4
    elif min ==2:
        anwer[1] = 5
    elif min ==1:
        anwer[1] = 6
    elif min ==0:
        anwer[1] = 6
    
    return anwer
    