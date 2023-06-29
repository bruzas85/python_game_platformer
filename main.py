import pygame

pygame.init()
screen_width = 240
screen_height = 240
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("platformer")
clock = pygame.time.Clock()

player_anim_count = 0

running = True
while running:  # Основной цикл игры



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            running = False

    clock.tick(10)
