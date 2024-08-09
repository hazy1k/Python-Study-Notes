# 复习一下字符串
# python中的字符串是不可改变的，也就是说，一旦创建，就不能修改它的内容。

# 字符串的表示方法
# 1.普通字符串
a = "hello world"
# 2.原始字符串
s = r"hello\nworld"
# 3.长字符串
s = '''
hello
world
'''
print(s)

# 字符串与数字相互转换
# 1.字符串转数字
num = int("123")
print(num)
# 2.数字转字符串
c = str(True)
print(c)

# 格式化字符串
# 1.使用%运算符
name = '小李'
print("你好，我叫%s" % name)
# 2.format()方法
name1 = '小明'
age = 20
print('你好，我叫{}，今年{}岁'.format(name1, age))

pi = 3.1415926
print("圆周率的值为：{:.2f}".format(pi))

# 3.f-string
addr = 'china'
print(f"welcome to {addr}")
name2 = '小红'
age2 = 20
print(f"{name2}今年{age2}岁了")


# 字符串的操作
# 1.字符串的拼接
s1 = "hello"
s2 = "world"
s3 = s1 + s2
print(s3)
# 2.字符串的查找
print(s3.find("l"))
# 3.字符串替换
word = "hello world"
new_word = word.replace("world", "python")
print(new_word)
# 4.字符串切片
num = "1 2 3 4 5"
print(num.split())
print(num.split(',',2))
# 5.去除字符串两侧空格
text = "  hello world  "
print(text.strip())
text1 = "**strip*"
print(text1.strip('*'))
