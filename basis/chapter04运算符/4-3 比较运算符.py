# 输入三个互不相等的整数，按照从小到大输出
num01, num02, num03 = eval(input("请输入三个整数，用逗号分隔："))
if num01 > num02 :
    if num02 > num03:
        print("从小到大输出：%d, %d ,%d " %  (num03, num02, num01))
    elif num01 > num03:
        print("从小到大输出：%d, %d ,%d " % (num02, num03, num01))
    else:
        print("从小到大输出：%d, %d ,%d " % (num02, num01, num03))
else:
    if num01 < num03:
        print("从小到大输出：%d, %d ,%d " % (num03, num01, num02))
    elif num03 > num02:
        print("从小到大输出：%d, %d ,%d " % (num01, num02, num03))
    else:
        print("从小到大输出：%d, %d ,%d " % (num01, num03, num02))
