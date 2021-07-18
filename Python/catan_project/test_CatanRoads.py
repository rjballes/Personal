# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:21:21 2021

@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This is the unittest for the CatanRoads class.
"""

from CatanSettlements import Colors
from CatanRoads import CatanRoads
import pytest

# Create fixture for a default instance of CatanSettlements
@pytest.fixture
def roadDefault():
    roadDefault = CatanRoads(0.0, 0.0, 12.0, -45.0)
    return roadDefault

@pytest.fixture
def orangeRoad():
    orangeRoad = CatanRoads(-45.0, 24.0, 0.0, 54.0, Colors.ORANGE)
    return orangeRoad


def test_Constructor_RoadDefault(roadDefault):
    assert roadDefault.getColor() == Colors.UNINITIALIZED
    
    retPoint1, retPoint2 = roadDefault.getPoints()
    assert retPoint1.x() == 0.0
    assert retPoint1.y() == 0.0
    assert retPoint2.x() == 12.0
    assert retPoint2.y() == -45.0


def test_Constructor_OrangeRoad(orangeRoad):
    assert orangeRoad.getColor() == Colors.ORANGE
    
    retPoint1, retPoint2 = orangeRoad.getPoints()
    assert retPoint1.x() == -45.0
    assert retPoint1.y() == 24.0
    assert retPoint2.x() == 0.0
    assert retPoint2.y() == 54.0


def test_SetColor_NotInRange(roadDefault):
    with pytest.raises(ValueError):
        roadDefault.setColor(Colors.NUM_COLORS)


def test_SetColor_InvalidInputType(roadDefault):
    with pytest.raises(TypeError):
        roadDefault.setColor(None)


def test_SetPoints_InvalidInputInts(roadDefault):
    with pytest.raises(ValueError):
        roadDefault.setPoints(60,60,0.0,10.2)


def test_SetPoints_InvalidInputNotNumber(roadDefault):
    with pytest.raises(ValueError):
        roadDefault.setPoints(60.0,None,0.25,-1.0)
