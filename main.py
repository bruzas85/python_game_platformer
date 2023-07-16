import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("images/player/001.png"))
        self.sprites.append(pygame.image.load("images/player/002.png"))
        self.sprites.append(pygame.image.load("images/player/003.png"))
        self.sprites.append(pygame.image.load("images/player/004.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[self.current_sprite]

pygame.init()
screen_width = 240
screen_height = 240
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(50, 75)
moving_sprites.add(player)

pygame.display.set_caption("platformer")
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

player_anim_count = 0

running = True
while running:  # Основной цикл игры

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            player.animate()

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(10)
