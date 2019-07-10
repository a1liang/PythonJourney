# 使用format格式化输出
name = "Alice"
gender = "男"
age = 23
print("姓名: %s 性别：%s 年龄：%d" %(name, gender, age))
print("姓名: {}   性别：{}   年龄：{}" .format(name, gender, age))
print("姓名: {0}  性别：{1}  年龄：{2}  学生姓名：{0}" .format(name, gender, age))
print("姓名: {name}  性别：{gender}  年龄：{age}  学生姓名：{name}" .format(name=name, gender=gender, age=age))

print("姓名：{:10}" .format(name))     # 默认左对齐
print("姓名：{:<10}" .format(name))    # 左对齐
print("姓名：{:>10}" .format(name))    # 右对齐
print("姓名：{:^10}" .format(name))    # 中间对齐

print("{:<10.2f}".format(3.1415926))    # 保留2位有效数字，在10个字符空间中打印，左对齐
print("{:10.2f}".format(3.1415926))    # 保留2位有效数字，在10个字符空间中打印，默认右对齐
print("{:>10.2f}".format(3.1415926))    # 保留2位有效数字，在10个字符空间中打印，由对齐
print("{:^10.2f}".format(3.1415926))    # 保留2位有效数字，在10个字符空间中打印，中间对齐

# 数值操作
num01, num02 = 200, 300
print("十六进制打印：{0:x} {1:x}" .format(num01,num02))
print("八进制打印：{0:o} {1:o}" .format(num01,num02))
print("十进制打印：{0:d} {1:d}" .format(num01,num02))
print("二进制打印：{0:b} {1:b}" .format(num01,num02))

print("{:c}" .format(76))
print("{:e}" .format(123456.77544))
print("{:0.2e}" .format(123456.77544))
print("{:g}" .format(123456788.77544))
print("{:0.2g}" .format(123456788.77544))

print("{:%}" .format(34))
print("{:0.2%}" .format(34))
print("{:0.0%}" .format(34))

# 千位分隔符
print("{:,}" .format(123456789))