 
from settings import Setting

from ship import Ship
from comrade import Comrade
from game_functions import Events
from game_stats import Gamestats

from pygame.sprite import Group
import pygame 

def run_game():

 # Initialize game and create a screen object.
 pygame.init()
 
 my_set = Setting()
 stats = Gamestats(my_set)

 screen = pygame.display.set_mode((my_set.screen_width, my_set.screen_height))
 pygame.display.set_caption("Comrade Invasion")
 
 """INTO SCREEN"""
 screen.fill(my_set.screen_color) # Change the color of the screen
 intro_post = screen.get_rect()
 image = pygame.image.load("./images/INTRO.bmp")
 intro_rect = image.get_rect()
 intro_rect.center = intro_post.center
 #intro_rect.midtop = intro_post.midtop +(100)

 screen.blit(image,intro_rect)


 my_ship = Ship(screen)
 comrade = Comrade(my_set,screen)

 # Make a group to store bullets in
 bullets = Group()
 comrades = Group()

 number_row = Events.get_number_rows(my_set, my_ship, comrade.rect.height)
 Events.create_fleet(my_set, screen, comrades,number_row)

  # Start the main loop for the game.
 while True:
    Events.check_events(my_set,screen,my_ship,bullets)
    
    my_ship.ship_update()
    bullets.update(my_set,screen,comrades,bullets,number_row,Events )
    Events.update_comrades(my_set,stats,screen,bullets,comrades,my_ship )
    Events.update_screen(screen,my_set,my_ship,comrades, bullets,3 )
    
 

run_game()