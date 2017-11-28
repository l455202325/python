__author__ = "ZiXing"
# _*_coding:utf-8_*_

import json
import os

users = []
# 查找所有用户
if (os.path.exists("users.db")):
    with open("users.db", "r") as user_db_get:
        users = json.load(user_db_get)
        user_db_get.close()

# 保存用户
def save_user(json_data):
    with open("users.db", "w") as user_db_save:
        users.append(json_data)
        json.dump(users, user_db_save)
        user_db_save.close()
        print ("新增用户完成！")



info = '''
    1.登录
    2.注册
    Q.退出
'''
is_loop = True
while(is_loop):
    print(info)
    input_type = int(input("请选择 "))

    if(input_type == 1):
        if(len(users)>0):
            user_name = input("请输入用户名：")
            if(user_name != "Q"):
                isOk = False
                for user in users:
                    if(user['userName'] == user_name):
                        user_pwd = input("请输入密码: ")
                        if(user_pwd != "Q"):
                            if(user['userPwd'] == user_pwd):
                                isOk = True
                            else:
                                print("密码错误！")
                        else:
                            print ("程序即将退出，再见！")
                            is_loop = False
                if(isOk):
                    print("欢迎 %s 回来" % (user_name))
                else:
                    print("用户不存在！请先注册")

            else:
                print ("程序即将退出，再见！")
                is_loop = False
        else:
            print("用户不存在！请先注册")
    elif(input_type == 2):
        new_user_name = input("请输入用户名：")
        if(new_user_name != "Q"):
            new_user_pwd = input("请输入密码: ")
            if(new_user_pwd != "Q"):
                new_user = {"userName": new_user_name, "userPwd": new_user_pwd}
                save_user(new_user)
            else:
                print ("程序即将退出，再见！")
                is_loop = False
        else:
            print ("程序即将退出，再见！")
            is_loop = False
    elif (input_type == "Q"):
        print ("程序即将退出，再见！")
        is_loop = False



