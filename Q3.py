def bin_search(a, key):
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr:
            break
    
    return -1

a=list(map(int,input().split()))

answer = bin_search(a, 39)

if answer==-1:
    print("검색 값 없음")
else:
    print("검색값 39 있음")

