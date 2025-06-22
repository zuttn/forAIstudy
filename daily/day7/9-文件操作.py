# 作者: 王道 龙哥
# 2025年06月03日11时18分01秒
# xxx@qq.com

def use_open_r():
    file = open('Readme', mode='r', encoding='utf8')
    txt = file.read()
    print(txt)
    file.close()


def use_open_r2():
    """
    使用r+,打开文件光标在文件开头
    :return:
    """
    file = open('Readme', mode='r+', encoding='utf8')
    txt = file.read()
    print(txt)
    file.write('HELLO')
    file.close()


def use_open_w():
    file = open('Readme', mode='w', encoding='utf8')
    file.write('hello')
    file.close()


def use_open_w2():
    # 相对路径
    file = open('dir1/Readme', mode='w+', encoding='utf8')
    file.close()


def use_open_a2():
    """
    使用a+,相对于r+，可以创建文件（如果文件不存在），打开后光标在文件末尾
    :return:
    """
    file = open('Readme', mode='a+', encoding='utf8')
    file.write('王道')
    file.close()


if __name__ == '__main__':
    # use_open_r()
    # use_open_r2()
    # use_open_w()
    # use_open_w2()
    use_open_a2()
