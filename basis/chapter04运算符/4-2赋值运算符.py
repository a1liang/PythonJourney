# 编程实现145893秒是几天几小时几分钟几秒
total = 145893
day = total // (24 * 60 * 60)
hour = (total % (24 * 60 * 60)) // (60 * 60)
minute = total % (60 * 60) // 60
second = total % 60
# 打印
print("%d秒为 %d天 %d小时 %d分 %d秒 " %(total, day, hour, minute, second))

# 用户输入语文、数学、英语分数，输出总分和平均分
Chinese = int(input("请输入语文分数："))
Math = int(input("请输入数学分数："))
English = int(input("请输入英语分数："))
print("本次考试的总分%.2f, 平均分%.2f " %(Chinese + Math + English, (Chinese + Math + English)/3))


