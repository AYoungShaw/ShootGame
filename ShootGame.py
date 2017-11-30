# 初始化pygame

import pygame

from sys import exit

from pygame.locals import *

# from plane import Bullet, Player, Enemy

# from settings import setting

import random


#设置游戏屏幕大小
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800
#子弹类
class Bullet(pygame.sprite.Sprite):
	def __init__(self, bullet_img, init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.midbottom = init_pos
		self.speed = 10

	def move(self):
		self.rect.top -= self.speed
		

# 玩家飞机类
class Player(pygame.sprite.Sprite):
	def __init__(self, plane_img, player_rect, init_pos):
		pygame.sprite.Sprite.__init__(self)
		#用来存储玩家飞机图片的列表
		self.image = []

		for i in range(len(player_rect)):
			# convert_alpha透明的部分
			# 将传入的每个爆炸图片对象透明化
			self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
		
		# 初始化图片所在的矩形
		# 获取第一个飞机对象
		self.rect = player_rect[0]
		# 初始化矩形的左下角坐标
		self.rect.topleft = init_pos
		# 初始化玩家飞机速度
		self.speed = 8

		#玩家飞机所发射的子弹的集合
		self.bullets = pygame.sprite.Group()

		# 玩家飞机图片索引
		self.img_index = 0

		# 玩家是否被击中
		self.is_hit = False

	# 发射子弹
	def shoot(self, bullet_img):
		# 实例化子弹
		bullet = Bullet(bullet_img, self.rect.midtop)
		self.bullets.add(bullet)

	# 向上移动，需要判断边界
	def moveUp(self):
		if self.rect.top <= 0:
			self.rect.top = 0
		else:
			self.rect.top -= self.speed

	# 向下移动
	def moveDown(self):
		if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
			self.rect.top = SCREEN_HEIGHT - self.rect.height
		else:
			self.rect.top += self.speed

	#向左移动
	def moveLeft(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		else:
			self.rect.left -= self.speed

	# 向右移动
	def moveRight(self):
		if self.rect.left >= SCREEN_WIDTH - self.rect.width:
			self.rect.left = SCREEN_WIDTH - self.rect.width
		else:
			self.rect.left += self.speed

# 敌机类
# pygame.sprite	
# 操作移动图像
class Enemy(pygame.sprite.Sprite):
	def __init__(self, enemy_img, enemy_down_imgs, init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = enemy_img
		self.rect = self.image.get_rect()
		self.rect.topleft = init_pos
		self.down_imgs = enemy_down_imgs
		self.speed = 2
		self.down_index = 0

	# 敌机移动，边界判断以及删除在游戏主循环里处理
	def move(self):
		self.rect.top += self.speed


# 先初始化
pygame.init()

# 设定界面大小，背景图片及标题
# 像素大小

# pygame.display.set_mode()这个函数会返回一个Surface对象
# 这里也就是要绘制的游戏界面的大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 标题
pygame.display.set_caption('飞机大战')

# 背景图
background = pygame.image.load('image/background.png').convert()

#game over 背景
game_over = pygame.image.load('image/gameover.png')

# 飞机与子弹图片集合
plane_img = pygame.image.load('image/shoot.png')


# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
player_rect = []
# 玩家飞机图片
player_rect.append(pygame.Rect(0, 99, 102, 126))

#玩家爆炸图片
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))

player_pos = [200, 600]

# 实例化玩家飞机
player = Player(plane_img, player_rect, player_pos)

# 子弹图片
bullet_rect = pygame.Rect(1004, 987, 9, 21)
# pygame.surface	
# 管理图像和屏幕
bullet_img = plane_img.subsurface(bullet_rect)

#敌机不同的状态列表，多张图片展示为动画效果
# pygame.rect	
# 管理矩形区域
# 生成一个Rect对象
# pygame.Rect(left,top,width,height)
enemy1_rect = pygame.Rect(534, 612, 57, 43)
# Rect对象是用来存储矩形对象的，Rect对象有一些虚拟属性，
# 比如top.left,bottom.right这些是用来固定矩形的位置的，
# 还有size,width,height，这些是描述矩形大小，宽高分别是多大，
# center为矩形的中心点，其实就是关于横纵坐标的二元组，因此又有centerx,centery两个属性

enemy1_img = plane_img.subsurface(enemy1_rect)

enemy1_down_imgs = []
# 传入一个矩形对象，为了返回实例surface对象中矩形的一部分，
# 新的surface对象将继承他的父亲，颜色以及透明度设置上都继承了它的父对象
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

# 将大量的实体添加到精灵组里面
# pygame.sprite.Group()函数可以创建一个精灵组：
# group = pygame.sprite.Group()
# group.add(sprite_one)
# 精灵组也有update和draw函数：

# group.update()
# group.draw()

enemies1 = pygame.sprite.Group()

#存储被击毁的飞机，用来渲染击毁动画
enemies_down = pygame.sprite.Group()

#初始化射击及敌机移动频率
shoot_frequency = 0
enemy_frequency = 0

#玩家飞机被击中后的效果处理
player_down_index = 16

#初始化分数
score = 0
# 游戏循环帧率设置
# pygame中的time模块有一个get_ticks()方法可以满足定时
clock = pygame.time.Clock()

#判断游戏循环退出的参数
running = True

# 游戏主循环
while running:
	# 控制游戏最大帧率为60
	# 启动一个定时器，然后调用tick（num）函数就可以让游戏以num帧来运行了。
	clock.tick(60)

	# 生成子弹，需要控制发射频率
	# 首先判断玩家飞机没有被击中
	if not player.is_hit:
		if shoot_frequency % 15 == 0:
			player.shoot(bullet_img)
		shoot_frequency += 1
		if shoot_frequency >= 15:
			shoot_frequency = 0

	# 生成敌机，需要控制生成频率
	if enemy_frequency % 50 == 0:
		enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
		# 实例化敌机
		enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)

		enemies1.add(enemy1)

	enemy_frequency += 1

	if enemy_frequency >= 100:
		enemy_frequency = 0

	# 以固定速度移动子弹
	for bullet in player.bullets:
		bullet.move()
		#移除屏幕后删除子弹
		# rect自带的属性
		if bullet.rect.bottom < 0:
			player.bullets.remove(bullet)

	
	for enemy in enemies1:
		#移动敌机
		enemy.move()
		# 敌机与玩家飞机碰撞效果处理
		if pygame.sprite.collide_circle(enemy, player):
			enemies_down.add(enemy)
			enemies1.remove(enemy)
			player.is_hit = True
			break
		# 移动出屏幕后删除敌机
		if enemy.rect.top < 0:
			enemies1.remove(enemy)	


	# 敌机被子弹击中处理效果
	# 将被击中的敌机对象添加到击毁敌机Group中，用来渲染击毁动画
	enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)

	for enemy_down in enemies1_down:
		enemies_down.add(enemy_down)


	# 绘制背景
	# 对surface对象填充某一种颜色，可以主要是对背景可以实现填充
	screen.fill(0)
	screen.blit(background, (0, 0))

	# 绘制玩家飞机
	if not player.is_hit:
		# blit是个重要函数，第一个参数为一个Surface对象，第二个为位置
		# Surface对象有一个名为blit()的方法，它可以绘制位图
		screen.blit(player.image[player.img_index], player.rect)
		# 更换图片索引使飞机有动画效果
		player.img_index = shoot_frequency // 8
	else:
		# 玩家飞机被击中后的效果处理
		player.img_index = player_down_index // 8
		screen.blit(player.image[player.img_index - 1], player.rect)
		player_down_index += 1

		if player_down_index > 47:
			# 击中效果处理完后游戏结束
			running = False

	# 敌机被子弹击中效果显示
	for enemy_down in enemies_down:
		if enemy_down.down_index == 0:
			pass
		if enemy_down.down_index > 7:
			enemies_down.remove(enemy_down)
			score += 1000
			continue
		
		screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)

		enemy_down.down_index += 1

	# pygame.draw	
	# 绘制形状、线和点

	# 显示子弹
	player.bullets.draw(screen)
	# 显示敌机
	enemies1.draw(screen)

	#绘制得分
	score_font = pygame.font.Font(None, 36)
	score_text = score_font.render(str(score), True, (128, 128, 128))
	text_rect = score_text.get_rect()
	text_rect.topleft = [10, 10]
	screen.blit(score_text, text_rect)

	# 更新屏幕
	pygame.display.update()

	# 处理游戏退出
	# pygame.event	
	# 管理事件
	# pygame.event.get()来处理所有的事件
	# QUIT	用户按下关闭按钮
	for event in pygame.event.get():
		# event.type 事件的类型
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# 获取键盘事件
	# pygame.key	
	# 读取键盘按键
	key_pressed = pygame.key.get_pressed()

	# 处理键盘事件(移动飞机的位置)
	if key_pressed[K_w] or key_pressed[K_UP]:
		player.moveUp()
	if key_pressed[K_s] or key_pressed[K_DOWN]:
		player.moveDown()
	if key_pressed[K_a] or key_pressed[K_LEFT]:
		player.moveLeft()
	if key_pressed[K_d] or key_pressed[K_RIGHT]:
		player.moveRight()

# def run():
	
	

# 游戏结束显示分数
# pygame.font.Font(字体类型, 大小)
# 返回一个字体对象
# 使用字体
font = pygame.font.Font(None, 48)
# 一旦你创建了一个font对象，你就可以使用render方法来写字了，然后就能blit到屏幕上：
# 第一个参数是写的文字；第二个参数是个布尔值，第三个参数是字体的颜色，
# 第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。
text = font.render('Score:' + str(score), True, (255, 0, 0))

text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

# 显示得分并处理游戏退出
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	# 刷新一下画面
	pygame.display.update()