import pygame
from pygame.sprite import Sprite

class Comrade(Sprite):

    def __init__(self,setting,screen):
        super().__init__()

        self.screen = screen
        self.setting = setting

 # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("C:\PROGRAMMING\Python\\alien_invasion\images\comrade 1.bmp")
        self.rect = self.image.get_rect()

 # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

 # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = self.rect.y
    def check_edges(self):
           screen_rect = self.screen.get_rect()
           if self.rect.right >= screen_rect.right:
                  return True
           elif self.rect.left <= 0:
                  return True


    def update(self):
           """Move Comrades Right"""
           self.x += (self.setting.comrade_speed* self.setting.comrade_direction)
           self.rect.x = self.x
           
         

  

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)