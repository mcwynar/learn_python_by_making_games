import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# set window title
pygame.display.set_caption('Asteroid Shooter')

# create a surface
test_surf = pygame.Surface((400, 100))
# we need to attach the surface to the display surface
# both the display surface and the surface are black


# keeps the code going
while True:   # run forever -> keeps our game running
    # DO NOT RUN THE CODE UNTIL I TELL YOU

    # 1. Input  -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updates
    display_surface.fill((15,140,122))
    test_surf.fill((219,114,16))
    display_surface.blit(test_surf, (0,0))

    # 3. Show the frame to the player / update the display surface
    pygame.display.update()