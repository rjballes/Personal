# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:20:34 2021

@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This is a unittest for the CatanTiles class.
"""


#imports
from CatanTiles import CatanTiles, ResourceTypes
from CatanSettlements import CatanSettlements, Colors
from CatanRoads import CatanRoads
from PyQt5 import QtCore
import pytest



@pytest.fixture
def tileDefault():
    tileDefault = CatanTiles(0, 1, 70.0)
    return tileDefault

@pytest.fixture
def forestTile():
    forestTile = CatanTiles(0, 1, 70.0, ResourceTypes.LUMBER, 8, False)
    return forestTile

@pytest.fixture
def orangeSettlement():
    orangeSettlement = CatanSettlements(-60.0, 145.0, 1, Colors.ORANGE)
    return orangeSettlement

@pytest.fixture
def orangeRoad():
    orangeRoad = CatanRoads(-60.0, 0.0, -10.0, 40.0, Colors.ORANGE)
    return orangeRoad

@pytest.fixture
def defaultValues():
    defaultValues = {
        'Vertex': [[60.62177826491071, -35.00000000000003],
                   [7.105427357601002e-15, -2.1316282072803006e-14],
                   [-1.0039627830461944e-14, 69.99999999999997],
                   [60.62177826491071, 104.99999999999994],
                   [121.24355652982145, 70.0],
                   [121.24355652982148, 0.0]],
        'Edge': [[[48.49742261192857, -28.00000000000003],[12.124355652982148, -7.000000000000023]],
                 [[3.676416319988413e-15, 13.999999999999979],[-6.610616792849355e-15, 55.99999999999997]],
                 [[12.124355652982132, 76.99999999999997],[48.49742261192857, 97.99999999999994]],
                 [[72.74613391789286, 97.99999999999996],[109.1192008768393, 76.99999999999999]],
                 [[121.24355652982145, 56.0],[121.24355652982148, 14.0]],
                 [[109.11920087683933, -7.000000000000005],[72.74613391789286, -28.00000000000002]]]
        }
    return defaultValues


def test_Constructor_TileDefault(tileDefault, defaultValues):
    assert tileDefault.getEdgeLength() == 70.0
    assert tileDefault.getResourceType() == ResourceTypes.NONE
    assert tileDefault.getTileValue() == 0
    assert tileDefault.checkTileHasRobber() == False
    
    for i in range(6):
        retVertex = tileDefault.getTileVertex(i)
        assert retVertex.getValue() == 0
        assert retVertex.getColor() == Colors.UNINITIALIZED
        retCoord = retVertex.getCoords()
        assert retCoord.x() == defaultValues['Vertex'][i][0]
        assert retCoord.y() == defaultValues['Vertex'][i][1]
            
    for i in range(6):
        retEdge = tileDefault.getTileEdge(i)
        assert retEdge.getColor() == Colors.UNINITIALIZED
        retP1, retP2 = retEdge.getPoints()
        assert retP1.x() == defaultValues['Edge'][i][0][0]
        assert retP1.y() == defaultValues['Edge'][i][0][1]
        assert retP2.x() == defaultValues['Edge'][i][1][0]
        assert retP2.y() == defaultValues['Edge'][i][1][1]


def test_Constructor_ForestTile(forestTile, defaultValues):
    assert forestTile.getEdgeLength() == 70.0
    assert forestTile.getResourceType() == ResourceTypes.LUMBER
    assert forestTile.getTileValue() == 8
    assert forestTile.checkTileHasRobber() == False
    
    for i in range(6):
        retVertex = forestTile.getTileVertex(i)
        assert retVertex.getValue() == 0
        assert retVertex.getColor() == Colors.UNINITIALIZED
        retCoord = retVertex.getCoords()
        assert retCoord.x() == defaultValues['Vertex'][i][0]
        assert retCoord.y() == defaultValues['Vertex'][i][1]
            
    for i in range(6):
        retEdge = forestTile.getTileEdge(i)
        assert retEdge.getColor() == Colors.UNINITIALIZED
        retP1, retP2 = retEdge.getPoints()
        assert retP1.x() == defaultValues['Edge'][i][0][0]
        assert retP1.y() == defaultValues['Edge'][i][0][1]
        assert retP2.x() == defaultValues['Edge'][i][1][0]
        assert retP2.y() == defaultValues['Edge'][i][1][1]


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
        

def test_UpdateTileVertex(forestTile, defaultValues):
    forestTile.updateTileVertex(0, 1, Colors.ORANGE)
    retVertex = forestTile.getTileVertex(0)
    assert retVertex.getValue() == 1
    assert retVertex.getColor() == Colors.ORANGE
    retCoord = retVertex.getCoords()
    assert retCoord.x() == defaultValues['Vertex'][0][0]
    assert retCoord.y() == defaultValues['Vertex'][0][1]
    
    forestTile.updateTileVertex(0, 2)
    retVertex = forestTile.getTileVertex(0)
    assert retVertex.getValue() == 2
    assert retVertex.getColor() == Colors.ORANGE
    retCoord = retVertex.getCoords()
    assert retCoord.x() == defaultValues['Vertex'][0][0]
    assert retCoord.y() == defaultValues['Vertex'][0][1]
    

def test_UpdateTileVertex_InvalidNegativeIndex(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileVertex(-1, 1, Colors.ORANGE)
        

def test_UpdateTileVertex_InvalidNegativeValue(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileVertex(0, -1, Colors.ORANGE)


def test_UpdateTileVertex_InvalidLargeValue(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileVertex(0, 5, Colors.ORANGE)
        

def test_UpdateTileVertex_InvalidNoneColor(forestTile):
    with pytest.raises(TypeError):
        forestTile.updateTileVertex(0, 1, None)


def test_UpdateTileVertex_InvalidLargeColor(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileVertex(0, 1, Colors.NUM_COLORS)

    
def test_UpdateTileEdge(forestTile, defaultValues):
    forestTile.updateTileEdge(0, Colors.ORANGE)
    retEdge = forestTile.getTileEdge(0)
    assert retEdge.getColor() == Colors.ORANGE
    retP1, retP2 = retEdge.getPoints()
    assert retP1.x() == defaultValues['Edge'][0][0][0]
    assert retP1.y() == defaultValues['Edge'][0][0][1]
    assert retP2.x() == defaultValues['Edge'][0][1][0]
    assert retP2.y() == defaultValues['Edge'][0][1][1]


def test_UpdateTileEdge_InvalidNegativeIndex(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileEdge(-1, Colors.ORANGE)
        

def test_UpdateTileEdge_InvalidNoneColor(forestTile):
    with pytest.raises(TypeError):
        forestTile.updateTileEdge(0, None)
        

def test_UpdateTileEdge_InvalidLargeColor(forestTile):
    with pytest.raises(ValueError):
        forestTile.updateTileEdge(0, Colors.NUM_COLORS)


def test_FindVertexIdFromPoint_ValidInput(forestTile):
    samplePoint = QtCore.QPointF(60.62177826491071, 104.99999999999994)
    retId = forestTile.findVertexIdFromPoint(samplePoint)
    assert retId == 3
    

def test_FindVertexIdFromPoint_InvalidInputType(forestTile):
    samplePoint = None
    with pytest.raises(TypeError):
        forestTile.findVertexIdFromPoint(samplePoint)
        
        
def test_FindVertexIdFromPoint_PointNotFound(forestTile):
    samplePoint = QtCore.QPointF(242.4871130596429, 0.0)
    retId = forestTile.findVertexIdFromPoint(samplePoint)
    assert retId == -1


def test_FindEdgeIdFromPoints_ValidInput(forestTile):
    samplePoint1 = QtCore.QPointF(60.62177826491071, 104.99999999999994)
    samplePoint2 = QtCore.QPointF(121.24355652982145, 70.0)
    retId = forestTile.findEdgeIdFromPoints(samplePoint1, samplePoint2)
    assert retId == 3
    
    samplePoint2 = QtCore.QPointF(60.62177826491071, 104.99999999999994)
    samplePoint1 = QtCore.QPointF(121.24355652982145, 70.0)
    retId = forestTile.findEdgeIdFromPoints(samplePoint1, samplePoint2)
    assert retId == 3
    

def test_FindEdgeIdFromPoints_PointNotOnTile(forestTile):
    samplePoint1 = QtCore.QPointF(242.48711305964287, 70.0)
    samplePoint2 = QtCore.QPointF(242.4871130596429, 0.0)
    with pytest.raises(ValueError):
        forestTile.findEdgeIdFromPoints(samplePoint1, samplePoint2)
        

def test_FindEdgeIdFromPoints_InvalidInputType(forestTile):
    samplePoint1 = QtCore.QPointF(60.62177826491071, 104.99999999999994)
    samplePoint2 = None
    with pytest.raises(TypeError):
        forestTile.findEdgeIdFromPoints(samplePoint1, samplePoint2)
        
