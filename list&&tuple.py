# 创建列表
fruits = ["苹果", "香蕉", "橙子"]
scores = [90, 85, 78]
mixed = [1, "hello", True, 3.14]

# 访问元素（索引从0开始）
# print(fruits[0])   # 苹果
# print(fruits[-1])  # 橙子（-1 表示最后一个、-2即表示倒数第二个）

# 切片
# print(fruits[1:3]) # ['香蕉', '橙子']
# fruits.append("荔枝")    ###添加元素
# ADD = fruits
# print("列表长度为:",len(fruits), "  列表内容为: ",fruits[0:])
# print("###添加结束，已经添加1个水果####")
# fruits.insert(3,"芒果")  ###指定位置插入
# print(fruits)
# del fruits[0]
# fruits.remove("香蕉")
# print("###删除结束，已经删除2个水果####")
# print(fruits)
# print(len(fruits))
# print("荔枝" in fruits)


# 创建元组
colors = ("红", "绿", "蓝")
single = (5,)          # 只有一个元素时要加逗号

print(colors[1])
# colors[0] = "黑"  #尝试修改会报错
for i in range(len(fruits)):
    print(i, fruits[i])