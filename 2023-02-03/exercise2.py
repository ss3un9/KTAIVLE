'''
Q2 (https://programmers.co.kr/learn/courses/30/lessons/86051)
0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 수 ≤ 9
numbers의 모든 수는 서로 다릅니다'''


# Q2 Answer template

"""def solution(numbers):
    answer_list=[0,1,2,3,4,5,6,7,8,9]
    cnt=0
    for i in range(0,len(answer_list)):
        if answer_list[i] not in numbers:
            cnt+=answer_list[i]
        
            
            
    return cnt"""
    
def solution(numbers):
    return 45 - sum(numbers)


numbers = [5,8,4,0,6,7,9]	
answer = solution(numbers)
print(answer)
