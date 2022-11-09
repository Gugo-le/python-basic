# 조건식의 결과가 참인 동안 명령문을 반복하여 수행한다.

# 반복문이 없었다면 하나하나 작성해야겠지?
result1 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
 
print('반복문 미사용 : {0}'.format(result1))
# while 반복문을 사용하면
i = 0
result2 = 0
while i < 10:
    i = i + 1
    result2 += i
 
 ##############
print('반복문 사용 : {0}'.format(result2))

i = 0
while i < 5:
    i += 1
    print('*'*i)
    
    
#################3
count = int(input('반복할 횟수를 입력하세요: ')) # input 중요!
 
while count > 0:     # count가 0보다 클 때 반복
    print('Hello, world!', count)
    count -= 1       # count를 1씩 감소시킴    