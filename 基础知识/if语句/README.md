# 一个简单示例

```python
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```
输出结果：
Audi
BMW
Subaru
Toyota
# 条件测试
True/False
# if语句
if-elif-else结构

```python
age = 12
if age <4:
    price = 0
elif age < 18:
    price = 10
elif age > 60:
    price = 15
else:
    price = 20

print(f"your cost is ${price}")
```
