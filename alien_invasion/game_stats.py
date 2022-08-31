class Gamestats():

    def __init__(self,setting) -> None:
        pass
        self.setting = setting
        self.reset_stat()

    def reset_stat(self):
        print()
        self.ship_left = self.setting.ship_limit