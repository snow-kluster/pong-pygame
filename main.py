
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 400

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 770
paddleB.rect.y = 400

ball = Ball(WHITE,30,30)
ball.rect.x = 400
ball.rect.y = 300

obj_list = pygame.sprite.Group()

obj_list.add(paddleA)
obj_list.add(paddleB)
obj_list.add(ball)
running = True
clock = pygame.time.Clock()

ScoreA = 0
ScoreB = 0

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_x: 
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    screen.fill(BLACK)
    obj_list.update()

    if ball.rect.x>=770:
        ball.velocity[0] = -ball.velocity[0]
        ScoreA+=1
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
        ScoreB+=1
    if ball.rect.y>570:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
    
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    pygame.draw.line(screen, WHITE, [400, 0], [400, 600], 5)
    obj_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(ScoreA), 1, WHITE)
    screen.blit(text, (200,10))
    text = font.render(str(ScoreB), 1, WHITE)
    screen.blit(text, (600,10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

