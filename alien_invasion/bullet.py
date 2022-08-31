import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

 """A class to manage bullets fired from the ship"""
 def __init__(self,setting, screen, ship):
     """Create a bullet object at the ship's current position."""
     super().__init__()
     

     self.screen = screen
     self.right_side_bullet = False
     self.left_side_bullet = False
     self.top_bullet =False


     
           

     
# Create a bullet rect at (0, 0) and then set correct position.
     self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
     self.rect.centerx = ship.rect.centerx
     self.rect.top = ship.rect.top
 
# Create a side bullet rect  and its correct position.
    
          
     self.rect.center = ship.rect.center
    # self.rect.midleft = ship.rect.midleft

 # Store the bullet's position as a value.
     self.y = self.rect.y
     self.x = self.rect.x
     self.color =  setting.bullet_color
     self.speed =  setting.bullet_speed 
 
     
    
 def update(self,my_set,screen,comrades,bullets,number_row,Events):
     """Move the bullet up the screen."""
     if self.top_bullet:
         # Update the decimal position of the bullet.
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y

 # Update the decimal position of the side_bullet.
    
     if self.right_side_bullet: 
        self.x += self.speed
        
     if self.left_side_bullet:   
        self.x -= self.speed
         # Update the rect position.
     self.rect.x = self.x

    
# Remove old bullets
     for bullet in bullets.copy():
       if bullet.rect.bottom <=0 :
            bullets.remove(bullet)
       elif bullet.rect.x <=0:
            bullets.remove(bullet)
       elif bullet.rect.x >=1200:
            bullets.remove(bullet)
        #print(len(bullets))
     if len(comrades) < 2:
          Events.create_fleet(my_set, screen, comrades,number_row)
     


 def draw_bullet(self):
        """Draw the bullet to the screen.""" 
        #print(self.left_side_bullet)
         
        pygame.draw.rect(self.screen, self.color, self.rect) 

     
     