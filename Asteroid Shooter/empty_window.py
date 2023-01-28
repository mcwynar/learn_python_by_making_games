import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# set window title
pygame.display.set_caption('Asteroid Shooter')

# keeps the code going
while True:   # run forever -> keeps our game running
    # DO NOT RUN THE CODE UNTIL I TELL YOU

    # The game loop
    # The entire logic of our game will run in a while True loop
    # Inside of it, we will check for any input, update all parts of the game and place graphics on the display surface
    # At the end of the loop, we will show the display surface

    # 1. Input  -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updates
    #nothing yet

    # 3. Show the frame to the player / update the display surface
    pygame.display.update()