# 压缩字体文件
# 原理就是挑出一些必要的字符，然后生成一个新的字体文件

# pip3 install fonttools

from fontTools import subset

def compressFont(fontFile, charset):
    # 加载字体文件
    font = subset.load_font(fontFile, subset.Options())
    setter = subset.Subsetter()
    setter.populate(text=charset) 
    setter.subset(font)
    # 保存字体
    subset.save_font(font, 'output.ttf',subset.Options())



if __name__ == '__main__':

    # 定义需要包含的字符，比如我们有时只需要数字和英文字母
    include_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    # 从txt文件里加载常用字符
    # include_chars = open('常用字.txt', 'r', encoding='utf-8').read()

    # 压缩字体, 指定要包含的字符
    compressFont('myFont.ttf', include_chars)
