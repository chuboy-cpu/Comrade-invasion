import pygame

class Ship():

 def __init__(self, screen):
    """Initialize the ship and set its starting position."""
    self.screen = screen

 # Load the ship image and get its rect.
    self.image = pygame.image.load("C:\PROGRAMMING\Python\\alien_invasion\images\ship3.bmp")
    self.rect = self.image.get_rect() # getting the rectangle attribute of the image
    self.screen_rect = screen.get_rect()

    self.ship_center()
 
    self.moving_right = False    
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False


 def ship_center(self):
 # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom



 def blitme(self):

    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)

 def ship_update(self):

     if self.moving_right and self.rect.right < self.screen_rect.right:
         self.rect.centerx +=2
         

     if self.moving_left and self.rect.left > self.screen_rect.left :
         self.rect.centerx -=2

     if self.moving_up and self.rect.top !=0:
         self.rect.y -=2

     if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
         self.rect.y +=2




'''class Bullet(Sprite):

 """A class to manage bullets fired from the ship"""
 def __init__(self, my_set, screen, ship):
     """Create a bullet object at the ship's current position."""
     super().__init__()

     self.screen = screen
     self.right_side_bullet = False
     self.left_side_bullet = False

 # Create a bullet rect at (0, 0) and then set correct position.
     self.bullet_rect = pygame.Rect(0, 0, my_set.bullet_width, my_set.bullet_height)
     self.bullet_rect.centerx = ship.rect.centerx
     self.bullet_rect.top = ship.rect.top
 
# Create a side bullet rect  and its correct position.
     
     self.side_bullet_rect = pygame.Rect(0, 0, my_set.side_bullet_width, my_set.side_bullet_height)

     self.side_bullet_rect.midleft = ship.rect.midleft
#     elif self.left_side_bullet == True:
     #self.side_bullet_rect.midleft = ship.rect.midleft
     #self.side_bullet_rect.bottomleft = ship.rect.bottomleft
    
 # Store the bullet's position as a value.
     self.y = self.bullet_rect.y
     self.x = self.side_bullet_rect.x
     self.color = my_set.bullet_color
     self.speed = my_set.bullet_speed 


 def update(self):
     """Move the bullet up the screen."""
 # Update the decimal position of the bullet.
     self.y -= self.speed
 # Update the rect position.
     self.bullet_rect.y = self.y

 # Update the decimal position of the side_bullet.
    
     if self.right_side_bullet: 
        self.x += self.speed
        
     #if self.left_side_bullet:   
     self.x -= self.speed

 # Update the rect position.
     self.side_bullet_rect.x = self.x

 def draw_bullet(self):
        """Draw the bullet to the screen.""" 
        print(self.left_side_bullet)
        if self.left_side_bullet:
            pygame.draw.rect(self.screen, self.color, self.side_bullet_rect)
        
        else:   
           pygame.draw.rect(self.screen, self.color, self.bullet_rect) '''

     
     