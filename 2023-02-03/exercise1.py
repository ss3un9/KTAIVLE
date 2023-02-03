# Q1 Answer template
def maximum(lottos,win_nums):
    cnt=0
    for n in lottos:
        if n==0:
            cnt+=1
        if n in win_nums:
            cnt+=1
    #print(cnt)
    return cnt

def minimum(lottos,win_nums):
    cnt=0
    for n in lottos:
        if n in win_nums:
            cnt+=1
    #print(cnt)
    return cnt

def win_cnt(cnt):
    if cnt==6:
        return 1
    if cnt==5:
        return 2
    if cnt==4:
        return 3
    if cnt==3:
        return 4
    if cnt==2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    cnt=0
    max_cnt=maximum(lottos, win_nums)
    answer.append(win_cnt(max_cnt))
    
    min_cnt=minimum(lottos, win_nums)
    answer.append(win_cnt(min_cnt))
    
    print(answer)
            
    return answer

lottos = [0,0,0,0,0,0]
win_nums = [38, 19, 20, 40, 15, 25]
solution(lottos, win_nums)
#print(answer)