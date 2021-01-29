# 开发贪吃蛇游戏

import pygame
import sys
import random
from pygame.locals import *


# 1 定义颜色变量 rgb 0-255  000黑色，255 255 255 白色
redColor = pygame.Color(255,0,0) # 目标方块
whiteColor = pygame.Color(255,255,255) #贪吃蛇
blackColor = pygame.Color(0,0,0)    # 背景



# 2 定义游戏结束函数
def gameover():

    pygame.quit()
    sys.exit()

# 3实现工作方式
def main():

    pygame.init()    # 初始化pygame各模块

    # 定义一个变量控制游戏速度
    fpsClock = pygame.time.Clock()
    # 定义一个窗口
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("贪吃蛇")


    # 初始化变量
    # 贪吃蛇起始位置
    snakePosition = [100,100]
    #贪吃蛇长度
    snakeBody = [[100,100],[80,100],[60.100]]
    # 目标方块位置
    targetPosition = [300,300]
    # 定义一个标记，判断目标方块是否被吃掉
    targetFlag = 1
    # 初始化方向
    direction = "right"
    # 改变方向变量
    changeDirection = direction

    # 键盘按键等都是事件，这些时间都要放到实时循环里面处理
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = "right"
                if event.key == K_LEFT:
                    changeDirection = "left"
                if event.key == K_UP:
                    changeDirection = "up"
                if event.key == K_DOWN:
                    changeDirection = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))


        # 确定方向
        if changeDirection == "left" and not direction == "right":
            direction = changeDirection
        if changeDirection == "right" and not direction == "left":
            direction = changeDirection
        if changeDirection == "up" and not direction == "down":
            direction = changeDirection
        if changeDirection == "down" and not direction == "up":
            direction = changeDirection

        # 根据方向移蛇头
        if direction == "right":
            snakePosition[0] += 20
        if direction == "left":
            snakePosition[0] -= 20
        if direction == "up":
            snakePosition[1] -= 20
        if direction == "down":
            snakePosition[1] += 20

        # 增加蛇的长度
        snakeBody.insert(0,list(snakePosition))
        # 判断如果贪吃蛇和目标方块的位置重合就增加长度，则标记为0
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetFlag = 0
        else:
            snakeBody.pop()


        if targetFlag == 0:
            # 32和24不能取到
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            targetPosition = [int(x*20),int(y*20)]
            targetFlag = 1


        # 绘制显示层
        playSurface.fill(blackColor)
        for position in snakeBody:
            # 在playSurface上绘制矩形,并指定颜色
            pygame.draw.rect(playSurface,whiteColor,Rect(position[0],position[1],20,20)) # 蛇
            pygame.draw.rect(playSurface,redColor,Rect(targetPosition[0],targetPosition[1],20,20)) # 目标方块


        # 游戏结束
        pygame.display.flip()

        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameover()

        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameover()


        # 控制游戏速度,值越大速度越快
        fpsClock.tick(20)





if __name__ == "__main__":
    main()
