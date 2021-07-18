# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:21:21 2021

@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This is the unittest for the CatanSettlements class.
"""

from CatanSettlements import Colors, CatanSettlements
import pytest

# Create fixture for a default instance of CatanSettlements
@pytest.fixture
def settlementDefault():
    settlementDefault = CatanSettlements(60.0, -35.0)
    return settlementDefault

@pytest.fixture
def blueSettlement():
    blueSettlement = CatanSettlements(-60.0, 145.0, 1, Colors.BLUE)
    return blueSettlement


def test_Constructor_Default(settlementDefault):
    assert settlementDefault.getValue() == 0
    assert settlementDefault.getColor() == Colors.UNINITIALIZED
    retCoords = settlementDefault.getCoords()
    assert retCoords.x() == 60.0
    assert retCoords.y() == -35.0


def test_Constructor_BlueSettlement(blueSettlement):
    assert blueSettlement.getValue() == 1
    assert blueSettlement.getColor() == Colors.BLUE
    retCoords = blueSettlement.getCoords()
    assert retCoords.x() == -60.0
    assert retCoords.y() == 145.0


def test_SetValue_InvalidInput(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setValue(-1)
       
        
def test_SetColor_NotInRange(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setColor(Colors.NUM_COLORS)


def test_SetColor_InvalidInputType(settlementDefault):
    with pytest.raises(TypeError):
        settlementDefault.setColor(None)


def test_SetCoords_InvalidInputInts(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setCoords(60,60)


def test_SetCoords_InvalidInputNotNumber(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setCoords(60.0,None)