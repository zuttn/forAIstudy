"""
1、把上课写的飞机大战初始化窗口，绘制背景图，英雄的代码，事件机制写一下,写法与和上课一致
"""
import pygame

pygame.init()

# 创建游戏的主窗口，大小为480x700
screen = pygame.display.set_mode((480,700))

# 加载背景图片
background = pygame.image.load('../飞机大战项目/images/background.png')

# 把背景图片贴(blit)在窗口上，坐标为(0,0)
screen.blit(background,(0,0))

# 加载英雄
hero = pygame.image.load('../飞机大战项目/images/me_destroy_1.png')

# 把英雄贴在窗口上，坐标为(200,480)
screen.blit(hero,(200,480))

# 贴完更新窗口
pygame.display.update()

# 创建时钟对象，保证窗口更新频率
clock = pygame.time.Clock()

# 用于记录英雄的位置
hero_rect = pygame.Rect(200, 480, 102, 126)

# 设置死循环，让窗口一直保留，并在循环内监听窗口时间
while True:
    # 设置时钟， 让循环一秒执行60次
    clock.tick(60)

    # 1. 让背景重新变成（0，0）
    screen.blit(background,(0,0))
    # 2. 用hero_rect记录并操作hero的坐标
    screen.blit(hero,hero_rect)
    # 3. 贴完图更新窗口
    pygame.display.update()

    # 每次循环让英雄的y轴-1
    hero_rect.y -= 1

    # 判断英雄是否飞出屏幕
    if hero_rect.bottom <= 0:
        # 飞出屏幕后，把英雄的y轴换到屏幕底部
        hero_rect.y = 700

    # 添加监听事件，even_list 记录所有的事件
    even_list = pygame.event.get()
    if even_list:
        # print(even_list)
        for even in even_list:
            if even.type==pygame.QUIT:
                print('退出游戏')
                pygame.quit()
                exit(0)
            # 添加鼠标点击事件
            if even.type==pygame.MOUSEMOTION:
                bullet = pygame.image.load('../飞机大战项目/images/enemy1.png')
                screen.blit(bullet,(200,hero_rect.y))
                pygame.display.update()

pygame.quit()