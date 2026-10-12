####计算累计1+2....+100####

m = 1
total = 0

while m <= 100:
    total += m
    m += 1
print("计算好了",total)




####乘法口诀表###

for i in range(1, 10):
    j=1
    while j <= i :
        print(i,"*",j,"=",i*j,end="  ")
        j += 1
    print()


for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}", end=" ")
    print()