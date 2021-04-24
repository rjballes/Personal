# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:20:34 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is a unittest for the CatanTiles class.
"""


#imports
from CatanTiles import CatanTiles, ResourceTypes
import pytest



@pytest.fixture
def tileDefault():
    tileDefault = CatanTiles()
    return tileDefault


def test_Constructor_TileDefault(tileDefault):
    assert tileDefault.getResourceType() == ResourceTypes.NONE
