# 初始化pygame

import pygame

from sys import exit

from pygame.locals import *

from plane import Bullet, Player, Enemy

from settings import Settings

from DisplayScore import ShowScore

from game_function import Game_function

import random

def run_game():
	# 先初始化
	pygame.init()

	plane_settings = Settings()

	# pygame.display.set_mode()这个函数会返回一个Surface对象
	# 这里也就是要绘制的游戏界面的大小
	screen = pygame.display.set_mode((plane_settings.SCREEN_WIDTH, plane_settings.SCREEN_HEIGHT))

	# 标题
	pygame.display.set_caption('飞机大战')

	# 实例化玩家飞机
	player = Player(plane_settings.plane_img, plane_settings.player_rect, plane_settings.player_pos)

	#初始化分数
	score = 0
	# 游戏循环帧率设置
	# pygame中的time模块有一个get_ticks()方法可以满足定时
	clock = pygame.time.Clock()

	#判断游戏循环退出的参数
	running = True

	#初始化射击及敌机移动频率
	shoot_frequency = 0
	enemy_frequency = 0

	#玩家飞机被击中后的效果处理
	player_down_index = 16
	game_functions = Game_function(player)

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
			enemy1_pos = [random.randint(0, plane_settings.SCREEN_WIDTH - enemy1_rect.width), 0]
			# 实例化敌机
			enemy1 = Enemy(plane_settings.enemy1_img, plane_settings.enemy1_down_imgs, plane_settings.enemy1_pos)

			plane_settings.enemies1.add(enemy1)

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

		for enemy in plane_settings.enemies1:
			#移动敌机
			enemy.move()
			# 敌机与玩家飞机碰撞效果处理
			if pygame.sprite.collide_circle(enemy, player):
				plane_settings.enemies_down.add(enemy)
				plane_settings.enemies1.remove(enemy)
				player.is_hit = True
				break
			# 移动出屏幕后删除敌机
			if enemy.rect.top < 0:
				plane_settings.enemies1.remove(enemy)	


		# 敌机被子弹击中处理效果
		# 将被击中的敌机对象添加到击毁敌机Group中，用来渲染击毁动画
		plane_settings.enemies1_down = pygame.sprite.groupcollide(plane_settings.enemies1, player.bullets, 1, 1)

		for enemy_down in plane_settings.enemies1_down:
			plane_settings.enemies_down.add(enemy_down)


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
		for enemy_down in plane_settings.enemies_down:
			if enemy_down.down_index == 0:
				pass
			if enemy_down.down_index > 7:
				plane_settings.enemies_down.remove(enemy_down)
				score += 1000
				continue
			
			screen.blit(plane_settings.enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)

			enemy_down.down_index += 1

		# pygame.draw	
		# 绘制形状、线和点

		# 显示子弹
		player.bullets.draw(screen)
		# 显示敌机
		plane_settings.enemies1.draw(screen)

		#绘制得分
		score_font = pygame.font.Font(None, 36)
		score_text = score_font.render(str(score), True, (128, 128, 128))
		text_rect = score_text.get_rect()
		text_rect.topleft = [10, 10]
		screen.blit(score_text, text_rect)

		# 更新屏幕
		pygame.display.update()
		game_functions.check_events()
		game_functions.chek_board()
		
	# 结束显示分数
	showScore = ShowScore(screen)
	showScore.show()

	# 显示得分并处理游戏退出
	while 1:
		game_functions.check_events()
	# 刷新一下画面
	pygame.display.update()

run_game()