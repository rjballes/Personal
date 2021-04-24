# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:21:21 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is the unittest for the CatanRoads class.
"""

from CatanSettlements import Colors
from CatanRoads import CatanRoads
import pytest

# Create fixture for a default instance of CatanSettlements
@pytest.fixture
def roadDefault():
    roadDefault = CatanRoads()
    return roadDefault

@pytest.fixture
def orangeRoad():
    orangeRoad = CatanRoads(Colors.ORANGE)
    return orangeRoad

def test_Constructor_RoadDefault(roadDefault):
    assert roadDefault.getColor() == Colors.UNINITIALIZED

def test_Constructor_OrangeRoad(orangeRoad):
    assert orangeRoad.getColor() == Colors.ORANGE

def test_SetColor_InvalidInput(roadDefault):
    with pytest.raises(ValueError):
        roadDefault.setColor(Colors.NUM_COLORS)