import pygame
class MySurface(pygame.Surface):
	def __init__(self, xy,color):
		super(MySurface, self).__init__(xy)
		self.color = color

if __name__=="__main__":
	pygame.init()
	screen_size = 400
	main_screen = pygame.display.set_mode((screen_size, screen_size))
	main_screen.fill((255,255,255))
	square = MySurface([20, 20], "black")

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if square.get_bounding_rect().collidepoint(x, y):
				print "clicked"
		main_screen.blit(square, (0, 0))
		pygame.display.flip()
