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
# 继承
编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可用继承。一个类继承另一个类时，将自动获得另一个类的所有属性和方法。原有的类称为父类，而新类称为子类。子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。
## 子类的方法__init()__
在既有类的基础上编写新类时，通常要调用父类的方法__init__()。这将初始化在父类__init__()方法中定义的所有属性，从而让子类包含这些属性。

```python
class Car:
    """一次模拟汽车的简单尝试"""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
```
创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在圆括号内指定父类的名称。方法__init__()接受创建Car实例所需的信息。

super()是一个特殊函数，能够调用父类的方法。也称为超类。

倒数第二行创建ElectricCar类的一个实例，并将其赋给变量my_tesla。这行ElectricCar类调用定义的方法__init__()，后者调用父类Car中定义的方法__init__()。

除方法__iniy__()外，ElectricCar没有其他特有的属性和方法。
## 给子类定义属性和方法
让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。
下面添加一个电瓶属性：

```python
class Car:
    """一次模拟汽车的简单尝试"""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```
添加了新属性self.battery_size，并设置初始值为75.还添加了一个describe_battery()的方法，打印有关电瓶的信息。
## 重写父类的方法
对于父类的方法，只要它不属于子类模拟的实物的行为，都可以进行重写。可以在子类中定义一个与要重写的父类方法同名的方法。这样python就不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

假设Car类有一个名为fill_gas_tank()的方法，对电动车毫无意义，下面演示一种重写方法：
```python
class ElectricCar(Car):
	--snip--

    def fill_gas_tank(self):
        """电动车没有邮箱，混合电动除外"""
        print("This car doesn't need a gas tank!")
```

## 将实例用作属性
使用代码模拟实物时，会发现给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，需要将类的一部分提取出来，作为一个独立的类。可以将大型类拆分成多个协同工作的小类。

例如不断给ElectricCar类添加细节时，会发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下，可将这些属性和方法提取出来，放到一个名为Battery的类中，并将一个Battery实例作为ElectricCar类的属性：

```python
class Car:
    --snip--

class Battery:
    """"模拟电瓶"""

    def __init__(self,battery_size=75):
        """初始化电瓶的属性""" 
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """电动车独特之处"""

    def __init__(self,make,model,year):
        """初始化"""
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s','2019')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```
定义一个Battery的新类，没有继承任何类

在ElectricCar类中，添加了一个名为self.battery的属性，让python创建了一个新的battery实例（因为没有指定容量，所以为默认值75），并将该实例赋给属性self.battery。每当方法__init__()被调用时，都将执行该操作，所以现在每个ElectricCar实例都包含一个自动创建的Battery实例。

再给Battery添加一个方法，将根据电瓶容量报告汽车的续航里程：

```python
class Car:
    --snip--

class Battery:
    --snip--

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    --snip--

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
新增方法get_range()做一个简单的比较分析
# 导入类
将类存储在模块中，在主程序中导入所需的模块
## 导入单个类
下面来创建一个只包含Car类的模块。

```python
"""一个可用于表示汽车的类"""
class Car:

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """指出汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
```
下面来创建另一个文件my_car.py，在其中导入Car类并创建其实例：

```python
from car import Car

my_new_car = Car('audi','a7','2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
输出结果：

```python
2019 Audi A7
This car has 23 miles on it.
```

## 在一个模块中存储多个类
根据需求在一个模块中存储任意数量的类。Battery类和ElectricCar类都可帮助，下面都加入模块car.py中：

```python
"""一个可用于表示汽车的类"""
class Car:

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """指出汽车的里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值，禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery:
    """"模拟电瓶"""

    def __init__(self,battery_size=75):
        """初始化电瓶的属性""" 
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动车独特之处"""

    def __init__(self,make,model,year):
        """初始化"""
        super().__init__(make,model,year)
        self.battery = Battery()
```
新建一个名为my_electric_car.py的文件，导入ElectricCar类，并创建一辆电动车：

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla','model s',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
输出与之前相同，但大部分逻辑隐藏在一个模块中：

```python
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

## 从一个模块中导入多个类
可根据需要在程序文件中导入任意数量的类。如果要在同一个程序中创建普通与电动。就需要将Car类和ElectricCar类都导入。
```python
from car import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
```
从一个模块导入多个类时，用逗号分隔了各个类。导入必要的类后，就可根据需要创建每个类的任意数量实例。

输出结果：

```python
2019 Volkswagen Beetle
2019 Tesla Roadster
```

## 导入整个模块
导入整个模块，再使用句点表示法访问需要的类

```python
import car

my_beetle = car.Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
```
导入整个car模块，然后使用语法module.name.ClassName访问需要的类
## 导入模块中的所有类

```python
from module_name import * 
```
不推荐使用这种导入方式
## 在一个模块中导入到另一个模块
有时候需要将类分散到多个模块中，以免模块太大或在同一个模块中存储不相关的类。将类存储在多个模块中时，会发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。

下面将Car类存储在一个模块中，并将Battery类和ElectricCar类存储在另一个模块中
```python
from car import Car
    
class Battery:
    --snip--

class ElectricCar(Car):
	--snip--
```
ElectricCar类可以访问其父类Car
## 使用别名
导入类时，可指定别名
比如反复输入ElectricCar，可以替换为EC

```python
from electric_car import ElectricCar as EC
```
每当需要创建电动车实例时，都可使用这个别名

```python
my_tesla = EC('tesla','model s',2019)
```

## 自定义工作流程
一开始应让代码结构尽可能简单。萌新先尽可能在一个文件中完成所有的工作，确定一切都能正常运行后，再将类移到独立的模块中。后期需要模块和文件的交互方式，可以在项目开始时就尝试将类存储到模块中。
# python标准库
python标准库是一组模块，这是别人编写好的，只需在程序开头包含一句简单的import语句即可，例如下面的两个函数：randint()和choice()

```python
from random import randint
print(randint(1,6))
```

```python
from random import choice
players = ['Barbara','Klee','Dliuc','Jean','Sucrose','Venti','Amber']
first_up = choice(players)
print(first_up)
```
还可以从其他地方下载外部模块，例如后期的cv2，matplotlib，numpy
[下载参考文章](https://blog.csdn.net/qq_45618521/article/details/121461399)
# 类编码风格
类名应采用驼峰命名法，即类名中的每个字母的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加下划线。

对于每个类，都应紧跟在类定义后面包含一个文档字符串，这种文档字符串需要简要描述类的功能，并遵循编写函数的文档字符串时采用的格式约定，每个模块也一样。
