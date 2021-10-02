列表是一系列按特定顺序排列的元素组成，python中用【】表示列表，用逗号分隔其中的元素
## 访问列表元素
列表是有序合集，想访问要得到该元素的位置（索引）

```python
bicycles = ['Trek','cannondale','redline','specialized']
print(bicycles[0])
```
从列表提取第一个元素
索引从0开始
## 修改，添加和删除元素
### 修改列表元素
与访问列表元素语法类似，指定列表名和要修改的元素的索引，再指定该元素的新值
### 添加元素
末尾添加append，不影响列表中其他元素

```python
bicycles.append('pico')
print(bicycles)
```
在任意位置添加insert，需要指定新元素的索引和值

```python
bicycles = ['Trek','cannondale','redline','specialized']

bicycles.insert(0,'pico')
print(bicycles)
```
值’pico‘被插入到列表开头，方法insert（）在索引0处添加空间，并将值储存到这个地方，这种操作使列表中既有的每个元素都右移一个位置
### 删除元素
#### 使用del语句

```python
bicycles = ['Trek','cannondale','redline','specialized']

del bicycles[0]
print(bicycles)
```
删除列表bicycles中的第一个元素‘Trek’
#### 使用pop语句
方法pop（）删除列表末尾的元素，并能够接着使用它

```python
bicycles = ['Trek','cannondale','redline','specialized']

poped_bicycles = bicycles.pop()
print(bicycles)
print(poped_bicycles)
```
实际上pop可以删除任意位置的元素，只需要在括号内指定要删除元素的索引

```python
bicycles = ['trek','cannondale','redline','specialized']

bicycles_sold = bicycles.pop(0)
print(f"the sold is the {bicycles_sold.title()}")
```
#### 根据值删除元素

```python
bicycles = ['trek','cannondale','redline','specialized']

bicycles.remove('trek')
print(bicycles)
```
## 组织列表
### 使用sort（）对列表永久排序

```python
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted ilst:")
print(sorted(cars))

cars.sort()
print(cars)
```
按与字母顺序相反的顺序排序

```python
cars.sort(reverse=True)
```
修改是永久性的
