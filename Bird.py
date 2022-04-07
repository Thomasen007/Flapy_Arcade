from PIL import Image
from arcade import Point
from typing import List, Union, Tuple
import math
import random
from pymunk import autogeometry
import pymunk
from Constants import *


class Bird(arcade.AnimatedTimeBasedSprite):
    
    def __init__(self, center_x, center_y, death_height):
        super().__init__(center_x=center_x, center_y=center_y)
        self.score = 0
        self.textures = []
        rnd = random.SystemRandom()
        color = rnd.choice(list(BIRDS))
        
        for i in range(4):
            self.textures.append(arcade.load_texture(BIRDS[color][i % 3]))

        self.cur_texture_index = 0
        self.vel = 0
        self.dy = 0
        self.death_height = death_height
        self.dead = False

    def set_velocity(self, velocity):
        self.vel = velocity

    def update(self, dt=0):
        if self.dead:
            self.angle = -90
            if self.center_y > self.death_height + self.height//2:
                self.center_y -= 4
            return

        if self.vel > 0:        
            self.center_y += DY
            self.vel -= DY
            if self.angle < 30:
                self.angle = min(self.angle + ANGUP, 30)
        else:
            if self.angle > -90:
                self.angle = max(self.angle + ANGDOWN, -90)
            self.center_y -= GRAVITY

    def flap(self):
        self.vel = JUMP_DY

    def die(self):
        self.dead = True
        arcade.play_sound(SOUNDS['die'])

    def calculate_hit_box_points_detailed(image: Image,
                                      hit_box_detail: float = 4.5)\
        -> Union[List[Point], Tuple[Point, ...]]:


        def sample_func(sample_point: Point) -> int:
            """ Method used to sample image. """
            if sample_point[0] < 0 \
                    or sample_point[1] < 0 \
                    or sample_point[0] >= image.width \
                    or sample_point[1] >= image.height:
                return 0

            point_tuple = sample_point[0], sample_point[1]
            color = image.getpixel(point_tuple)
            if color[3] > 0:
                return 255
            else:
                return 0


        p1 = 0, 0
        p2 = 0, image.height - 1
        p3 = image.width - 1, image.height - 1
        p4 = image.width - 1, 0

        if sample_func(p1) and sample_func(p2) and sample_func(p3) and sample_func(p4):
            p1 = (-image.width / 2, -image.height / 2)
            p2 = (image.width / 2, -image.height / 2)
            p3 = (image.width / 2, image.height / 2)
            p4 = (-image.width / 2, image.height / 2)

            return p1, p2, p3, p4


        logo_bb = pymunk.BB(-1, -1, image.width, image.height)

        line_set = autogeometry.PolylineSet()

        downres = 1
        horizontal_samples = int(image.width / downres)
        vertical_samples = int(image.height / downres)

        line_sets = autogeometry.march_soft(
            logo_bb,
            horizontal_samples, vertical_samples,
            99,
            sample_func)

        if len(line_sets) == 0:
            return []

        selected_line_set = line_sets[0]
        selected_range = None
        if len(line_set) > 1:

            for line in line_set:
                min_x = None
                min_y = None
                max_x = None
                max_y = None
                for point in line:
                    if min_x is None or point.x < min_x:
                        min_x = point.x
                    if max_x is None or point.x > max_x:
                        max_x = point.x
                    if min_y is None or point.y < min_y:
                        min_y = point.y
                    if max_y is None or point.y > max_y:
                        max_y = point.y

                if min_x is None or max_x is None or min_y is None or max_y is None:
                    raise ValueError("No points in bounding box.")

                my_range = max_x - min_x + max_y + min_y
                if selected_range is None or my_range > selected_range:
                    selected_range = my_range
                    selected_line_set = line

        # Reduce number of vertices
        # original_points = len(selected_line_set)
        selected_line_set = autogeometry.simplify_curves(selected_line_set,
                                                        hit_box_detail)
        # downsampled_points = len(selected_line_set)

        # Convert to normal points, offset fo 0,0 is center, flip the y
        hh = image.height / 2
        hw = image.width / 2
        points = []
        for vec2 in selected_line_set:
            point = round(vec2.x - hw), round(image.height - (vec2.y - hh) - image.height)  # type: ignore
            points.append(point)

        if len(points) > 1 and points[0] == points[-1]:
            points.pop()

        # print(f"{sprite.texture.name} Line-sets={len(line_set)}, Original points={original_points}, Downsampled points={downsampled_points}")  # noqa