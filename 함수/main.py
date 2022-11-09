def func1():
    print('gugo')
 
# 함수 호출
func1()
func1()
func1()


def func2(a, b):
    print(f'{a} 곱하기 {b} = {a * b}')
 
func2(1, 2)
func2(1, 3)
func2(2, 4)

#############
def func3():
    return "abcdefg"
 
a = func3()
print(a + "GG")

##############
def func4(a, b):
    return a * b
 
 
c = func4(3, 9)
print(c)



# 구구단 no 함수 버전
 
# 구구단 출력
for i in range(1, 10):
    print(f'{2} x {i} = {2 * i}')
for i in range(1, 10):
    print(f'{3} x {i} = {3 * i}')
 
# ...
for i in range(1, 10):
    print(f'{9} x {i} = {9 * i}')
    
    
    # 구구단 함수 버전
def gugudan(num):
    for i in range(1, 10):
        print(f'{num} x {i} = {num * i}')
 
# 구구단 출력
gugudan(2)
gugudan(3)
# ...
gugudan(9)