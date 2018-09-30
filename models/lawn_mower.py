from core.exceptions import UnexpectedOrientation, OutOfBoundsError


class LawnMower(object):
    ORIENTATIONS = ('N', 'E', 'W', 'S')
    ROTATIONS = ('L', 'R')
    ORIENTATION_ROTATIONS = {
        'N': {'L': 'W', 'R': 'E'},
        'E': {'L': 'N', 'R': 'S'},
        'W': {'L': 'S', 'R': 'N'},
        'S': {'L': 'E', 'R': 'W'},
    }
    MOVEMENTS = ('F')
    ORIENTATION_MOVEMENTS = {
        'N': {'F': {'attr': 'y', 'magnitude': 1}},
        'E': {'F': {'attr': 'x', 'magnitude': 1}},
        'W': {'F': {'attr': 'x', 'magnitude': -1}},
        'S': {'F': {'attr': 'y', 'magnitude': -1}},
    }

    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def __repr__(self):
        return 'Lawn Mower at {}:{}:{}'.format(
            self.position.x, self.position.y, self.orientation)

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation not in self.ORIENTATIONS:
            raise UnexpectedOrientation(
                'Unexpected orientation. '
                'Expected values: {}'.format(self.ORIENTATIONS))
        self.__orientation = orientation

    def rotate(self, rotation):
        self.orientation = self.ORIENTATION_ROTATIONS[
            self.orientation][rotation]

    def move(self, movement):
        attr = self.ORIENTATION_MOVEMENTS[self.orientation][movement]['attr']
        magnitude = self.ORIENTATION_MOVEMENTS[
            self.orientation][movement]['magnitude']
        current_attr_value = getattr(self.position, attr)
        try:
            setattr(self.position, attr, current_attr_value + magnitude)
        except OutOfBoundsError:
            pass

    def perform_actions(self, actions):
        for action in actions:
            if action in self.ROTATIONS:
                self.rotate(action)
            elif action in self.MOVEMENTS:
                self.move(action)
