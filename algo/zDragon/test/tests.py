# coding: utf8

import pytest

# the lsystem function returns actions for maximun recursion depth
# e.g. lsystem(2) == 'F+F++-F-F+'
from dragon import lsystem

# read actions for differents depths
with open('../dragon.txt', 'r', newline='\n') as fp:
    actions = [line.strip() for line in fp]

@pytest.mark.parametrize(
    'depth, actions', list(enumerate(actions))
)

# valid grids test
def test_dragon(depth, actions):
    assert lsystem(depth) == actions

