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
# 传递任意数量的实参
# 将函数储存在模块中
## 导入整个模块
## 导入特定的函数
# 函数编写指南
# 小结
