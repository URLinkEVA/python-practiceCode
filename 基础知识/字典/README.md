@[TOC]
# 一个简单的字典

```python
ailen_0 = {'color':'green','point':5}

print(alien_0['color'])
print(alien_0['points'])
```
字典alien_0存储了外星人的颜色和分数
# 使用字典
**字典**是一系列**键值对**，与键相关联的值可以是数，字符串，列表或者字典
在python中，字典用放在花括号（{}）中的一系列键值对表示
**键值对**是对两个相关联的值。指定键时，将返回到与之相关联的值，键和值之间用冒号分隔，键值对之间用逗号分隔
## 访问字典中的值
## 添加键值对

```python
alien_0['x_position'] = 0
alien_0['y_position'] = 0
```
新增两个键值对
## 修改字典中的值

```python
alien_0 = {'color':'green'}
print(f"the alien is {alien_0['color']}.")

alien_0['color' = 'yellow']
print(f"the alien is now {alien_0['color']}.")
```
修改‘color’相关联的值改为‘yellow’
## 删除键值对
使用del语句，必须指定字典名和要删除的键

```python
alien_0 = {'color': 'green' , 'points':5}
del alien_0['points']
```
## 由类似对象组成的字典

```python
fav_lan = { 
	'jan':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

language = fav_lan['sarah'].title()
print(f"sarah favorite language is {language}.")
```
## 使用get()来访问值
从字典中访问指定的键不存在时会报错
显示traceback
所以采用方法get()在指定的键不存在时返回一个默认值

```python
alien_0 = {'color':'green','speed':'slow'}

point_value = alien_0.get('points','no point value assiged.')
print(point_value)
```
输出结果：no point value assiged.

# 遍历字典
## 遍历所有键值对
采用for循环

```python
user = {
	'username':'efermi',
	'first':'enrico',
	'last':'femi',
	}

for key,value in user.items():
	print(f"\nKey:{key}")
	print(f"Value:{value}")
```
输出结果

```python
Key:username
Value:efermi

Key:first
Value:enrico

Key:last
Value:femi
```

## 遍历字典中所有值
在不需要使用字典中的值时，方法keys()很有用

```python
fav_lan = { 
	'jan':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name in fav_lan.keys():
	print(name.title())
```
最后倒数第二行也可写成
for name in fav_lan：
输出不变
## 按特定顺序遍历字典中的所有键
在for循环中对返回的值进行排序，使用函数sorted()来获得按特定顺序排列的键列表的副本

```python
fav_lan = { 
	'jan':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for name in sorted(fav_lan.keys()):
	print(f"{name.title()},thank you for taking the poll.")
```
sorted()采用ASCII码比较，第一个字符相同就比较下一个
## 遍历字典中的所有值
使用方法values()来返回一个值列表，不包含任何键

```python
fav_lan = { 
	'jan':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for language in fav_lan.values():
	print(language.title())
```
剔除重复项，可使用集合set，集合中的每个元素都必须是独一无二的

```python
fav_lan = { 
	'jan':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for language in set(fav_lan.values()):
	print(language.title())
```
### 更简单的用法

```python
languages = {'python','ruby','c','python'}
languages
{'python','ruby','c'}
```
# 嵌套
将一系列字典存储在列表中，或将列表组作为值存储在字典中，称之为嵌套
## 字典列表
创建包含三个alien的列表

```python
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
```
现实情况，alien不止三个，如下面用range()生成30个相同特征的alien

```python
# 创建一个存储空列表
aliens = []

# 创建30个
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前五个
for alien in aliens[:5]:
    print(alien)

# 显示创建了多少个
print(f"total number of aliens:{len(aliens)}")
```
修改一些数据

```python
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] == 'red'
        alien['speed'] == 'fast'
        alien['points'] = 15
```

## 在字典中存储列表
有时需要将列表存储在字典中

```python
# 存储所点披萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

# 概述所点的披萨
print(f"you ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
```
为打印配料，编写一个for循环。为访问配料列表，使用键‘toppings’

每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表

```python
fav_lan = { 
	'jan':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
	}

for name,languages in fav_lan.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
```
现在与每个名字相关联的值都是一个列表，在遍历字典的主循环中，使用了另一个for循环来遍历每一个人喜欢的语言列表
## 在字典中存储字典
代码会很复杂

```python
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princetion',
    },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")
```
首先定义一个user字典，包含两个键‘aeinstein’，‘mcurie’
与每个键相关联的值都是一个字典，然后遍历users，接着开始访问内部字典，变量user_info包含用户信息字典
