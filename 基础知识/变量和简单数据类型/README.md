## 变量命名和使用
```python
message = "hello world"
print(message)
```
添加一个名为message的变量，每个变量都指向一个值，这里的值是hello world
### 规则
1.变量名只包含字母，数字和下划线。以字母或下划线开头，不能以数字开头
2.变量名不能包含空格，但能用下划线来分隔其中的单词
3.不能使用关键字和函数名来用作变量名
4.变量名应简短并具有描述性
5.慎用小写字母l和大写字母O，与1和0具有混淆性
## 字符串
字符串就是一系列字符串。在python中，用引号括起来的都是字符串，引号可以是单引号或双引号
### 修改大小写

```python
name = "hello world"
print(name.title())
```
结果：Hello World
方法title()以首字母大写的方式显示每个单词
全部大写

```python
print(name.upper())
```
全部小写

```python
print(name.lower())
```
### 字符串中使用变量

```python
first_name="hello"
second_name="world"
full_name=f"{first_name} {second_name}"
print(full_name)
```
字符串中插入变量的值，要在前引号前加入字母f（format），再将要插入的变量放在花括号内
当python显示字符串时，把每个变量都替换为其值
### 使用制表符或换行符来添加空白
```python
print("\tHello")//制表符
print("language:\nC++\nJava\nPython")//换行符
```
也可同时使用制表符和换行符
字符串“\n\t”让python换到下一行了，并下一行开头添加一个制表符
### 删除空白
确保字符串末尾没有空白，使用rstrip()
```python
first_name.rstrip()
```
删除字符串开头的空白
lstrip（）
同时删除字符串两边的空白
strip（）
## 数
### 整数
直接加减乘除
**表示乘方运算
### 浮点数
所有带小数点的数
### 同时给多个变量赋值
x,y,z都初始化为0
```python
x,y,z = 0,0,0
```
## 结尾
解释器中输入import this
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210711190520778.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NjE4NTIx,size_16,color_FFFFFF,t_70)
