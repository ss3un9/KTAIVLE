# Q2 Answer template
def Q2(N):
    
    M=N
    count=0
    while True:
        a=M//10
        b=M%10
        c=(a+b)%10
        M=(b*10)+c
        count+=1
        if M==N:
            break
    return count
        
N=int(input())        
print(Q2(N))
    
    