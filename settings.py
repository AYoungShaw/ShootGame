import pygame

class Settings():
	#设置游戏屏幕大小
	def __init__(self):
		'''初始化类'''
		#设置游戏屏幕大小
		self.SCREEN_WIDTH = 480
		self.SCREEN_HEIGHT = 800
		# 设定界面大小，背景图片及标题
		# 像素大小
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
		# 背景图
		self.background = pygame.image.load('image\\background.png').convert()
		#game over 背景
		self.game_over = pygame.image.load('image\\gameover.png')

		# 飞机与子弹图片集合
		self.plane_img = pygame.image.load('image\\shoot.png')

		# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
		self.player_rect = []
		# 玩家飞机图片
		self.player_rect.append(pygame.Rect(0, 99, 102, 126))
		#玩家爆炸图片
		self.player_rect.append(pygame.Rect(165, 234, 102, 126))
		self.player_rect.append(pygame.Rect(330, 624, 102, 126))
		self.player_rect.append(pygame.Rect(330, 498, 102, 126))
		self.player_rect.append(pygame.Rect(432, 624, 102, 126))

		self.player_pos = [200, 600]

		# 子弹图片
		self.bullet_rect = pygame.Rect(1004, 987, 9, 21)
		# pygame.surface	
		# 管理图像和屏幕
		self.bullet_img = self.plane_img.subsurface(self.bullet_rect)

		#敌机不同的状态列表，多张图片展示为动画效果
		# pygame.rect	
		# 管理矩形区域
		# 生成一个Rect对象
		# pygame.Rect(left,top,width,height)
		self.enemy1_rect = pygame.Rect(534, 612, 57, 43)
		# Rect对象是用来存储矩形对象的，Rect对象有一些虚拟属性，
		# 比如top.left,bottom.right这些是用来固定矩形的位置的，
		# 还有size,width,height，这些是描述矩形大小，宽高分别是多大，
		# center为矩形的中心点，其实就是关于横纵坐标的二元组，因此又有centerx,centery两个属性

		self.enemy1_img = self.plane_img.subsurface(self.enemy1_rect)

		self.enemy1_down_imgs = []
		# 传入一个矩形对象，为了返回实例surface对象中矩形的一部分，
		# 新的surface对象将继承他的父亲，颜色以及透明度设置上都继承了它的父对象
		self.enemy1_down_imgs.append(self.plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
		self.enemy1_down_imgs.append(self.plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
		self.enemy1_down_imgs.append(self.plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
		self.enemy1_down_imgs.append(self.plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

		# 将大量的实体添加到精灵组里面
		# pygame.sprite.Group()函数可以创建一个精灵组：
		# group = pygame.sprite.Group()
		# group.add(sprite_one)
		# 精灵组也有update和draw函数：

		# group.update()
		# group.draw()

		self.enemies1 = pygame.sprite.Group()

		#存储被击毁的飞机，用来渲染击毁动画
		self.enemies_down = pygame.sprite.Group()

		#初始化射击及敌机移动频率
		self.shoot_frequency = 0
		self.enemy_frequency = 0

		#玩家飞机被击中后的效果处理
		self.player_down_index = 16
