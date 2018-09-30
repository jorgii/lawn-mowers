import pytest

from models import Grid, Position
from core.exceptions import OutOfBoundsError, InvalidGridCoordinates


class TestGrid(object):
    def test_grid_x_str_value_error(self):
        with pytest.raises(ValueError):
            Grid('foo', 2)

    def test_grid_y_str_value_error(self):
        with pytest.raises(ValueError):
            Grid(2, 'foo')

    def test_invalid_grid_coordinates_x(self):
        with pytest.raises(InvalidGridCoordinates):
            Grid(-1, 0)

    def test_invalid_grid_coordinates_y(self):
        with pytest.raises(InvalidGridCoordinates):
            Grid(0, -1)


class TestPosition(object):
    @pytest.fixture
    def grid(self):
        return Grid(5, 5)

    def test_positions_x_out_of_bounds(self, grid):
        with pytest.raises(OutOfBoundsError):
            Position(6, 5, grid)

    def test_positions_x_out_of_bounds_negative(self, grid):
        with pytest.raises(OutOfBoundsError):
            Position(-1, 5, grid)

    def test_positions_y_out_of_bounds(self, grid):
        with pytest.raises(OutOfBoundsError):
            Position(5, 6, grid)

    def test_positions_y_out_of_bounds_negative(self, grid):
        with pytest.raises(OutOfBoundsError):
            Position(5, -1, grid)

    def test_position_x_str_value_error(self, grid):
        with pytest.raises(ValueError):
            Position('foo', 2, grid)

    def test_position_y_str_value_error(self, grid):
        with pytest.raises(ValueError):
            Position(2, 'foo', grid)

    def test_position_x_y_bounds_lower_left(self, grid):
        position = Position(0, 0, grid)
        assert position.x == 0
        assert position.y == 0

    def test_position_x_y_bounds_lower_right(self, grid):
        position = Position(5, 0, grid)
        assert position.x == 5
        assert position.y == 0

    def test_position_x_y_bounds_upper_left(self, grid):
        position = Position(0, 5, grid)
        assert position.x == 0
        assert position.y == 5

    def test_position_x_y_bounds_upper_right(self, grid):
        position = Position(5, 5, grid)
        assert position.x == 5
        assert position.y == 5
