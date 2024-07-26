# 第五章 __init__方法

```python
# 下面学习__init__方法的使用

class MacBook(object):
    def __init__(self, cpu="M1", ram="32GB", screen="Retina"):
        self.cpu = cpu
        self.ram = ram
        self.screen = screen

    def print_info(self):
        print("当前电脑的配置是：", self.cpu, self.ram, self.screen)

my_mac_book = MacBook()
my_mac_book.print_info()

my_mac_book2 = MacBook("M2", "64GB", "OLED")
my_mac_book2.print_info()
```


