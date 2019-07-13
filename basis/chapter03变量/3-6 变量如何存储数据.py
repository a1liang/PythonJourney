# 变量是为了方便取出存储在内存中的数据

if __name__=='__main__':
    num01 = 100
    num02 = 100
    num03 = 100
    num04 = num01
    num05 = 200
    print("num01的内存地址：",id(num01))
    print("num02的内存地址：",id(num02))
    print("num03的内存地址：",id(num03))
    print("num04的内存地址：",id(num04))
    print("num05的内存地址：",id(num05))
    # 对于数值类型，相同的值只存储一份

    str01 = "www.ilync.cn"
    str02 = "Steven"
    str03 = "Steven"
    print(id(str01))
    print(id(str02))
    print(id(str03))

    # str01中的n
    print("str01中的内存地址:",id(str01))
    print("str01中的n内存地址:",id(str01[-1]))

    print("str02中的内存地址:",id(str02))
    print("str02中的n内存地址:",id(str02[-1]))