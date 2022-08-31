import pygame
import sys
from bullet import Bullet
from comrade import Comrade
from time import sleep
#from random import randint
class Events():

     
    def check_events(my_set,screen,ship,bullets):

            # Watch for keyboard and mouse events.
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    my_set.screen_color =(0,0,120)
                 

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # moves the ship a step to the right
                        ship.moving_right = True
                    
                    elif event.key == pygame.K_LEFT:
                        # moves the ship a step to the right
                        ship.moving_left = True

                    elif event.key == pygame.K_UP:
                        # moves the ship a step Up
                        ship.moving_up = True

                    elif event.key == pygame.K_DOWN:
                        # moves the ship a step down
                        ship.moving_down = True

                    elif event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_d:
                        # Create Bullets
                       # if len(bullets) < my_set.bullet_allowed:
                          new_bullet = Bullet(my_set,screen,ship)
                          

                          if event.key == pygame.K_w:
                               new_bullet.top_bullet =True
                               my_set.bullet_width = 4
                               my_set.bullet_height = 15
                          if event.key == pygame.K_a:
                              new_bullet.left_side_bullet = True
                              my_set.bullet_width = 15
                              my_set.bullet_height = 4
                              
                          if event.key == pygame.K_d:        
                              new_bullet.right_side_bullet = True
                              my_set.bullet_width = 15
                              my_set.bullet_height = 4
                          bullets.add(new_bullet)
                          

                          
                          
                    elif  event.key == pygame.K_ESCAPE:
                        sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        ship.moving_right = False

                    elif event.key == pygame.K_LEFT:
                        ship.moving_left = False
                    
                    elif event.key == pygame.K_UP:
                        ship.moving_up = False

                    elif event.key == pygame.K_DOWN:
                        ship.moving_down = False

    def get_number_rows(setting, ship, alien_height):
     """Determine the number of rows of comrades that fit on the screen."""
     available_space_y = (setting.screen_height -(2 * alien_height) - ship.rect.height)
     number_rows = int(available_space_y / (2 * alien_height))
     return number_rows


    def create_fleet(setting, screen, comrades,number_row):
      """Create a full fleet of comrades."""
 # Create an comrade and find the number of comrades in a row.
 # Spacing between each comrade is equal to one comrade width.
      comrade = Comrade(setting, screen)
      comrade_width = comrade.rect.width
      available_space_x = setting.screen_width - 2 * comrade_width
      number_aliens_x = int(available_space_x / (2 * comrade_width))
 
 # Create the first row of comrades.
      for row_number in range(number_row):
         for alien_number in range(number_aliens_x):
 # Create an comrade and place it in the row.
            comrade = Comrade(setting, screen)
            comrade.x = comrade_width + 2 * comrade_width * alien_number
            comrade.rect.x = comrade.x
        
            comrade.rect.y = comrade.rect.height + 2 * comrade.rect.height * row_number
            comrades.add(comrade)

    
    def change_fleet_direction(setting, comrades):
        """Drop the entire fleet and change the fleet's direction."""
        for comrade in comrades.sprites():
            comrade.rect.y += setting.drop_speed
        setting.comrade_direction *= -1


    def check_fleet_edges(setting, comrades):
         """Respond appropriately if any comrades have reached an edge."""
         for comrade in comrades.sprites():
            if comrade.check_edges():
                Events.change_fleet_direction(setting, comrades)
                break
 

    
 
    def update_comrades(setting,stats,screen,bullets,comrades,ship):
        """Check if the fleet is at an edge,and then update the postions of all comrades in the fleet."""
        Events.check_fleet_edges(setting, comrades)
    
        comrades.update()

        """ Look for alien-ship collisions."""
        if pygame.sprite.spritecollideany(ship, comrades):
              #print("Ship hit!!!")
              Events.ship_hit(setting, stats,screen,ship,comrades,bullets)
        
        else:
            """Check if the alien have passed the bottom of the screen"""
            screen2 = screen.get_rect()
            for comrade in comrades.sprites():
                if comrade.rect.bottom >= screen2.bottom:
                     Events.ship_hit(setting, stats,screen,ship,comrades,bullets)



    def ship_hit(settings, stats, screen, ship, comrades, bullets):
          """Respond to ship being hit by alien."""
               # Decrement ships_left.
          stats.ship_left -= 1
 
              # Empty the list of aliens and bullets.
          comrades.empty()
          bullets.empty()
 
              # Create a new fleet and center the ship.
          if stats.ship_left != 0:
              Events.create_fleet(settings, screen, comrades, number_row=3)

              ship.ship_center()
          else:
              sys.exit()
 
              # Pause.
          sleep(1.0)


    def update_screen(screen,my_set,ship,comrades,bullets,number_row):

        if my_set.screen_color == (0,0,120):
            screen.fill(my_set.screen_color)
            
            ship.blitme() 
             # Redraw all bullets behind ship and comrades.
            for bullet in bullets.sprites():
                bullet.draw_bullet()

            # Check for any bullets that have hit aliens.
                # If so, get rid of the bullet and the alien.
            collisions = pygame.sprite.groupcollide(bullets, comrades, True, True)
            comrades.draw(screen)
           
           
        pygame.display.flip()