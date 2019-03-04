import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Shadow Ninja')
clock = pygame.time.clock()
dead = False

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

            print(event)

    pygame.display.update()

    clock.tick(60)

pygame.display.quit()
pygame.quit()
quit()
