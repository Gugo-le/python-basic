a = [1,2,3] # 리스트 만들기
b = ['Life', 'is', 'short']
c = [1, 2, 'life', 'is']
d = [1, 2, [3, 4], ['life', 'is']]

#리스트 인덱싱
print(d[0]) # 1
print(d[2]) # [3, 4]
print(d[3][-1]) # is

#리스트 연결
print(a+b)
print(b[0] + " hi~") # life hi~

#리스트 반복
print(a*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 삭제,,, del 사용
del a[-1]
print(a) #[1, 2]

# 리스트 추가,,, append 사용
a.append(5)
print(a) #[1, 2, 5]

# 원소 정렬
b.sort()
print(b) # ['Life', 'is', 'short']

# 원소 삭제
a.remove(2)
print(a) #[1, 5]

# 특정 원소값의 개수
a = [2,1,4,5,2,2,3,4]
print(a.count(2)) #2의 개수는 ??? 3