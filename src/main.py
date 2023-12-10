import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 748)) # , flags=pygame.NOFRAME
pygame.display.set_caption("Pygame itProger Game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("images/bg.png")
# player = pygame.image.load("images/idle.png")
walk_left = [
    pygame.image.load("images/player_left/player_left1.png"),
    pygame.image.load("images/player_left/player_left2.png"),
    pygame.image.load("images/player_left/player_left3.png"),
    pygame.image.load("images/player_left/player_left4.png"),
    pygame.image.load("images/player_left/player_left5.png"),
    pygame.image.load("images/player_left/player_left6.png")
]
walk_right = [
    pygame.image.load("images/player_right/player_right1.png"),
    pygame.image.load("images/player_right/player_right2.png"),
    pygame.image.load("images/player_right/player_right3.png"),
    pygame.image.load("images/player_right/player_right4.png"),
    pygame.image.load("images/player_right/player_right5.png"),
    pygame.image.load("images/player_right/player_right6.png")
]

player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound("sounds/bg.mp3")
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))
    screen.blit(walk_right[player_anim_count], (640, 550))

    if player_anim_count == 5:
        player_anim_count = 0
    else:
        player_anim_count += 1
    
    bg_x -= 2
    if bg_x == -1280:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    clock.tick(20)
