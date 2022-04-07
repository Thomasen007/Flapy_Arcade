import random
# BAD PRACTICE IN 3.. 2.. 1.. GO!
from Constants import *

pipe = random.choice(PIPES)


class Pipe(arcade.Sprite):

    def __init__(self, image, scale=1):
    
        super().__init__(image, scale)
        self.horizontal_speed = -1
        self.scored = False

    @classmethod
    def random_pipe_obstacle(cls, sprites, height):
        
        bottom_pipe = cls(pipe)
        bottom_pipe.top = random.randrange(sprites['base'].height + MIN_HEIGHT, height - GAP_SIZE - MIN_HEIGHT)
        bottom_pipe.left = sprites['background'].width

        top_pipe = cls(pipe)
        top_pipe.angle = 180
        top_pipe.left = sprites['background'].width
        top_pipe.bottom = bottom_pipe.top + GAP_SIZE

        return bottom_pipe, top_pipe

    def update(self):
        self.center_x += self.horizontal_speed