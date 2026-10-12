#学生成绩管理：
#功能实现：
# 创建一个空列表 scores。

# 依次添加 5 个整数成绩（使用 append）：88, 92, 76, 85, 90。

# 删除第 3 个成绩（索引2，值为76）。

# 修改第 2 个成绩（索引1）为 95。

# 在末尾添加一个新成绩 100。

# 打印最终列表和总成绩（用 sum() 函数）。

# scores = []
# for score in [88,92,76,85,90]:
#     scores.append(score)
# print(scores)

# # del scores[2]
# scores.remove(76)
# print(scores)
# scores[1] = 95
# print(scores)
# scores.append(100)
# print("最终列表为：",scores) 
# total = sum(scores)         #sum()函数
# print(f"最终成绩为{total}")
# x = 0 
# for result in range(len(scores)):
#     x+=scores[result]
# print("     总成绩为：",end="")
# print(x)



# 创建一个元组 course = ("Python", "Java", "C++")。

# 尝试修改第一个元素为 "Go"（观察报错，然后注释掉）。

# 将元组转换成列表，修改列表的第一个元素为 "Go"，再转回元组，打印新元组。

# 用 for 循环遍历新元组，打印每个元素。

course = ("python","java","C++")
# course[1] = ("Go")
course_list = list(course)
course_list[1]="Go"
course_tuple = tuple(course_list)
print(course_tuple)
for i in course_tuple:
    print(i)