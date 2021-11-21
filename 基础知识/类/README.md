# 创建和使用类
## 创建Dog类
根据Dog类创建的每个实例都将存储名字和年龄，赋予每只小狗蹲下（shit()）和打滚（roll_over()）的能力：

```python
class dog:
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """"模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """"模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over")
```
首先定义一个Dog的类，根据约定，在Python中首字母大写的名称指的是类，这个类定义中没有圆括号，因为要从空白创建这个类。
### 方法__init__()
类中的函数称为方法，在这个方法的名称中，开头和末尾各有两个下划线，这也是一个约定，旨在避免python默认方法与普通方法发生名称冲突。

将方法__init__定义成包含三个形参:self,name和age。创建Dog实例时，自动传入实参self。每个与实例相关联的方法调用都自动传递实参self，它是一个指向实力本身的引用，让实例能够访问类中的属性和方法。
## 根据类创建实例
