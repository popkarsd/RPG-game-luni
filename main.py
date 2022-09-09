import pygame
import sys
from objects import *
from settings import Settings



def run_game():
    pygame.init()

    # Clock
    clock = pygame.time.Clock()
    ai_settings = Settings()

    # Screen
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    # Sprite groups
    luni = Luni(screen)
    blocks  = pygame.sprite.Group()
    for i in range(6):
        blocks.add(Block(screen, ai_settings.screen_width/2-100*i, 460-30*i))

    mouse_pos = pygame.mouse.get_pos()
    # Start loop
    while True:
        # Update mouse_pos
        mouse_pos = pygame.mouse.get_pos()
        # Watch for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    luni.is_jumping = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #be sure to get these constant into settings.py
                    luni.go_left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    luni.go_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    luni.is_jumping = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #be sure to get these constant into settings.py
                    luni.go_left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    luni.go_right = False



        # Update physics properties
        luni.update()

        # Check for collisions
        collide_list = pygame.sprite.spritecollide(luni, blocks, False)
        if (len(collide_list) > 0):
            luni.debug_collision(collide_list[0].rect)
        else:
            luni.floor_y = ai_settings.floor_y

        # Redraw background/screen color
        screen.fill(ai_settings.bg_col)
        
        # Draw characters & objects
        luni.blitme()
        for entity in blocks:
            entity.blitme()
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,ai_settings.floor_y,2000,2) )
        # Make screen visible
        pygame.display.flip()

        # Pass time
        clock.tick(60)
run_game()

##########
'''
goals/steps for the game:
1. create 1st level
    - create physics for the world
    - ceate && animate luni's sprite
    - create terrain
    - create weapons
    - create basic enemy spirte (all 3)
    - create narrator textbox && texts
    - create elementals
2. create main menu interface
3. add music
4. add more levels
5. add prelogue
6. add epilogue
done!?
    
'''
##########
