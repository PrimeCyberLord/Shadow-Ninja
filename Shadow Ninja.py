import pygame

#variables
width = 1200
height = 700

##classes
###Player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./Sprite/Idle/0000.png")
		self.rect = self.image.get_rect()
		self.rect.center = (200,600)

	def update(self):
		keystate = pygame.key.get_pressed()

		if keystate[pygame.K_RIGHT]:
			self.rect.x += 2
		if keystate[pygame.K_LEFT]:
			self.rect.x += -2

	def shoot(self):
		weapon = Weapon((self.rect.centerx + 40), (self.rect.centery + 70))
		all_Sprites.add(weapon)
		weapon_Sprite.add(weapon)

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./Sprite/Idle/0000.png")
		self.rect = self.image.get_rect()
		self.rect.center = (1000,600)

class Weapon(pygame.sprite.Sprite):
	def __init__(self, x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./Sprite/Ninja Weapon.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom =y
		self.speed = 5

	def update(self):
		self.rect.x += self.speed
		keystate = pygame.key.get_pressed()
		#remove the bullet
		if self.rect.x > width:
			self.kill()



pygame.init()
screen=gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Shadow Ninja')
clock = pygame.time.Clock()
dead = False
event = pygame.event.get()

#load background
bgImage = pygame.image.load("./background/forest-background.png").convert()
bgImage = pygame.transform.scale(bgImage,(1200,700))

#groups
all_Sprites = pygame.sprite.Group()
enermy_Sprite =pygame.sprite.Group()
weapon_Sprite = pygame.sprite.Group()

#initialise variables
player = Player()
enemy = Enemy()
#add sprite to group
all_Sprites.add(player)
enermy_Sprite


while not dead:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
            dead = True
    	elif event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_SPACE:
        		player.shoot()


    #game Logic


    all_Sprites.update();
    screen.blit(bgImage,[0,0])
    all_Sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
pygame.quit()
quit()
