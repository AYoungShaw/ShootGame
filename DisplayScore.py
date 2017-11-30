import pygame

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