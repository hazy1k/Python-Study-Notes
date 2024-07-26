# 第四章 self

```python
# 学习python中的self

# 1.self会在定义方法的时候自动填写上
# 2.self往往指向自己，即谁调用的方法，那么这个方法中的self就指向谁
# xx.test() 那么执行test实例方法中self就指向xx指向的对象

class Dog(object):
    def set_name(self, name):
        self.name = name
    def print_name(self):
        print("My name is %s" % self.name)

black = Dog()
black.set_name("小黑")
black.print_name() # My name is 小黑

# 以上代码中，我们定义了一个Dog类，里面有两个方法，set_name和print_name。
# 其中set_name方法用来设置对象的名字，print_name方法用来打印对象的名字。
# 我们创建了一个Dog类的实例对象black，并调用了set_name方法设置了它的名字为"小黑"。

```


