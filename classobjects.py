"""
The class of the tools.
"""

import random
from constants import *

class Objects:
    def __init__(self):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def randomize_position(self, level):
        while level[self.case_y][self.case_x] == '0':
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            self.x = self.case_x * SPRITE_SIZE
            self.y = self.case_y * SPRITE_SIZE
