import math
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 600
BACKGROUND_COLOR = [0, 75, 0]
CUBE_COLOR = [0, 100, 200]
CUBE_VALUE_COLOR = [255, 255, 255]
CUBE_LENGTH = 40
POINT_RADIUS = 4

background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


class Cube:
    @staticmethod
    def coordinates(alfa):
        rotation = [0, 0, 0, 0]
        rotation[0] = int(math.cos(math.radians(alfa)) * CUBE_LENGTH)
        rotation[2] = int(math.sin(math.radians(alfa)) * CUBE_LENGTH)
        rotation[1] = int(math.cos(math.radians(90 - alfa)) * CUBE_LENGTH)
        rotation[3] = int(math.sin(math.radians(90 - alfa)) * CUBE_LENGTH)
        return rotation

    def cube(self, x, y, alfa):
        rotation = self.coordinates(alfa)
        pygame.draw.polygon(background, CUBE_COLOR,
                            [[x, y], [x + rotation[0], y - rotation[2]],
                             [x + (rotation[0] + rotation[2]), y - (rotation[2] - rotation[0])],
                             [x + rotation[1], y + rotation[3]]])
        return rotation

    def point(self, x, y, alfa, pi, coordinate_x, coordinate_y, size):
        rotation = self.coordinates(alfa)
        pygame.draw.circle(background, CUBE_VALUE_COLOR,
                           (int((x + (x + (rotation[0] + rotation[2]))) / 2) + int(
                               math.cos(math.radians(alfa) + pi) * 1.5 * coordinate_x),
                            int((y + (y - (rotation[2] - rotation[0]))) / 2) + int(
                                math.sin(math.radians(alfa) + pi) * 1.5 * coordinate_y)),
                           size)

    def cube_with_value_one(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, 0, 0, 0, POINT_RADIUS)

    def cube_with_value_two(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, (math.pi * 3) / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, (math.pi * 3) / 4, -10, 10, POINT_RADIUS)

    def cube_with_value_three(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, (math.pi * 3) / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, (math.pi * 3) / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, 0, 0, 0, POINT_RADIUS)

    def cube_with_value_four(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, (math.pi * 3) / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, (math.pi * 3) / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, -10, 10, POINT_RADIUS)

    def cube_with_value_five(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, (math.pi * 3) / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, (math.pi * 3) / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, 0, 0, 0, POINT_RADIUS)

    def cube_with_value_six(self, x, y, alfa):
        self.cube(x, y, alfa)
        self.point(x, y, alfa, (math.pi * 3) / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, (math.pi * 3) / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, 10, -10, POINT_RADIUS)
        self.point(x, y, alfa, math.pi / 4, -10, 10, POINT_RADIUS)
        self.point(x, y, alfa, 0, -7.5, 7.5, POINT_RADIUS)
        self.point(x, y, alfa, 0, 7.5, -7.5, POINT_RADIUS)
