num01, num02 = 200, 300
print("八进制输出：0o%o, 0o%o" % (num01,num02))
print("十六进制输出：0x%x,0x%x"%(num01,num02))
print("十进制输出：%d,%d "%(num01,num02))
print("二进制：",bin(num01),"二进制：",bin(num02))

# 小数的格式化输出
num01 = 1234567.8912
print("f标准的模式：%f" % num01)
print("f保留2位有效数字： %.2f" % num01)
print("e标准的模式：%e" % num01)
print("e保留2位有效数字： %.2e" % num01)
print("g标准的模式：%g" % 123456.4567)
print("g保留2位有效数字： %.2g" % 1234567.4567)

# 字符串的标准输出
str01 = "www.ilync.cn"
print("s标准输出： %s" % str01)
print("s固定空间中输出： %20s" % str01)  # 右对齐
print("s固定空间中输出： %-20s" % str01) # 左对齐
print("截取： %.3s" % str01)
print("截取： %10.3s" % str01)
print("截取： %-10.3s" % str01)