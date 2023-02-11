import pygame
import sys


def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)

def display_score():
    score_text = f'Score:{pygame.time.get_ticks() // 1000} '
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'White', text_rect.inflate(30, 30), width=8, border_radius=5)

def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

# game init
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
# ship_reversed_surf = pygame.transform.flip(ship_surf, flip_x=False, flip_y=True)
# ship_scaled_surf = pygame.transform.scale(ship_surf, (600, 50))
ship_rotated_surf = pygame.transform.rotate(ship_surf, 45)
# ship_y_pos = 500

bg_surf = pygame.image.load('./asteroid_shooter_files/graphics/background.png').convert()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# print(ship_rect)
laser_surf = pygame.image.load('./asteroid_shooter_files/graphics/laser.png').convert_alpha()
laser_list = []
# laser_rect = laser_surf.get_rect(midbottom = (ship_rect.centerx, ship_rect.top))

#laser timer
can_shoot = True
shoot_time = None

# import text
font = pygame.font.Font('./asteroid_shooter_files/graphics/subatomic.ttf', 50)

# drawing
# test_rect = pygame.Rect(100, 200, 400, 500)
# text_border = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)

# keeps the code going
while True:  # run forever -> keeps our game running
    # DO NOT RUN THE CODE UNTIL I TELL YOU

    # 1. Input  -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:
        #     # print(event.pos)
        #     # print(event.buttons)
        #     # print(event.rel)
        #     ship_rect.center = event.pos
        # if event.type == pygame.MOUSEBUTTONUP:
        #     # print('Shoot')
        #     print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            #laser
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

            #timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

    # framerate limit
    dt = clock.tick(120) / 1000
    # print(clock.get_fps())

    # mouse input
    # print(pygame.mouse.get_pos())
    # print(pygame.mouse.get_pressed())
    ship_rect.center = pygame.mouse.get_pos()

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

    display_score()
    # if ship_rect.top > 0:
    #     ship_rect.y -= 4   #or  ship_rect.top -= 4 or  ship_rect.bottom -= 4
    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot, 500)
    # display_surface.blit(laser_surf, laser_rect)


    # rect drawing
    # pygame.draw.rect(display_surface, 'purple', test_rect, width=10, border_radius=5)
    # pygame.draw.lines(display_surface, 'red', False, [(0,0), (200,50), (300,100)])
    # pygame.draw.rect(display_surface, 'red', text_border, width=1)

    for rect in laser_list:
        display_surface.blit(laser_surf, rect)



    display_surface.blit(ship_surf, ship_rect)

    # 3. Show the frame to the player / update the display surface; draw the final frame
    pygame.display.update()
