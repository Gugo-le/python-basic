#for 변수 in 리스트(또는 튜플, 문자열):
   # 수행할 문장1
   #수행할 문장2

test_list = ['one', 'two', 'three']

for i in test_list:   
    x = i + '!'
    print(x)
    #one!
    #two!
    #three!
    
number = 0

for score in [90,25,67,45,93]:
    number += 1    
    
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)    
    
#1번 학생은 합격입니다.
#2번 학생은 불합격입니다.
#3번 학생은 합격입니다.
#4번 학생은 불합격입니다.
#5번 학생은 합격입니다.



# +range function
# 1 부터 10까지 더한 값
add = 0 
for i in range(1, 11): 
     add = add + i 
print(add)
    
# 구구단    
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
         print(i*j, end=" ") 
         print('')
         
         
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    print(result)         
    
# 짝수에만 3을 곱하여 리스트 출력    
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)    


index = 0
s = "BlockDMask" 
for a in s:
    if a == 'k':            
        break    # 'k'를 찾았으니 for문에서 나와랏!
     
    index = index + 1


print(index)    # 'k'가 첫번째로 존재하는 위치 출력