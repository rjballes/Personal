# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:21:21 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is the unittest for the CatanSettlements class.
"""

from CatanSettlements import Colors, CatanSettlements
import pytest

# Create fixture for a default instance of CatanSettlements
@pytest.fixture
def settlementDefault():
    settlementDefault = CatanSettlements()
    return settlementDefault

@pytest.fixture
def blueSettlement():
    blueSettlement = CatanSettlements(1, Colors.BLUE)
    return blueSettlement

def test_Constructor_Default(settlementDefault):
    assert settlementDefault.getValue() == 0
    assert settlementDefault.getColor() == Colors.UNINITIALIZED

def test_Constructor_BlueSettlement(blueSettlement):
    assert blueSettlement.getValue() == 1
    assert blueSettlement.getColor() == Colors.BLUE

def test_SetValue_InvalidInput(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setValue(-1)
        
def test_SetColor_InvalidInput(settlementDefault):
    with pytest.raises(ValueError):
        settlementDefault.setColor(Colors.NUM_COLORS)