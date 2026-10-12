def add(a,b):
    return a + b

result = add(3,5)
print(result)

with open("ips.txt", "r") as f:
    for i in f:
        print(i.strip())