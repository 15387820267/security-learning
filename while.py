
count = 0
while count <= 5:
    print(count)
    count = count + 1

numbers = [1,2,3,4,5,6,7,8,9,10]
for n in  numbers:
    if n % 2 == 0:
        print("找到偶数",n)
        break
for m in range(1,9):
    if m % 2 == 0:
        continue
    print(m)
