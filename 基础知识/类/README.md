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

```python
class Dog:
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

my_dog = Dog('goro',6)

print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
```
### 访问属性
要访问实例的属性，可使用句点表示法，例如以下访问my_dog的属性name的值

```python
my_dog.name
```
句点表示法在python中很常用，这种语法演示了python如何获悉属性的值。先找到实例my_dog，再查找与该实例相关联的属性name
### 调用方法
根据Dog类创建实例后，就能使用句点表示法来调用Dog类中定义的任何方法
```python
class Dog:
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

my_dog = Dog('goro',3)
my_dog.sit()
my_dog.roll_over()
```
要调用方法，可指定实例的名称和要调用的方法，并用句点分隔。遇到代码my_dog.sit(）时，python在类Dog中查找方法sit()并运行其代码

输出结果：
```python
goro is now sitting
goro rolled over
```
### 创建多个实例
可按需求根据类创建任意数量的实例。下面再创建一个名为your_dog的小狗实例：

```python
class Dog:
    --snip--

my_dog = Dog('goro',3)
your_dog = Dog('xina',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

# 使用类和实例
## Car类
下面来编写一个表示汽车的类。存储有关汽车的信息，还有一个汇总信息的办法：

```python
class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi','a7',2021)
print(my_new_car.get_descriptive_name())
```
第一个def定义了方法__init__()，与前面Dog类一样，这个方法的第一个形参为self，还包括三个形参：make.model和year。方法__init__这些形参的值，并将它们赋给根据这个类创建的实例的属性。创建新的Car实例时，需要指定其制造商，型号和年份。

第二个def定义了名为get_descriptive_name()的方法。它使用属性year,make和model创建一个对汽车进行描述的字符串，让我们无须分别打印每个属性的值。为在这个方法中访问属性的值，使用了self.make,self.model和self.year。

最后根据Car类创建了一个实例，并将其赋给变量my_new_car。接下来，调用方法get_descriptive_name()，指出我们拥有一辆什么样的车。

为了让这个类更有趣，下面给它添加一个随时间变化的属性，用于存储汽车的总里程
## 给属性指定默认值
创建实例时，有些属性无须通过形参来定义，可在方法__init__()中为其指定默认值

下面来添加一个名为odometer_reading的属性，其初始值总是为0，还添加一个名为read_odometer()的方法，用于读取汽车的里程碑。

```python
class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a7',2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```
## 修改属性的值
能以三种方式修改属性的值：直接通过实例进行修改，通过方法进行设置，以及通过方法进行递增（增加特定的值）
### 直接修改属性的值
要修改属性的值，最简单的方式是通过实例直接访问它。下面就是将里程表读数修改为23：

```python
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

### 通过方法修改属性的值
无须直接访问属性，将值传递给方法，由它在内部进行更新

```python
class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

my_new_car = Car('audi','a7',2021)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
添加了方法update_odometer()。这个方法接受一个里程值，并将其赋给self.odometer_reading。倒数第二行调用update_odometer()，并提供实参23.方法read_odometer()打印该读数。

可对方法update_odometer()进行拓展，使其在修改里程表读数时做些额外工作，下面来添加一些逻辑，禁止任何人将里程表读数往回调：

```python
class Car:
    __snip__

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
```
现在update_odometer()在修改属性前检查指定的读数是否合理
### 通过方法对属性的值进行递增

```python
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        """"将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_used_car = Car('subaru','outback','2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```
新增的方法increment_odometer()接收一个数，并将其加入self.odometer_reading中，然后创建一个二手车my_used_car，调用方法update_odometer()传入23500，再调用increment_odometer()并传入100，以增加多的100路程。

```python
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```
