'''
Q) 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하여라.
'''


a=[]

for i in range(2,1001):
    cnt=0
    for j in range(2,i):
        if i%j==0:
            cnt=1
            break
        
    if cnt==0:
        a.append(i)
print(a)
        
        
            

            
    