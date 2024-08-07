# 分支语句
# if-else语句
# for循环语句
# while循环语句

# 我们来看if的使用
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "admin" and password == "123456":
    print("登录成功！")
else:
    print("登录失败！")

score = int(input("请输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

id_code = input("请输入身份证号：")
if len(id_code) == 18:
    number = int(id_code[-2])
    if number % 2 == 0:
        print("女性")
    else:
        print("男性")
else:
    print("输入错误")

# while循环语句
count = 0
num = 0
while count < 100:
    count += 1
    num = num + count
print(num)

while True:
    num1 = int(input("请输入一个数字："))
    print("你输入的数字是：", num1)

# for循环语句
languages = ["C", "C++", "python", "Java"]
for x in languages:
    print("当前语言：", x)

for i in range(6):
    print("当前数字：", i)
for i in range(1, 3):
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(f"{i} x {j} = {i*j}".format(i,j), end="\t")


# 跳转语句
# break、continue、pass

# break语句
for s in "hello world":
    if s == "l":
        break
    print("当前字母", s)

# continue语句
for x in [0, -2, 5, 7, -10]:
    if x <= 0:
        continue
    print("当前数字", x)

# pass
if x <= 0:
    pass
