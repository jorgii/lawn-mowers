import argparse

from models import Grid, Position, LawnMower
from utils import parse_file

parser = argparse.ArgumentParser(description='Lawn mowers processor.')
parser.add_argument('lm_data_file', metavar='lm-data-file', type=str,
                    help='Lawn mowers data file locations.')
args = parser.parse_args()


if __name__ == '__main__':
    parse_data = parse_file(args.lm_data_file)
    grid = Grid(*parse_data['grid'])
    lm_actions = []
    for lm in parse_data['lawn_mowers']:
        position = Position(*lm['position'], grid=grid)
        orientation = lm['orientation']
        lm_actions.append([LawnMower(position, orientation), lm['actions']])
    for lawn_mower, actions in lm_actions:
        lawn_mower.perform_actions(actions)
        print(
            lawn_mower.position.x,
            lawn_mower.position.y,
            lawn_mower.orientation)
