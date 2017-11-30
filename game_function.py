import sys

import pygame

class Game_function():

	def __init__(self, player):
		# 获取键盘事件
		# pygame.key	
		# 读取键盘按键
		self.key_pressed = pygame.key.get_pressed()
		self.player = player

	def check_events(self):
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

	def chek_board(self):
		# 处理键盘事件(移动飞机的位置)
		if self.key_pressed[K_w] or self.key_pressed[K_UP]:
			player.moveUp()
		if self.key_pressed[K_s] or self.key_pressed[K_DOWN]:
			player.moveDown()
		if self.key_pressed[K_a] or self.key_pressed[K_LEFT]:
			player.moveLeft()
		if self.key_pressed[K_d] or self.key_pressed[K_RIGHT]:
			player.moveRight()