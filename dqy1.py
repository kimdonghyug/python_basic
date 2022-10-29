input_num = int(input("Enter the number of rows: "))
list = [] #an empty list
num = 0
for n in range(input_num):
    list.append([])
    list[n].append(1)

    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])

    list[n].append(1)
del list[0][0]

pascal = []

for i in range(input_num):
    temp = ''
    for j in range(i+1):
        temp += (str(list[i][j]) + ' ')
    
    pascal.append(temp)

last_len = len(pascal[-1])

last_len1 = len(pascal[-1])

for i in range(input_num):
    while last_len1 > 0:
        last_len_half = last_len / 2
        vacuum = last_len_half * ''
        pascal[num].append(vacuum)
        num +=1
        last_len1 -=1
print(pascal)