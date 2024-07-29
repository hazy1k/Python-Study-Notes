# 第十二章 super

```python
# 学习super
# 重写时候，可以用super()来调用父类的方法，这样可以避免重复的代码。

class Father(object):
    def play_game(self):
        print("父类的方法，玩魂斗罗")


    def drink(self):
        print("父类的方法，喝酒")


class Son(Father):
    def play_game(self):
        super().play_game()
        print("儿子的方法，玩游戏")

son = Son() # 创建儿子对象
son.play_game() # 调用儿子的方法的同时，会调用父类的同名方法
son.drink() # 调用父类的方法

```


