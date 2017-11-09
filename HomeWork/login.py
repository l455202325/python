__author__ = "ZiXing"

info = '''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    欢迎进入Python登录系统      

  1.登录
  2.注册
  Q.退出
  H.帮助

┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛

'''
print(info)
msg = input("请按照指令输入：")
userList = []


isQ = ""
while isQ != "Q":
    if msg == "1":
        userName = input("请输入用户名：")
        pwd = input("请输入密码：")
        userList = open("userList","r",encoding="utf-8");
    elif msg == "2":
        userName = input("请输入用户名：")
        pwd1 = input("请输入密码：")
        pwd2 = input("请再次输入密码：")
    elif msg == "Q":
        isQ = "Q"
    elif msg == "H":
        print(info)
    else:
        print("指令无效")
