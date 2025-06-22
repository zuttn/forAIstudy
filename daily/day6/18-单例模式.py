# 作者: 王道 龙哥
# 2025年06月02日16时46分56秒
# xxx@qq.com

class MusicPlayer:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 给对象申请空间
        return cls.instance

    def __init__(self):
        print('音乐播放器初始化')


player1 = MusicPlayer()
player2 = MusicPlayer()
pass
