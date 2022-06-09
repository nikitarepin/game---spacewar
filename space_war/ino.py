import pygame

class Ino(pygame.sprite.Sprite):
	#класс 1 пришельца 

	def __init__(self, screen):
		#инициализация и задаем нач позицию
		super(Ino, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('image/ino.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def draw(self):
		#вывод пришельца на экран
		self.screen.blit(self.image, self.rect)


	def update(self):
		# перемещение пришельцев
		self.y += 0.3
		self.rect.y = self.y