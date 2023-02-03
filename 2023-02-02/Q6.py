'''Q6 (https://programmers.co.kr/learn/courses/30/lessons/12934)
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.'''


# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
a_data=list(data)
result=1
for n in a_data:

    if int(n)==0 or int(n)==1:
        result+=int(n)
        print('+' ,n ,end=' ')
    else:
        result=result*int(n)
        print('x', n ,end=' ')
