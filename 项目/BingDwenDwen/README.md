# 玩转turtle
Turtle库是Python语言中一个很流行的绘制图像的函数库，可以想象一个小乌龟，从一个横轴为x、纵轴为y的坐标系**开始，它根据一组函数指令的控制，在这个平面坐标系中移动，从而在它爬行的路径上绘制了图形。而画出一个图像通常需要涉及到以下几个步骤：
## 1.设置画布(canvas)

指绘图区域，可以设置它的大小和初始位置。

设置画布大小
```python
turtle.screensize(canvwidth=None, canvheight=None, bg=None)
#参数分别为画布的宽(单位像素), 高, 背景颜色
```
如：
```python
turtle.screensize(800,600, "green")
turtle.screensize() #返回默认大小(400, 300)
```
## 2.设置画笔

在画布上，默认有一个坐标**为画布中心的坐标轴，坐标**上有一只面朝x轴正方向小乌龟，小乌龟其实就是我们的画笔。

可以设置画笔属性，比如颜色、画线的宽度等

1) turtle.pensize()：宽度；

2) turtle.pencolor()：没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。

3) turtle.speed(speed)：设置画笔移动速度，范围为0~10的整数，数字越大越快。

## 3.控制海龟移动绘制图形

使用turtle绘图的基本动作方法包括：forward（前进参数）、backward（后退参数）、left（左转角度）、right（右转角度）。库中内置了这些动作方法，因此在使用的时候直接调用并给定相应参数即可。当然还有别的一些常见操作命令，比如，turtle.circle()，半径为正(负)，表示圆心在画笔的左边(右边)画圆，turtle.penup()，提起笔移动，不绘制图形，用于另起一个地方绘制等等。
```python
turtle.forward(distance)
turtle.fd(distance)
#画笔向前移动distance距离

turtle.backward(distance)
turtle.back (distance)/ turtle.bk (distance)
#画笔向后移动distance距离

turtle.right(degree)
turtle.rt(degree)
#绘制方向向右旋转degree度

turtle.left(degree)
turtle.lt(degree)
#绘制方向向左旋转degree度

circle(50) # 整圆;
circle(50,steps=3) # 三角形;
circle(120, 180) # 半圆
```
## 4.色彩填充

turtle.fillcolor(colorstring)#绘制图形的填充颜色

fillcolor()：这有助于选择填充形状的颜色。它将输入参数作为颜色名称或颜色的十六进制值，并用所选颜色填充即将到来的封闭地理对象。颜色名称是基本颜色名称，即红色、蓝色、绿色、橙色。

颜色的十六进制值是十六进制数字的字符串（以'#'开头），即#RRGGBB。R、G 和 B 是十六进制数（0、1、2、3、4、5、6、7、8、9、A、B、C、D、E、F）。

begin_fill()：此函数告诉海龟所有即将关闭的图形对象都需要用所选颜色填充。

end_fill()：此函数告诉海龟停止填充即将关闭的图形对象。

### 简单示例：

绘制同心圆
```python
import turtle
t = turtle.Turtle()
# 初始半径
r = 10
# 循环画圆
for i in range(50):
t.circle(r * i)
t.up()
t.sety((r * i) * (-1))
t.down()
```
# 冰墩墩实现
将冰墩墩拆分成各个部分，然后在这个基础上再进行修改和微调。

用turtle画图，无非就是调整画笔颜色、画笔方向、抬笔、落笔、画圆、填充颜色、画直线等基本操作，啥都别说上来就是肝，没什么复杂逻辑，但也没有捷径，需要不断微调代码，保证最终出图和原始图案一致。

比如冰墩墩肚子上的五环：
```python
# 画出五环
t.penup() # 抬笔
t.goto(-25, -170) # 移至坐标
t.pendown() # 落笔
t.pencolor("blue")
t.circle(6) # 画圆
t.penup() t.goto(-10, -170)
t.pendown()
t.pencolor("black") # 设置画笔颜色
t.circle(6)
t.penup()
t.goto(5, -170)
t.pendown()
t.pencolor("brown")
t.circle(6)
t.penup()
t.goto(-18, -175)
t.pendown()
t.pencolor("lightgoldenrod")
t.circle(6)
t.penup()
t.goto(-4, -175)
t.pendown()
t.pencolor("green")
t.circle(6)
t.penup()
```
最后把所有的分解动作合到一个入口函数中,就完成了

完整代码在BingDwenDwen.py中
