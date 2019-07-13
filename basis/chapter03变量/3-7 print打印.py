if __name__=='__main__':
    # print用来打印
    print("Hello , World !")

    student_age = 18
    print("学生的年龄为：" ,student_age)
    # print("学生的年龄为：" ) 不换行！ print(student_age)

    # print执行完成后换行
    print("Hello , World !", end="\n")

    # 如果希望打印不换行，需要修改end = ""
    print("Hello , World !", end=" ")
    print("Hello , World !", end="\n")

    # 一次打印多个变量、值
    print("Alice","Bob","Tomas","Peter",sep="=|=")

    money =121
    print("本次消费的金额为：",money,sep="￥")

    #输出到文件：
    str01 = "本次消费的金额为：121元"
    f = open("D:\Python\Project\第一季基础入门篇\Sales.txt","w") #write
    print(str01,file = f)

