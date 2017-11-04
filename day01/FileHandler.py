__author__ = "ZiXing"
# 文件操作

# 打开文件
# data = open("song", encoding="utf-8").read()

# 打开文件句柄，进行文件操作
# file = open("song", encoding="utf-8")  # 文件句柄
# data = file.read()
# print(data)


# 打开文件句柄，进行文件操作
# file = open("song", encoding="utf-8")  # 文件句柄
# data = file.read()
# data2 = file.read()
# print(data)
# print("data2", data2) # 文件读了一次后，第二次不能读到数据，因为第一次已经读到结尾了

# 以只读模式打开文件
# file = open("song", "r", encoding="utf-8")  # 文件句柄
# data = file.read()  # 文件可读
# print(data)
#
# file.writable("hello world!")  # 只读模式打开的文件不可写

# 以写的模式打开文件
# file = open("song2", "w", encoding="utf-8")
#
# file.write("hello\n")
# file.write("world!")

# 以追加的模式打开文件
# file = open("song2", "a", encoding="utf-8")
# # a = append 追加
#
# file.write("\npython is good!")
#
# file.close()


# file = open("song2", "a", encoding="utf-8")
# file.write("\nPython是世界上最好的语言")
# data = file.read()  # 以追加模式打开的文件只能写 不能读
# print(data)

# f = open("song", "r", encoding="utf-8");
# 土鳖方法读取前五行
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# 稍微不太土鳖的方法读取前五行
# for i in range(5):
#     print(f.readline())
'''
f = open("song", "r", encoding="utf-8")

# print(f.readlines())
for line in f.readlines():
    print(line.strip())

f.close()
'''

'''
f = open("song", "r", encoding="utf-8")
# 这个方式文件在内存里面有保存一行，效率最高
for line in f:
    print(line.strip())
'''

f = open("song", "r", encoding="utf-8")

print(f.tell())  # 获取文件当前“指针”的位置（字符数）
print(f.readline())
print(f.tell())

print(f.encoding)  # 文件编码格式
print(f.fileno())  # 文件编号

