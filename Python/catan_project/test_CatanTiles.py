# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:20:34 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is a unittest for the CatanTiles class.
"""


#imports
from CatanTiles import CatanTiles, ResourceTypes
from CatanSettlements import CatanSettlements, Colors
from CatanRoads import CatanRoads
import pytest



@pytest.fixture
def tileDefault():
    tileDefault = CatanTiles()
    return tileDefault

@pytest.fixture
def forestTile():
    forestTile = CatanTiles(ResourceTypes.LUMBER, 8, False)
    return forestTile

@pytest.fixture
def orangeSettlement():
    orangeSettlement = CatanSettlements(1, Colors.ORANGE)
    return orangeSettlement

@pytest.fixture
def orangeRoad():
    orangeRoad = CatanRoads(Colors.ORANGE)
    return orangeRoad


def test_Constructor_TileDefault(tileDefault):
    assert tileDefault.getResourceType() == ResourceTypes.NONE
    assert tileDefault.getTileValue() == 0
    assert tileDefault.checkTileHasRobber() == False
    
    for i in range(2):
        for j in range(3):
            retVertex = tileDefault.getTileVertex(i, j)
            assert retVertex.getValue() == 0
            assert retVertex.getColor() == Colors.UNINITIALIZED
            
    for i in range(3):
        for j in range(2):
            retEdge = tileDefault.getTileEdge(i, j)
            assert retEdge.getColor() == Colors.UNINITIALIZED


def test_Constructor_ForestTile(forestTile):
    assert forestTile.getResourceType() == ResourceTypes.LUMBER
    assert forestTile.getTileValue() == 8
    assert forestTile.checkTileHasRobber() == False
    
    for i in range(2):
        for j in range(3):
            retVertex = forestTile.getTileVertex(i, j)
            assert retVertex.getValue() == 0
            assert retVertex.getColor() == Colors.UNINITIALIZED
            
    for i in range(3):
        for j in range(2):
            retEdge = forestTile.getTileEdge(i, j)
            assert retEdge.getColor() == Colors.UNINITIALIZED


def test_SetResourceType_Grain(tileDefault):
    tileDefault.setResourceType(ResourceTypes.GRAIN)
    assert tileDefault.getResourceType() == ResourceTypes.GRAIN


def test_SetResourceType_InvalidInput(tileDefault):
    with pytest.raises(ValueError):
        tileDefault.setResourceType(ResourceTypes.NUM_RESOURCES)


def test_SetTileValue(tileDefault):
    tileDefault.setTileValue(6)
    assert tileDefault.getTileValue() == 6


def test_SetTileValue_InvalidInput(tileDefault):
    with pytest.raises(ValueError):
        tileDefault.setTileValue(15)


def test_SetTileHasRobber(tileDefault):
    tileDefault.setTileHasRobber(True)
    assert tileDefault.checkTileHasRobber() == True


def test_SetTileHasRobber_InvalidInput(tileDefault):
    with pytest.raises(ValueError):
        tileDefault.setTileHasRobber(0)
        

def test_SetTileVertex(forestTile, orangeSettlement):
    forestTile.setTileVertex(0, 2, orangeSettlement)
    retVertex = forestTile.getTileVertex(0, 2)
    assert retVertex.getValue() == 1
    assert retVertex.getColor() == Colors.ORANGE
    

def test_SetTileVertex_InvalidRow(forestTile, orangeSettlement):
    with pytest.raises(ValueError):
        forestTile.setTileVertex(-1, 2, orangeSettlement)
        

def test_SetTileVertex_InvalidCol(forestTile, orangeSettlement):
    with pytest.raises(ValueError):
        forestTile.setTileVertex(0, 5, orangeSettlement)
        

def test_SetTileVertex_InvalidSettlement(forestTile):
    with pytest.raises(ValueError):
        forestTile.setTileVertex(0, 2, None)

    
def test_SetTileEdge(forestTile, orangeRoad):
    forestTile.setTileEdge(0, 1, orangeRoad)
    retEdge = forestTile.getTileEdge(0, 1)
    assert retEdge.getColor() == Colors.ORANGE


def test_SetTileEdge_InvalidRow(forestTile, orangeRoad):
    with pytest.raises(ValueError):
        forestTile.setTileEdge(-1, 1, orangeRoad)
        

def test_SetTileEdge_InvalidCol(forestTile, orangeRoad):
    with pytest.raises(ValueError):
        forestTile.setTileEdge(0, 5, orangeRoad)
        

def test_SetTileEdge_InvalidRoad(forestTile):
    with pytest.raises(ValueError):
        forestTile.setTileEdge(0, 1, None)
