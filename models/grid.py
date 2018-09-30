from core.exceptions import OutOfBoundsError, InvalidGridCoordinates


class Grid(object):
    START_X = 0
    START_Y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        x = int(x)
        if x < self.START_X:
            raise(InvalidGridCoordinates)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        y = int(y)
        if y < self.START_Y:
            raise(InvalidGridCoordinates)
        self.__y = y

    @property
    def boundaries(self):
        return '[{}:{}] - [{}:{}]'.format(
            self.START_X,
            self.START_Y,
            self.x,
            self.y
        )


class Position(object):

    def __init__(self, x, y, grid):
        self.grid = grid
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        x = int(x)
        if x > self.grid.x or x < self.grid.START_X:
            raise OutOfBoundsError(
                'X ({}) is outside of grid boundaries '
                '({})'.format(x, self.grid.boundaries))
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        y = int(y)
        if y > self.grid.y or y < self.grid.START_Y:
            raise OutOfBoundsError(
                'Y ({}) is outside of grid boundaries '
                '({})'.format(y, self.grid.boundaries))
        self.__y = y
