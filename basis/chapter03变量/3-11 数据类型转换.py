"""
num01 = input("请输入第一个数：")
num02 = input("请输入第二个数：")
print(type(num01))
# 需要把字符串的类型转换为整型
print("%d + %d = %d" %(int(num01),int(num02),int(num01)+int(num02)))
"""
# 总结
"""
数据类型转换： 要转换的类型（数据）
1、要把num01转为整数   int(num01)
2、要把num01转为浮点数   float(num01)
3、要把num01转为字符串   str(num01)
4、要把num01转为bool   bool(num01)
"""
print(int("12345") + 1)
print(float("12.345") + 1.187)
print(str(123) + "456")
print(bool(-1))
print(bool(0))
# 如果转为bool类型，非0 -->True, 0 --> False

print(int(12.945))  # 去除小数点后的值
# print(int("爱我中华"))

# 在做数据类型转换的时候，不是所有的转换都能成功，需要做异常处理

# 数值 --- 字符
print(ord("X"))
print(chr(88))

# 进制
print(hex(200))
print(oct(200))
print(bin(200))

