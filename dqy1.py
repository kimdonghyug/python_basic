num = 0
hap = 0
while num < 10:
    num +=1
    if num %3 == 0:
        continue
        
    hap += num 
print(f"1~100까지의 수중에서 3의 배수가 아닌 수들의 합은 {hap}")