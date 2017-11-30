import pygame

class ShowScore(object):
	"""docstring for DisplayScore"""
	def __init__(self, screen):
		self.screen = screen


	def show(self):
		# 游戏结束显示分数
		# pygame.font.Font(字体类型, 大小)
		# 返回一个字体对象
		# 使用字体
		#game over 背景
		self.game_over = pygame.image.load('image\\gameover.png')

		self.font = pygame.font.Font(None, 48)
		# 一旦你创建了一个font对象，你就可以使用render方法来写字了，然后就能blit到屏幕上：
		# 第一个参数是写的文字；第二个参数是个布尔值，第三个参数是字体的颜色，
		# 第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。
		self.text = font.render('Score:' + str(score), True, (255, 0, 0))

		self.text_rect = text.get_rect()
		self.text_rect.centerx = self.screen.get_rect().centerx
		self.text_rect.centery = self.screen.get_rect().centery + 24
		self.screen.blit(self.game_over, (0, 0))
		self.screen.blit(self.text, self.text_rect)
		


