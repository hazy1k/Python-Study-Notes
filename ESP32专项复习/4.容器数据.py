# 复习容器类型数据

# 序列类型：字符串、列表、元组、集合和字典
# 如何访问
a = "hello"
print(a[0])  # 'h'

# 加和乘操作
a = 'hello'
print(a+' world')
print(a*3)

# 切片操作
str = 'hello world'
print(str[0:2:1]) # 开始的位置：结束的位置：步长

# 成员测试
print('e' in str) # True
print('z' in str) # False

# 列表
# 列表是一种有序集合，可以存储任意类型的数据，可以随时添加或删除元素
# 创建列表
list_one = [] # 空列表
list_two = [1, 2, 3, 4, 5] # 整数列表
list_three = [1, 'a', '&', 2.3] # 不同类型元素的列表
# 我们还可以使用list()函数来创建列表
list_four = list([1, 2, 3, 4, 5])
print(list_one)
type(list_four) # <class 'list'>
# 添加元素
list_one.append(6)
print(list_one)
# 插入元素
names = ['张三', '李四', '王五']
names.insert(2, 'Jack')
print(names)
# 替换元素
names[0] = 'Tom'
print(names)
# 删除元素
del names[0]
print(names)
chars = ['a', 'b', 'c']
chars.remove('b')
print(chars)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers.pop(3))


# 元组
# 元组是不可变的列表，一旦创建就不能修改
# 创建元组
tuple_one = () # 空元组
tuple_two = (1, 2, 3, 4, 5) # 整数元组
tuple_three = (1, 'a', '&', 2.3) # 不同类型元素的元组
tuple_null = tuple()
print(tuple_null)
# 元组拆包
val = (10, 20)
a, b = val
print(a) # 10


# 集合
# 集合是无序的，不重复的元素的集合
# 创建集合
set_one = set([1, 2, 3, 4, 5])
print(set_one)
print(type(set_one))
# 使用frozenset()函数创建不可变集合
frozenset_one = frozenset([1, 2, 3, 4, 5])
print(frozenset_one)
print(type(frozenset_one))
# 修改集合
# 1.添加元素
set_one.add(6) # 一次只能添加一个元素
set_one.update([7, 8, 9]) # 可以一次添加多个元素
print(set_one)
# 2.删除元素
set_one.remove(8) # 删除指定元素
set_one.discard(7) # 删除指定元素，如果元素不存在，不会报错
set_one.pop() # 删除随机元素
print(set_one)
set_one.clear() # 清空集合


# 字典
# 字典是无序的键值对集合
# 创建字典
dict_one = {} # 空字典
student = {'张三': 100, '李四': 98, '王五': 45}
print(student)
dict_two = dict(name='Tom', age=20)
print(dict_two)
# 添加和修改字典元素
add_dict = {'name': 'Jack', 'age': 21}
dict_two.update(add_dict)
print(dict_two)
# 删除字典元素
del dict_two['age']
print(dict_two)
# 访问字典
info = {'001':'张三','002':'李四','003':'王五'}
print(info.items())
for i in info.items():
    print(i)
print(info.keys())
for i in info.keys():
    print(i)
print(info.values())
for i in info.values():
    print(i)
