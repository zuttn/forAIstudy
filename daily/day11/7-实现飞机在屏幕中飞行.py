# 作者: 王道 龙哥
# 2025年06月07日09时46分55秒
# xxx@qq.com
import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("飞机大战项目/images/background.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))
# 3> update 更新屏幕显示
pygame.display.update()

hero = pygame.image.load('飞机大战项目/images/me1.png')
#  绘制英雄
screen.blit(hero, (200, 500))
#  更新屏幕显示
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 初始化矩形窗口
hero_rect = pygame.Rect(200, 500, 102, 126)

while True:
    clock.tick(60)
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:  # 判断飞机是否飞出屏幕
        hero_rect.y = 700  # 飞机飞出屏幕后，重新设置飞机位置

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

    event_list = pygame.event.get()
    if event_list:
        print(event_list)  # 键盘鼠标等事件，都已经设计好了
        for event in event_list:
            if event.type == pygame.QUIT:
                print("游戏退出")
                pygame.quit()
                exit(0) #进程终止
pygame.quit()

