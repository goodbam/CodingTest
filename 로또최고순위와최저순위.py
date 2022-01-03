
def solution(lottos,win_nums):
    anwer=[0,0]
    
    Num = 0
    lostNum = 0

    for i in range(0,6):
        if  lottos[i] == 0:
            lostNum += 1
        else:
            for j in range(0,6):
                if  lottos[i] == win_nums[j]:
                    Num += 1
                    break
    
    max = Num + lostNum
    min = Num

    reslut = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    anwer[0] = reslut[max]
    anwer[1] = reslut[min]

    return anwer
    