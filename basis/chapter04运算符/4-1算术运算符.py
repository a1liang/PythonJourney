# 运算的基本介绍
print(100 + 200)
print(100 - 200)
print(100 * 200)
print(10 / 3)
print(round(10 / 3,2))          # round() 函数
print("%.2f" % (10 / 3))        # 基本的格式化输出
print("{:.2f}".format(10 / 3))  # format格式化输出
print(10 // 3)                  # 除之后取整
print( 10 % 5)
print(3 ** 4)                   # 3**4 = 3*3*3*3

"""
输入一个三位数，然后输出每个位置的数字
    比如输入：719    ，显示如下：
    百位数字：7  十位数字：1  个位数字：9
"""
# 方法01
# print(719//100)
# print(719%100//10)
# print(719%10)
"""
num = int(input("请输入一个三位数："))
bai = num // 100
shi = num % 100 // 10
ge = num % 10
print("三位数{0}的百位数字：{1}  十位数字：{2}    个位数字：{3}" .format(num, bai, shi, ge))
"""

# 方法02
num = input("请输入一个三位数：")
print("三位数{0}的百位数字：{1}  十位数字：{2}    个位数字：{3}" .format(num,num[0],num[1],num[2]))














