from turtle import bgcolor


class Setting():

    def __init__(self):

        
        self.screen_width = 1350
        self.screen_height = 700
        self. screen_color = (225,225,225)

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 4
        self.bullet_height = 15

        self.bullet_color = 210, 100, 0
        self.bullet_allowed =3

        # Comrade Setting
        self.comrade_speed = 0.5
        self.comrade_direction = +5
        self.drop_speed = +10

        # Ship setting
        self.ship_limit = 3