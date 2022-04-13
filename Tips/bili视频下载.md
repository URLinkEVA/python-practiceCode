# 缘由
bilibili下载助手和bilibilijj都挂了，遇到版权保护视频直接不给下载

# you-get
cmd使用命令下载
```
pip install -U you-get
```
# 使用
例如下载个视频

原链接
```
https://www.bilibili.com/video/BV1Y3411J7rX?spm_id_from=333.999.0.0
```
观察网址，然后把?后面的字符串都删掉，不然可能会报一些奇怪的错误，删除后如下
```
https://www.bilibili.com/video/BV1Y3411J7rX
```
然后使用如下命令
```
you-get "https://www.bilibili.com/video/BV1Y3411J7rX"
```
加不加""应该都行

会在下载路径看到两文件，一个是xml，B站的视频弹幕，可以用工具将它转换为ass格式导入到播放器中。
