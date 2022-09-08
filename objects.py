import pygame
from settings import Settings
ai_settings = Settings()

class Luni():
    def __init__(self, screen):
        # Initialize luni's stats and properties
        self.screen = screen

        # Initialize image and rect properties
        self.image = pygame.image.load('orb.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = [ai_settings.screen_width/3, ai_settings.floor_y]


        # Initialize luni's left and right keys
        self.go_left = False
        self.go_right = False

        # Initialize luni's physics properties
        self.x_acceleration = 0
        self.x_velocity = 0
        self.y_acceleration = ai_settings.g
        self.y_velocity = 0
        self.is_jumping = False

        # Prediction vars
        self.next_left = self.rect.left
        self.next_bottom = self.rect.bottom
        self.next_right = self.rect.right
        self.next_top = self.rect.top
        

    def blitme(self):
        # Draws itself to screen
        self.screen.blit(self.image,self.rect)

    def horizontal_movement(self):
        if (self.go_left and (not self.go_right)):
            self.x_velocity = -ai_settings.move_increment
            if (self.next_left < self.screen_rect.left):
                self.x_velocity = 0
        elif (self.go_right and (not self.go_left)):
            self.x_velocity = ai_settings.move_increment
            if (self.next_right > self.screen_rect.right):
                self.x_velocity = 0
        else:
            self.x_velocity = 0
        

    def calculate_next(self):
        self.next_bottom = self.rect.bottom - self.y_velocity
        self.next_left = self.rect.left + self.x_velocity
        self.next_right = self.rect.right + self.x_velocity
        self.next_top = self.rect.top - self.y_velocity
    
    def jump(self):
        if (not self.is_jumping):
            return
        if self.rect.bottom == ai_settings.floor_y:
            self.y_velocity = ai_settings.jump_vel
            

            
    def implement_velocities(self):
        self.x_velocity += self.x_acceleration
        self.y_velocity += self.y_acceleration
        if (self.rect.bottom - self.y_velocity >= ai_settings.floor_y):
            self.y_velocity = 0
            self.rect.bottom = ai_settings.floor_y

        self.rect.centerx += self.x_velocity
        self.rect.centery -= self.y_velocity

    def update(self):
        # Calculate next pos to check for stuff
        self.calculate_next()
        # Jump!
        self.jump()
        # Horizontal movement
        self.horizontal_movement()
        # Implement velocities and accelerations
        self.implement_velocities()


class Block():
    def __init__(self, screen, left, top):
        # Initialize block properties
        self.screen = screen

        # Initialize image and rect properties
        self.image = pygame.image.load('block.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.top = top
        self.rect.left = left
