# 作者: 王道 龙哥
# 2025年06月03日14时57分37秒
# xxx@qq.com
import os
def use_readline():
    file = open('Readme', encoding='utf8')
    while True:
        txt = file.readline()
        if txt:
            print(txt, end='')
        else:
            break
    file.close()


def use_read():
    file = open('Readme', encoding='utf8')
    while True:
        txt = file.read(5)  # 5代表5个字符，汉字算1个
        if txt:
            print(txt, end='')
        else:
            break
    file.close()

def use_seek():
    """
    文本模式使用seek
    :return:
    """
    file = open('Readme', mode='r', encoding='utf8')
    file.seek(10,os.SEEK_SET) #偏移是字节
    txt=file.read()
    print(txt)
    file.close()

def use_rb():
    """
    使用二进制打开图片文件
    :return:
    """
    file=open('test1.png', mode='rb')
    file_write=open('test2.png', mode='wb')
    png_bytes=file.read()
    file_write.write(png_bytes)
    file.close()

def use_rb2():
    """
    使用二进制打开文本文件
    :return:
    """
    file=open('Readme', mode='r', encoding='utf8')
    txt_bytes=file.read()
    file.close()

if __name__ == '__main__':
    # use_readline()
    # use_read()
    # use_seek()
    # use_rb()
    use_rb2()