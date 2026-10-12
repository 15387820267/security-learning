score=float(input("请输入你的分数："))
if score > 100 or score < 0:
    print ("分数无效噢")
elif score >= 90 and score <= 100:
    print("你的成绩是：优秀A")
elif score >=80:
    print("你的成绩是：良好B")
elif score >=70:
    print("你的成绩是：良好C")
elif score >=60:
    print("你的成绩是：及格C，加油！")
else:
    print("回去种地去吧")




if score >=60:
    print("你及格了")
else:
    print("你不及格")
print(score)