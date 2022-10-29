rows = int(input("파스칼의 삼각형을 출력할 행의 개수를 입력하세요> "))
lst=[]

for i in range(rows):
    lst.append([])
    lst[i].append(1)
    
    for j in range(1, i):
        lst[i].append(lst[i-1][j-1]+lst[i-1][j])
        
    if(rows != 0):
        lst[i].append(1)
  
a = len(str(lst[-1]))
for i in range(rows):
    if i == 0:
        str_temp = str([lst[0][0]])
        print(f'{str_temp:^{a}}')
    else:
        str_temp = str(lst[i])
        print(f'{str_temp:^{a}}')