#f = open('./gugo.txt', 'w')
#f.close

#파일 만들기
f = open('./gugo.txt', 'w')
for i in range(1, 6):
    data = "%d "% i
    f.write(data)
f.close()

#파일 읽기
f = open('./gugo.txt', 'r')
line = f.readline()
print(line)
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
