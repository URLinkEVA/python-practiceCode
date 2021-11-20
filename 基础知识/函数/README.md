# 定义函数
下面是一个打印问候语的简单函数，名为greet_user():

```python
def greet_user():
    print("hello")

greet_user()
```
关键词def是函数定义
## 向函数传递信息

```python
def greet_user(username):
    print("hello,{username.title()}!")

greet_user('kongla')
```
接收传递并输出
## 实参和形参
在函数greet_user()的定义中，变量username是一个形参，即函数完成工作所需的信息，在代码greet_user('kongla')中，值‘kongla’是一个实参，即调用函数时传递给函数的信息。

在greet_user('kongla')中，将实参‘kongla’传递给了函数greet_user()，这个值被赋给了形参username。
# 传递实参
传递函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方法很多：可使用位置实参，要求实参的顺序和形参的顺序相同；也可使用关键字实参，其中每个实参都是由变量名和值组成；还可使用列表和字典
## 位置实参
最简单的关联方式是基于实参的顺序

```python
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type} is called {pet_name.title()}.")

describe_pet('cat','sayu')
```
### 多次调用函数
要再描述一个，只需要再次调用describe_pet()
## 关键字实参
关键字实参是传递给函数的名称值对，在实参中将名称和值关联起来，向函数传递实参就不会混淆

```python
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type} is called {pet_name.title()}.")

describe_pet(animal_type='cat',pet_name='sayu')
```
**使用关键字实参时，务必准确指定函数定义中的形参名**

## 默认值
编写函数时，可给每个形参指定默认值。使用默认值可简化函数调用，还可清晰指出函数的典型用法

```python
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type} is called {pet_name.title()}.")

describe_pet(pet_name='sayu')
```
修改了·函数describe_pet()的定义，给形参animal_type()指定了默认值‘dog’，调用该函数时，如果没给animal_type指定值，python就会将这个形参设置为‘dog’
# 返回值
函数并非总是直接显示输出，还处理一些数据，并返回一个或一组值。函数返回的值成为返回值。在函数中，可使用return语句将值返回到调用函数的代码行。返回值能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
## 返回简单值

```python
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('pico','hendrix')
print(musician)
```
调用返回值的函数时，需要提供一个变量，以便将返回的值赋给它。上面代码是将返回值赋给了变量musician
## 返回字典
函数可返回任意类型的值，包括列表和字典等较复杂的数据结构

```python
def build_person(first_name,last_name):
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('pico', 'hendrix')
print(musician)
```
接下来拓展这个函数，使其接受可选值，如中间名，年龄，职业或其他任何要存储的信息

## 结合使用函数和while循环
结合使用函数get_formatted_name()和while循环

```python
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
```
while循环存在一个问题，没有定义退出条件，所以提示用户输入能进行break退出

```python
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
```

# 传递列表

```python
def greest_users(names):
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)

usernames = ['sayu','ayaka','paimo']
greest_users(usernames)
```
将greet_users()定义为接收一个名字列表，并将其赋给形参names。这个函数遍历收到的列表，并对其中的每位用户打印一句问候语，定义一个用户列表usernames，然后调用greet_users()并将列表传递给它。
## 在函数中修改列表

```python
# 创建要打印的列表
unprint_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

while unprint_designs:
    current_design = unprint_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

# 显示打印好的模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```
重新组织代码，编写两个函数提高效率，第一个函数处理负责打印设计的工作，第二个概述打印了哪些设计

```python
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\bThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designed = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
```
使用函数，这个程序更容易拓展和维护
## 禁止函数修改列表
要将列表的副本传递给函数

> function_name(list_name[:])

切片表示法[:]创造列表的副本
# 传递任意数量的实参
不知道函数需要接收多少个实参时，可以参考以下例子

```python
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
```
形参名*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中

现在将函数调用print()替换为一个循环，遍历列表进行描述

```python
def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
```
## 结合使用位置实参和任意数量实参
如果让函数接收不同类型的实参，必须将函数定义中将接纳任意数量实参的形参放在最后。python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个实参中。

例如前面的函数添加一个表示尺寸的形参，必须将其放在形参*toppings的前面

```python
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
```
## 使用任意数量的关键字实参

```python
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','sinstein',location='princeton',field='physics')
print(user_profile)
```
函数build_profile()的定义要求提供名和姓，同时允许根据需要提供任意数量的名称值对。形参**user_info中的两个星号让python创建一个名为user_info的空字典，并将收到的所有名称值对都放在这个字典中。
# 将函数储存在模块中
使用函数的优点之一是可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。还可更进一步，将函数储存在称为**模块**的独立文件中，再将模块**导入**到主程序中，import语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数储存在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上，还能在众多不同的程序中重用函数。知道如何导入函数还能让你使用别人编写的函数库。
## 导入整个模块
要让函数是可导入的，得先创造模块。下面来建造一个包含函数make_pizza()的模块：
pizza2.py
```python
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
```
然后在这个文件所在的目录中创建一个文件，这个新文件导入刚创建的模块，再调用make_pizza()两次

```python
import pizza2

pizza2.make_pizza(16,'pepperoni')
pizza2.make_pizza(12,'mushrooms','green peppers','extra cheese')
```
只需编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数
## 导入特定的函数
还可以导入模块中的特定函数，这种导入方式的语法如下：

```python
form module_name import function_name
```
通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

```python
form module_name import function_0,function_1,function_2
```
对于前面的making_pizzas.py示例，如果只想导入其中要使用的函数，代码类似如下：

```python
from pizza2 import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
```
## 使用as给函数指定别名
函数名称冲突或者太长，可指定简短且独一无二的别名，通用语法如下：

```python
form module_name import function_name as fn
```

## 使用as给模块指定别名
给模块指定简短的别名，能更轻松的调用模块中的函数，通用语法如下：

```python
import module_name as mn
```
## 导入模块中的所有函数
使用星号（*）运算符可让python导入模块中的所有函数

```python
from module_name import *
```
import语句中的星号让模块中的每个函数都复制到这个程序文件中
# 函数编写指南
# 小结
