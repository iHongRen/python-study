# 使用 Pillow 库处理图像

# Pillow 库提供了相当强大的图像处理功能。

# pip3 install pillow

from PIL import Image

# 加载图片
img = Image.open('avatar.png')
print(img)

# 图片名
print(img.filename) # avatar.png

# 图片格式
print(img.format) # PNG

# 图片格式描述
print(img.format_description) # Portable Network Graphics

# 图片尺寸
print(img.size) # (100, 100)
print(img.width) # 100
print(img.height) # 100

# 图片模式
print(img.mode) # RGB

# 图片相关数据
print(img.info) # {}


# 图片格式转换
img.save('avatar1.jpg')
img.save('avatar2.ico')

# 裁剪图片
crop = img.crop((0, 0, 50, 50))
crop.save('avatar3.png')

# 创建缩略图
crop.thumbnail((32, 32))
crop.save('avatar4.png')

# 修改尺寸
img2 = img.resize((50, 100))
img2.save('avatar5.png')

# 旋转图片
img3 = img.rotate(90)
img3.save('avatar6.png')

# 粘贴图片
img.paste(crop, (0, 0))
img.save('avatar7.png')

# 翻转图片
img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
img4.save('avatar8.png')


# ImageDraw 绘制
from PIL import ImageDraw

# 创建图片
img = Image.new('RGBA', (500, 500), 'white')

# 创建绘图对象
draw = ImageDraw.Draw(img)
print(draw)

# 画点
for i in range(0, 500, 20):
    draw.point((i, 50), 'red')

# 画线
draw.line((0, 80, 500, 80), 'red')
draw.line((0, 100, 500, 100), 'green')

# 画三角形
draw.polygon([(10, 200), (60, 120), (110, 200)], 'green')

# 画正方形
draw.rectangle((120, 120, 220, 220), 'blue')

# 画长方形
draw.rectangle((250, 120, 450, 200), 'blue', outline="red")

# 画椭圆
draw.ellipse((10, 250, 100, 400), 'green')

# 画圆
draw.ellipse((250, 250, 400, 400), 'green')

# 保存图片
img.save('avatar9.png')

img.close()


# ImageFont 字体
from PIL import ImageFont

# 加载字体
font = ImageFont.truetype("Arial.ttf", 20)

# 创建图片
img = Image.new('RGBA', (200, 200), 'white')

# 创建绘图对象
draw = ImageDraw.Draw(img)

# 绘制文本
draw.text((10, 10), 'Hello World', 'red', font)

# 保存图片
img.save('avatar10.png')



# ImageFilter 滤镜
from PIL import ImageFilter

img = Image.open('avatar.png')

# 模糊
img.filter(ImageFilter.BLUR).save('avatar11.png')

# 高斯模糊
img.filter(ImageFilter.GaussianBlur(radius=5)).save('avatar12.png')

# 轮廓
img.filter(ImageFilter.CONTOUR).save('avatar13.png')

# 边缘
img.filter(ImageFilter.EDGE_ENHANCE).save('avatar14.png')

# 深度边缘增强滤波，使得图像中边缘部分更加明显
img.filter(ImageFilter.EDGE_ENHANCE_MORE).save('avatar15.png')

# 浮雕
img.filter(ImageFilter.EMBOSS).save('avatar16.png')

# 找到边缘
img.filter(ImageFilter.FIND_EDGES).save('avatar17.png')


# ImageEnhance 图像增强
from PIL import ImageEnhance

img = Image.open('avatar.png')

# 亮度
enhancer = ImageEnhance.Brightness(img)
enhancer.enhance(2).save('avatar18.png')

# 对比度
enhancer = ImageEnhance.Contrast(img)
enhancer.enhance(2).save('avatar19.png')

# 锐度
enhancer = ImageEnhance.Sharpness(img)
enhancer.enhance(2).save('avatar20.png')

# 颜色
enhancer = ImageEnhance.Color(img)
enhancer.enhance(2).save('avatar21.png')


# 制作 gif
images = []
for i in range(11, 22):
    img = Image.open(f'avatar{i}.png')
    images.append(img)

# 保存
images[0].save("avatar.gif", save_all=True, append_images=images[1:])

