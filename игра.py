import pygame
import sys

pygame.init()
screnwidth,screnheidht=1920,1080
scren=pygame.display.set_mode((screnwidth,screnheidht))
pygame.display.set_caption('game')

black=(226, 5, 237)
red=(255,0,0)

sizeplayer=150
playerx,playery=screnwidth // 2,screnheidht // 2
playerspeed=100

runing=True
while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerx-=playerspeed
    if keys[pygame.K_RIGHT]:
        playerx+=playerspeed
    if keys[pygame.K_DOWN]:
        playery+=playerspeed
    if keys[pygame.K_UP]:
        playery-=playerspeed

    playerx=max(0,min(screnwidth-sizeplayer,playerx))
    playery=max(0,min(screnheidht-sizeplayer,playery))

    scren.fill(black)
    pygame.draw.rect(scren,red,(playerx,playery,sizeplayer,sizeplayer))

    pygame.display.flip()


    pygame.time.Clock().tick(100)
