# 操作流程
将mp4视频转化为用字符串表示的形式进行放

# 案例实现原理
众所周知，每段视频是由一帧帧图像构成，Opencv处理视频图像信息的原理就是将视频转为一帧帧的图像，将图像帧根据需求进行处理后，再将图像帧处理转换为视频，即可达到处理视频的目的。

本案例的实现原理也是基于上述，我们将需要处理的视频准备好了后，利用Python的一系列库函数如Opencv，将视频转换为一批帧图像，再通过代码函数对帧图像的像素进行处理，将其转换为字符串，最后将所有处理好的帧图像转换为视频进行播放，即可达到视频处理的目的。

本案例的实现过程主要分为以下几步
- 导入库函数；
- 将视频转化为图像帧；¶
- 对图片帧进行ASCII码的转换；
- 将转换好的图片帧合成视频；

# 案例实现代码
## 导入库函数
```
#导入Python库
import cv2
from PIL import Image,ImageFont,ImageDraw
import os
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
```
## 将视频转化为图像帧
```
#将视频转换为图片存入目标文件夹
def video_to_pic(vp):
    number = 0
    if vp.isOpened():
        r,frame = vp.read()
        if not os.path.exists('cache_pic'):
            os.mkdir('cache_pic')
        os.chdir('cache_pic')
    else:
        r = False
    while r:
        number += 1
        cv2.imwrite(str(number)+'.jpg',frame)
        r,frame = vp.read()
    print('\n由视频一共生成了{}张图片！'.format(number))
    os.chdir("..")
    return number
```

## 对图片帧进行ASCII码的转换
```
#将图片进行批量化处理
def star_to_char(number, save_pic_path):
    if not os.path.exists('cache_char'):
        os.mkdir('cache_char')

    # 生成目标图片文件的路径列表
    img_path_list = [save_pic_path + r'/{}.jpg'.format(i) for i in range(1, number + 1)]
    task = 0

    for image_path in img_path_list:
        # 获取图片的分辨率
        img_width, img_height = Image.open(image_path).size
        task += 1

        #处理图片
        img_to_char(image_path, img_width, img_height, task)
        print('{}/{} is processed.'.format(task, number))
    print('=======================')
    print('All pictures were processed!')
    print('=======================')
    return 0

# 将图片转换为灰度图像后进行ascii_char中的ASCII值输出
def get_char(r, g, b, alpha=256):
    ascii_char = list("#RMNHQODBWGPZ*@$C&98?32I1>!:-;. ")
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / len(ascii_char)
    return ascii_char[int(gray / unit)]


def img_to_char(image_path, raw_width, raw_height, task):
    width = int(raw_width / 6)
    height = int(raw_height / 15)

    # 必须以RGB模式打开
    im = Image.open(image_path).convert('RGB')
    im = im.resize((width, height), Image.NEAREST)

    txt = ''
    color = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))

            # 将颜色加入进行索引
            color.append((pixel[0], pixel[1], pixel[2]))
            if len(pixel) == 4:
                txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
            else:
                txt += get_char(pixel[0], pixel[1], pixel[2])
        txt += '\n'
        color.append((255, 255, 255))

    im_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255))
    dr = ImageDraw.Draw(im_txt)
    font = ImageFont.load_default().font
    x, y = 0, 0
    font_w, font_h = font.getsize(txt[1])
    font_h *= 1.37  # 调整字体大小
    for i in range(len(txt)):
        if (txt[i] == '\n'):
            x += font_h
            y = -font_w
        dr.text((y, x), txt[i], fill=color[i])
        y += font_w
    os.chdir('cache_char')
    im_txt.save(str(task) + '.jpg')

    #直接进入新创建的文件夹将生成的图片直接存入文件夹中
    os.chdir("..")
    return 0
```

## 将转换好的图片帧合成视频
```
# 进度条显示
def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join("■ " * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
    print(bar, end='', flush=True)


def jpg_to_video(char_image_path, FPS):
    # 设置视频编码器,这里使用MP42编码器
    video_fourcc = VideoWriter_fourcc(*"MP42")

    # 生成目标字符图片文件的路径列表
    char_img_path_list = [char_image_path + r'/{}.jpg'.format(i) for i in range(1, number + 1)]

    # 获取图片的分辨率
    char_img_test = Image.open(char_img_path_list[1]).size
    if not os.path.exists('video'):
        os.mkdir('video')
    video_writter = VideoWriter('video/output.avi', video_fourcc, FPS, char_img_test)
    sum = len(char_img_path_list)
    count = 0
    for image_path in char_img_path_list:
        img = cv2.imread(image_path)
        video_writter.write(img)
        end_str = '100%'
        count = count + 1
        process_bar(count / sum, start_str='', end_str=end_str, total_length=15)

    video_writter.release()
    print('\n')
    print('=======================')
    print('The video is finished!')
    print('=======================')
```

## 主函数
```
if __name__ == '__main__':
    #初始视频路径
    video_path = 'test_demo0510.mp4'
    #原始视频转为图片的图片保存路径
    save_pic_path = 'cache_pic'
    #图片经处理后的图片保存路径
    save_charpic_path = 'cache_char'

    # 读取视频
    vp = cv2.VideoCapture(video_path)

    # 将视频转换为图片 并进行计数，返回总共生成了多少张图片
    number = video_to_pic(vp)

    # 计算视频帧数
    FPS = vp.get(cv2.CAP_PROP_FPS)

    # 将图像进行字符串处理后
    star_to_char(number, save_pic_path)

    vp.release()

    # 将图片合成为视频
    jpg_to_video(save_charpic_path, FPS)
```

