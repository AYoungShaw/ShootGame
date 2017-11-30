import pygame

class Settings():
	#设置游戏屏幕大小
	def __init__(self):
		'''初始化类'''
		
		self.SCREEN_WIDTH = 480
		self.SCREEN_HEIGHT = 800
		# 设定界面大小，背景图片及标题
		# 像素大小
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		# 标题
		self.pygame.display.set_caption('飞机大战')
		# 背景图
		self.background = pygame.image.load('image\\background.png').convert()
		#game over 背景
		self.game_over = pygame.image.load('image\\gameover.png')

		# 飞机与子弹图片集合
		self.plane_img = pygame.image.load('image\\shoot.png')
