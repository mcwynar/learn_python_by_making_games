import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# set window title
pygame.display.set_caption('Asteroid Shooter')

clock = pygame.time.Clock()

# create a surface
# test_surf = pygame.Surface((400, 100))
# we need to attach the surface to the display surface
# both the display surface and the surface are black

# importing images
ship_surf = pygame.image.load('./asteroid_shooter_files/graphics/ship.png').convert_alpha()
# ship_y_pos = 500
bg_surf = pygame.image.load('./asteroid_shooter_files/graphics/background.png').convert()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
# print(ship_rect)


# import text
font = pygame.font.Font('./asteroid_shooter_files/graphics/subatomic.ttf',50)
text_surf = font.render('Space', True,'White')
text_rect = text_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-80))

# keeps the code going
while True:   # run forever -> keeps our game running
    # DO NOT RUN THE CODE UNTIL I TELL YOU

    # 1. Input  -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(60)

    # 2. Updates
    display_surface.fill((0, 0, 0))

    # test_surf.fill((219,114,16))
    # place a surface
    # display_surface.blit(test_surf, (880,310))
    # Exercise: Place the test surface so that the is on the right side of the display surface
    # display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(), (WINDOW_HEIGHT - test_surf.get_height())/2))

    display_surface.blit(bg_surf, (0, 0))
    # ship_y_pos -= 1
    # display_surface.blit(ship_surf, (300, 500))
    display_surface.blit(ship_surf, ship_rect)
    if ship_rect.top > 0:
        ship_rect.y -= 4   #or  ship_rect.top -= 4 or  ship_rect.bottom -= 4

    display_surface.blit(text_surf, text_rect)

    # 3. Show the frame to the player / update the display surface
    pygame.display.update()
