@[TOC]
# 函数input()的工作原理
函数input()让程序暂停运行，等待用户输入一些文本

```python
message = input("repeat back:")
print(message)
```
## 编写清晰的程序

```python
name = input("please input your name: ")
print(f"\nHello,{name}!")
```
在提示末尾包含一个空格，可将提示与用户输入分开

```python
prompt = "just the first line"
prompt += "\nYour name："

name = input(prompt)
print(f"\nHello,{name}!")
```
采用创建多行字符串的方式，第一行把消息的前半部分赋给变量prompt中，在第二行中。运算符+=在前面变量prompt的字符串末尾附加一个字符串
## 使用int()来获取数值输入
使用函数input()时，python将用户输入解读为字符串
![在这里插入图片描述](https://img-blog.csdnimg.cn/5edc35e3dbad4fa08b8818d63b12925c.png)
将输入用于数值比较时会报错，因为无法将字符串和整数类型进行比较
可以使用函数int()

```python
age = int(age)
```
## 求模运算符
%将两数相除并返回余数，如果被整除，余数就是0，所以可以用来判断一个数是奇数还是偶数

```python
number = input("enter a number: ")
number = int(number)

if number %2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

# while循环简介
for循环用于针对集合中的每个元素都执行一个代码块，while循环是不断运行，直到指定的条件不满足为止
## 使用while循环
可使用while循环来数数
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
```
## 选择何时退出
在程序中定义一个退出值

```python
prompt = "just the first line"
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```
不足处：将quit也打印出来了
增加一个简单的if测试

```python
prompt = "just the first line"
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quir':
        print(message)
```
## 使用标记
有多个事件导致程序结束，一条while语句检查所有条件显然复杂。可以定义一个变量，称之为标志(flag)

```python
prompt = "just the first line"
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```
简化了while语句，在任意一个事件导致活动标志变成false时程序将结束
## 使用break退出循环

```python
prompt = "--------------------"
prompt += "\n(Enter 'quit' to end the program: )"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"i love go to {city.title()}!")
```

## 在循环中使用continue
返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue

```python
current_number = 0
while current_number < 10:
    current_number+=1
    if current_number %2 == 0:
        continue

    print(current_number)
```
## 避免无限循环
程序陷入无限循环时，ctrl+C，或者手动关闭显示的终端窗口。
为了避免编写无限循环，务必对每个while循环进行测试，确保按预期结束，确保程序至少有一个地方能让循环条件为false，或者让break得以执行
# 使用while循环处理列表和字典
## 在列表之间移动元素

```python
uncon_users = ['klee','pimon','sayo']
con_users = []

# 进行验证
while uncon_users:
    current_users = uncon_users.pop()

    print(f"verifying user:{current_users.title()}")
    con_users.append(current_users)

# 显示已验证的
print("\nThe following users have been confirmed:")
for con_user in con_users:
    print(con_user.title())
```
## 删除为特定值的所有列表元素
之前用remove()只删除了一次特定值，要删除所有为特定值的元素，需要进行一个while循环

```python
pets = ['dog','cat','dog','goldfish','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```
## 使用用户输入来填充字典

```python
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nName: ")
    response = input("which mountain: ")

    # 将回答存储在字典中
    responses[name] = response

    # 看是否有人要参与
    repeat = input("Anyone? (yes/ no)")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- poll result ---")
for name,response in responses.items():
    print(f"{name} would you like to climb {responses}.")
```
