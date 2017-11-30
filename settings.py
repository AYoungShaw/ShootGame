import pygame

class setting():
	#设置游戏屏幕大小
	SCREEN_WIDTH = 480
	SCREEN_HEIGHT = 800
	# 设定界面大小，背景图片及标题
	# 像素大小
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	# 标题
	pygame.display.set_caption('飞机大战')
	# 背景图
	background = pygame.image.load('image\\background.png').convert()
	#gameover 背景
	game_over = pygame.image.load('image\\gameover.png')

	# 飞机与子弹图片集合
	plane_img = pygame.image.load('image\\shoot.png')