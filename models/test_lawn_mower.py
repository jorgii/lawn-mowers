import pytest

from models import LawnMower, Grid, Position
from core.exceptions import UnexpectedOrientation


class TestLawnMower(object):
    @pytest.fixture
    def position_1_1(self):
        grid = Grid(5, 5)
        return Position(1, 1, grid)

    @pytest.fixture
    def position_0_0(self):
        grid = Grid(5, 5)
        return Position(0, 0, grid)

    @pytest.fixture
    def position_0_5(self):
        grid = Grid(5, 5)
        return Position(0, 5, grid)

    @pytest.fixture
    def position_5_5(self):
        grid = Grid(5, 5)
        return Position(5, 5, grid)

    @pytest.fixture
    def position_5_0(self):
        grid = Grid(5, 5)
        return Position(5, 0, grid)

    def test_unexpected_orientation(self, position_1_1):
        with pytest.raises(UnexpectedOrientation):
            LawnMower(position_1_1, 'foo')

    def test_n_orientation(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'N')
        assert lawn_mower.orientation == 'N'

    def test_e_orientation(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'E')
        assert lawn_mower.orientation == 'E'

    def test_w_orientation(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'W')
        assert lawn_mower.orientation == 'W'

    def test_s_orientation(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'S')
        assert lawn_mower.orientation == 'S'

    def test_rotate_n_l(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'N')
        lawn_mower.rotate('L')
        assert lawn_mower.orientation == 'W'

    def test_rotate_n_r(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'N')
        lawn_mower.rotate('R')
        assert lawn_mower.orientation == 'E'

    def test_rotate_e_l(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'E')
        lawn_mower.rotate('L')
        assert lawn_mower.orientation == 'N'

    def test_rotate_e_r(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'E')
        lawn_mower.rotate('R')
        assert lawn_mower.orientation == 'S'

    def test_rotate_w_l(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'W')
        lawn_mower.rotate('L')
        assert lawn_mower.orientation == 'S'

    def test_rotate_w_r(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'W')
        lawn_mower.rotate('R')
        assert lawn_mower.orientation == 'N'

    def test_rotate_s_l(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'S')
        lawn_mower.rotate('L')
        assert lawn_mower.orientation == 'E'

    def test_rotate_s_r(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'S')
        lawn_mower.rotate('R')
        assert lawn_mower.orientation == 'W'

    def test_move_1_1_n(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'N')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 1
        assert lawn_mower.position.y == 2

    def test_move_1_1_e(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'E')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 2
        assert lawn_mower.position.y == 1

    def test_move_1_1_w(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'W')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 1

    def test_move_1_1_s(self, position_1_1):
        lawn_mower = LawnMower(position_1_1, 'S')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 1
        assert lawn_mower.position.y == 0

    def test_move_0_0_n(self, position_0_0):
        lawn_mower = LawnMower(position_0_0, 'N')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 1

    def test_move_0_0_e(self, position_0_0):
        lawn_mower = LawnMower(position_0_0, 'E')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 1
        assert lawn_mower.position.y == 0

    def test_move_0_0_w(self, position_0_0):
        lawn_mower = LawnMower(position_0_0, 'W')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 0

    def test_move_0_0_s(self, position_0_0):
        lawn_mower = LawnMower(position_0_0, 'S')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 0

    def test_move_0_5_n(self, position_0_5):
        lawn_mower = LawnMower(position_0_5, 'N')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 5

    def test_move_0_5_e(self, position_0_5):
        lawn_mower = LawnMower(position_0_5, 'E')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 1
        assert lawn_mower.position.y == 5

    def test_move_0_5_w(self, position_0_5):
        lawn_mower = LawnMower(position_0_5, 'W')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 5

    def test_move_0_5_s(self, position_0_5):
        lawn_mower = LawnMower(position_0_5, 'S')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 0
        assert lawn_mower.position.y == 4

    def test_move_5_5_n(self, position_5_5):
        lawn_mower = LawnMower(position_5_5, 'N')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 5

    def test_move_5_5_e(self, position_5_5):
        lawn_mower = LawnMower(position_5_5, 'E')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 5

    def test_move_5_5_w(self, position_5_5):
        lawn_mower = LawnMower(position_5_5, 'W')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 4
        assert lawn_mower.position.y == 5

    def test_move_5_5_s(self, position_5_5):
        lawn_mower = LawnMower(position_5_5, 'S')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 4

    def test_move_5_0_n(self, position_5_0):
        lawn_mower = LawnMower(position_5_0, 'N')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 1

    def test_move_5_0_e(self, position_5_0):
        lawn_mower = LawnMower(position_5_0, 'E')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 0

    def test_move_5_0_w(self, position_5_0):
        lawn_mower = LawnMower(position_5_0, 'W')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 4
        assert lawn_mower.position.y == 0

    def test_move_5_0_s(self, position_5_0):
        lawn_mower = LawnMower(position_5_0, 'S')
        lawn_mower.move('F')
        assert lawn_mower.position.x == 5
        assert lawn_mower.position.y == 0
