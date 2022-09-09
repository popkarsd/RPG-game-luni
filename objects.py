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

        #collision vars
        self.floor_y = ai_settings.floor_y
        self.collided = False
        # prev rect
        self.prev_rect = self.image.get_rect()

        

    def blitme(self):
        # Draws itself to screen
        self.screen.blit(self.image,self.rect)

    def horizontal_movement(self):
        if (self.go_left and (not self.go_right)):
            self.x_velocity = -ai_settings.move_increment
            if (self.rect.left < self.screen_rect.left):
                self.x_velocity = 0
        elif (self.go_right and (not self.go_left)):
            self.x_velocity = ai_settings.move_increment
            if (self.rect.right > self.screen_rect.right):
                self.x_velocity = 0
        else:
            self.x_velocity = 0
        

    def save_pos(self):
        self.prev_rect = self.rect.copy()
    
    def jump(self):
        if (not self.is_jumping):
            return
        if self.rect.bottom == self.floor_y:
            self.rect.centery -= 1
            self.y_velocity = ai_settings.jump_vel


            
    def implement_velocities(self):
        self.x_velocity += self.x_acceleration
        self.y_velocity += self.y_acceleration

        self.rect.centerx += self.x_velocity
        self.rect.centery -= self.y_velocity

        # Check if luni hits "floor" next frame and if so zero the velocity and put it back up
        if (self.rect.bottom >= self.floor_y):
            self.y_velocity = 0
            self.rect.bottom = self.floor_y


    def update(self):
        # Jump!
        self.jump()
        # Horizontal movement velocity stuff
        self.horizontal_movement()
        # Saves current positions 
        self.save_pos()
        # Implement velocities and accelerations
        self.implement_velocities()
    
    def debug_collision(self, collided_rect):

        #checks if luni coming to the box from above
        if (collided_rect.top >= self.prev_rect.bottom):
            self.rect.top = self.prev_rect.top
            self.floor_y = collided_rect.top
        #checks if luni coming from below
        elif (collided_rect.bottom <= self.prev_rect.top):
            self.rect.top = self.prev_rect.top
            self.y_velocity = 0
        #luni coming from left or right
        else:
            self.rect.left = self.prev_rect.left
            





class Block(pygame.sprite.Sprite):
    def __init__(self, screen, left, top):
        super().__init__()
        # Initialize block properties
        self.screen = screen

        # Initialize image and rect properties
        self.image = pygame.image.load('/Users/brendonjiang/Desktop/_home/python_programming/RPG/block.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.top = top
        self.rect.left = left
    
    def blitme(self):
        # Draws itself to screen
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.a = 1
