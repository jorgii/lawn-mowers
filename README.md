# Lawn Mowers Processor

[![Build Status](https://travis-ci.org/jorgii/lawn-mowers.svg?branch=master)](https://travis-ci.org/jorgii/lawn-mowers)


## Requirements

* python >= 3
* pip (to run unit tests)

## Run Application

```sh
python main.py test_actions.txt
```

## Run Tests

```sh
pip install pytest
pytest
```

# Task Description

The position of the mower can be represented by coordinates (x,y) and by a letter giving the cardinal direction (N,E,W,S). The lawn is divided into a grid to simplify the navigation. For example, a mower position can be « 0, 0, N », it means that this mower is located at the lower-left corner of the lawn, and it is oriented North.

The mower is controlled by sending it a sequence of letters. Possible letters are « R », « L » and « F ». « R » and « L » make the mower rotate of 90° respectively to the left or to the right, without moving. « F » mean```s that the mower is moving forward on the cell in front of it, without changing its orientation.

If the position after the move is outside the lawn, then the mower do not move, it keeps its orientation and process the next command.

The cell directly at North of the position (x, y) has for coordinates (x, y+1).

An input file following these rules is given to program the mower:

The first line is the coordinates of the upper-right corner of the lawn, coordinates of lowerleft corner are supposed to be (0,0)

Next lines of the file drive all mowers. There are two lines for each mower:

First line give the initial position and orientation of the mower. Position and orientation are given by 2 numbers and a letter, separated by a space

Second line is a sequence of instruction driving the mower across the lawn. Instructions are a sequence of letters without space.

Each mower moves sequentially, it means that the second mower moves only after the first one execute all its instructions.

When the mower has executed all its instructions, it outputs its position and orientation.

##### GOAL
Design and write a program implementing the above specifications and validating the following test.

##### TEST
**This file is given in input**:
5 5
1 2 N
LFLFLFLFF
3 3 E
FFRFFRFRRF

**This output is expected (final positions of mowers)**:
1 3 N
5 1 E

