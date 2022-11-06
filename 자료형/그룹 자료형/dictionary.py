dic = {'name': 'Gugo', 'phone':'01039404946', 'birth':'0718'}

# 원소 추가
dic[1] = 'a'
print(dic) #{'name': 'Gugo', 'phone': '01039404946', 'birth': '0718', 1: 'a'}

dic['pet'] = 'none'
print(dic) #{'name': 'Gugo', 'phone': '01039404946', 'birth': '0718', 1: 'a', 'pet': 'none'}

# 원소 삭제
del dic[1]
print(dic) #{'name': 'Gugo', 'phone': '01039404946', 'birth': '0718', 'pet': 'none'}

# 원소의 value 구하기
dic['pet']
print(dic['pet']) #none

dic['name']
print(dic['name']) # Gugo

#key 리스트 만들기
print(dic.keys()) #dict_keys(['name', 'phone', 'birth', 'pet'])
print(list(dic.values())) #['Gugo', '01039404946', '0718', 'none']

#key,value 쌍 구하기
print(dic.items()) #dict_items([('name', 'Gugo'), ('phone', '01039404946'), ('birth', '0718'), ('pet', 'none')])

# 원소 삭제
print(dic.clear()) #none