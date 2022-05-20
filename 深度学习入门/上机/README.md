# 上机一
要求：
1、实现给定要求的全连接神经网络，网络框架要求见图1；

2、利用1中构建的深度网络实现MNIST数据集识别（数据聚集已经提供，亦可直接下载）；

3、提交的作业：全部代码+代码说明文档+总结（包括最终实验结果截图，不少于800字）。

![](https://github.com/URLinkEVA/python-practiceCode/raw/main/Pic/4aff.jpg)

（该网络包括4个Affine仿射层，每一层的神经元个数分别为100，100，50，10；
3个ReLU激活层以及一个Softmax层，并采用Cross-Entropy Loss损失函数。
使用SGD迭代法更新网络参数。）

# 上机二
要求：
1、实现给定要求的卷积神经网络，网络框架要求见图2；

2、利用1中构建的深度网络实现MNIST数据集识别（数据聚集已经提供，亦可直接下载）；

3、提交的作业：全部代码+代码说明文档+总结（包括最终实验结果截图，不少于800字）。

![](https://github.com/URLinkEVA/python-practiceCode/raw/main/Pic/3con.jpg)

（该网络包括3个Convention卷积层；4个ReLU激活层；2个pooling池化层；2个Affine仿射层以及一个Softmax层，
采用Cross-Entropy Loss损失函数。注意，该网络中卷积层的卷积核的数量，大小，填充和步幅，池化层的窗口大小、步幅，
仿射层的神经元的个数等参数由自己决定，但需要在文档中给出每一层的参数说明。使用SGD迭代法更新网络参数。）
