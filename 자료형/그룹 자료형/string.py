s1 = 'Hello world'
print(s1) # Hello world 출력 ', '', ''' 상관없다.
 
 #문자열 연결
 
head = "python"
tail = " is fun"
print(head+tail)
 
print(head*2) # pythonpython
print(head*3) # pythonpythonpython

# 문자열 인덱싱
a= "Now is better than never"

print(a[0]) # N

print(a[2]) # w

print(a[-1]) # r

# 문자 개수
b = "python"
print(b.count('p')) # 1

print(b.find('y')) # 1

print(b.index('p')) # 0

# 문자 삽입

b = ","
c = b.join('Abcd')
print(c) # A,b,c,d

#문자열 바꾸기
a = 'Python is difficult'
print(a.replace("difficult","fun")) # Python is fun

# 문자열 나누기

print(a.split()) # ['Python', 'is', 'difficult']