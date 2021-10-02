## 遍历整个列表
采用for循环

```python
cars = ['bmw','audi','toyota','subaru']
for car in cars:
    print(car)
```
for循环中执行更多操作
```python
cars = ['bmw','audi','toyota','subaru']
for car in cars:
    print(f"{car.title()},is a good choice")
```

## 创建数值列表
使用range()创建数字列表

```python
numbers=list(range(1,6))
print(numbers)
```
使用range（）时，还可指定步长
打印1~10的偶数

```python
even_numbers=list(range(2,11,2))
print(even_numbers)
```
将前十个整数的平方加入一个列表中

```python
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square) 
print(squares)
```
更简洁的写法

```python
squares=[]
for value in range(1,11):
    squares.append(value**2) 
print(squares)
```
统计计算


```python
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
```


列表解析

```python
squares=[value**2 for value in range(1,11)]
print(squares)
```
指定一个描述性的列表名squares
## 使用列表的一部分
处理列表的部分元素，称之为切片
要创建切片，要指定使用的第一个元素和最后一个元素的索引，与range（）一样，到达第二个索引之前的元素停止

```python
players=['charles','martina','michael','florence','eli']
print(players[0:3])
```
输出结果

```python
['charles', 'martina', 'michael']
```
没有指定第一个索引，默认从列表开头开始
要让切片终止于末尾
`print（players[2:]`）

复制列表

```python
cars=['a','b','c','d']
friend_cars=cars[:]
```

## 元组
创建一系列不可修改的元素，不可变的列表被称为元组
元组使用**圆括号**而非中括号来标识

```python
dimensions=(200,5)
print(dimensions[0])
print(dimensions[1])
```
遍历与列表一样
给元组变量重新赋值合法

## 设置代码格式
访问python网站搜索PEP8-style guide for python code，阅读PEP-8格式设置指南
