'''
리스트를 사용자로부터 입력받아서 최대값과 최대값이 있는 인덱스를 출력하라.'''

N=list(map(int,input().split()))

print("최대값 : " , max(N))
print("최대값 인덱스 : ", N.index(max(N)))