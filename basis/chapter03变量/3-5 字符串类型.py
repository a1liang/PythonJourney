if __name__=='__main__':
    # 表示方法：单引号或者双引号
    str01 = "iLync"
    str02 = 'Steven'
    print(str01)
    print(str02)
    # 长字符串的表示：\--续行符号   三个双引号或者三个单引号，保持原本的格式
    str01 = "My name is Alice, My name is steven."\
            "My name is Alice, My name is steven. My name is Alice, My name is steven."\
            " My name is Alice, My name is steven. "
    print(str01)

    str02 = """My name is Alice, My name is steven. 
            My name is Alice, My name is steven. 
        My name is Alice, My name is steven.     
    """
    print(str02)
    # 转义字符和取消转义
    print("My \t name is \nAlice.")
    print("我是\"中国人\"")
    print("我的Python资料在D:\\Python\\")

    print(r"我的Python资料在D:\Python\ ")
    print(r"My \t name is \nAlice.")
    # 运算符+ *
    name = "Alice"
    print("我是" + name)
    print("我的年龄",11)
    print("我是帅哥"*10)
    # 索引的方式
    str01 = "abcdefghigklmnopqrstuvwxyz"
    print(str01[0]) #第一个字符
    print(str01[-1]) #最后一个字符
    print(str01[4]) #第五个
    print(str01[-5]) #倒数第五个
    print(str01[5:]) #从第六个开始到结束
    print(str01[-5:]) #从倒数第五个开始到结束
    print(str01[3:10]) #从第四个开始到第10个

    # 求长度
    print("字符串的长度：", len(str01))
    # 是否包含
    str02 = "xyz"
    print("是否包含：",str02 in str01)
    print("是否不包含：",str02 not in str01)
    # 判断是否相等
    str02 = "abcdefghigklmnopqrstuvwxyz"
    print(str01 == str02)
    print(str01 is str02)
