# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:52:25 2021

@author: Raymart Ballesteros
@date: 4/24/2021
@brief: This is the unittest for the methods in the CatanBoard class
"""

# imports
from CatanBoard import CatanBoard
from CatanTiles import ResourceTypes
from CatanSettlements import Colors
from PyQt5 import QtCore
from configparser import ConfigParser
import pytest


@pytest.fixture
def boardDefault():
    boardDefault = CatanBoard(70.0)
    return boardDefault

@pytest.fixture
def defaultValues():
    fileName = "defaultValues.txt"
    defaultValues = {
        'Vertices': [],
        'Edges': [],
        'uVertices': [],
        'uEdges': []
        # 'Resources': [ResourceTypes.OAR, ResourceTypes.WOOL, ResourceTypes.LUMBER, ResourceTypes.GRAIN,
        #       ResourceTypes.BRICK, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.LUMBER,
        #       ResourceTypes.NONE, ResourceTypes.LUMBER, ResourceTypes.OAR, ResourceTypes.LUMBER, ResourceTypes.OAR,
        #       ResourceTypes.GRAIN, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.WOOL],
        # 'Numbers' : [10, 2, 9, 11,
        #       6, 4, 10, 9, 11,
        #       0, 3, 8, 8, 3,
        #       4, 5, 5, 6, 12]
        }
    
    with open(fileName, "r") as f:
        for line in f:
            vals = line.split("\t")
            if len(vals) == 6:
                defaultValues['Vertices'].append(QtCore.QPointF(float(vals[0]),float(vals[1])))
                defaultValues['Edges'].append([QtCore.QPointF(float(vals[2]),float(vals[3])),
                                           QtCore.QPointF(float(vals[4]),float(vals[5]))])
            elif len(vals) == 2:
                defaultValues['uVertices'].append(QtCore.QPointF(float(vals[0]),float(vals[1])))
            elif len(vals) == 4:
                defaultValues['uEdges'].append([QtCore.QPointF(float(vals[0]),float(vals[1])),
                                           QtCore.QPointF(float(vals[2]),float(vals[3]))])
    
    return defaultValues

@pytest.fixture
def configParams():
    cfgFileName = "defaultConfig.ini"
    cfgParamsDict = {}
    
    parser = ConfigParser()
    parser.read(cfgFileName)
    
    # Retrieve a list of the resources to be assigned to the tiles objects
    cfgParamsDict['Types'] = [ResourceTypes(item) for item in parser.get('Resources', 'Types').split('\n')]
    # Retrieve the parameters for the file names of the images for the tiles
    cfgParamsDict['BRICK'] = parser.get('Resources', 'BRICK')
    cfgParamsDict['GRAIN'] = parser.get('Resources', 'GRAIN')
    cfgParamsDict['LUMBER'] = parser.get('Resources', 'LUMBER')
    cfgParamsDict['OAR'] = parser.get('Resources', 'OAR')
    cfgParamsDict['WOOL'] = parser.get('Resources', 'WOOL')
    cfgParamsDict['NONE'] = parser.get('Resources', 'NONE')
    # Retrieve the list of numbers to be assigned to the tiles objects
    cfgParamsDict['Numbers'] = [int(x) for x in parser.get('Numbers', 'Values').split('\n')]
    
    return cfgParamsDict

        

def test_BoardConstructor_Default(boardDefault, defaultValues):
    # verify all elements of tiles array
    for i in range(19):
        rTile = boardDefault.getATile(i)
        assert rTile.getEdgeLength() == 70.0
        assert rTile.getResourceType() == ResourceTypes.NONE
        assert rTile.getTileValue() == 0
        assert rTile.checkTileHasRobber() == False

        for j in range(6):
            rVertex = rTile.getTileVertex(j)
            assert rVertex.getValue() == 0
            assert rVertex.getColor() == Colors.UNINITIALIZED
            rPosition = rVertex.getCoords()
            assert rPosition == defaultValues['Vertices'][i*6+j]
        
        for k in range(6):
            rEdge = rTile.getTileEdge(k)
            assert rEdge.getColor() == Colors.UNINITIALIZED
            rPoint1, rPoint2 = rEdge.getPoints()
            assert rPoint1 == defaultValues['Edges'][i*6+k][0]
            assert rPoint2 == defaultValues['Edges'][i*6+k][1]
    
    # verify all elements of vertices array
    assert len(boardDefault.m_allVertices) == len(defaultValues['uVertices'])
    for k in range (len(boardDefault.m_allVertices)):
        assert boardDefault.m_allVertices[k] == defaultValues['uVertices'][k]
    
    #verify all elements of edges array
    assert len(boardDefault.m_allEdges) == len(defaultValues['uEdges'])
    for k in range(len(defaultValues['uEdges'])):
        assert boardDefault.m_allEdges[k][0] == defaultValues['uEdges'][k][0]
        assert boardDefault.m_allEdges[k][1] == defaultValues['uEdges'][k][1]


def test_getATile_NotValidIntType(boardDefault):
    with pytest.raises(TypeError):
        boardDefault.getATile(None)


def test_getATile_IndexOutOfRange(boardDefault):
    with pytest.raises(IndexError):
        boardDefault.getATile(-1)


def test_setTileResourceType_OK(boardDefault):
    boardDefault.setTileResourceType(3, ResourceTypes.LUMBER)
    
    rTile = boardDefault.getATile(3)
    assert rTile.getResourceType() == ResourceTypes.LUMBER


def test_setTileResourceType_NotValidIntType(boardDefault):
    with pytest.raises(TypeError):
        boardDefault.setTileResourceType(None, ResourceTypes.LUMBER)


def test_setTileResourceType_IndexOutOfRange(boardDefault):
    with pytest.raises(IndexError):
        boardDefault.setTileResourceType(-1, ResourceTypes.LUMBER)


def test_setTileValue_OK(boardDefault):
    boardDefault.setTileValue(3, 5)
    
    rTile = boardDefault.getATile(3)
    assert rTile.getTileValue() == 5


def test_setTileValue_NotValidIntType(boardDefault):
    with pytest.raises(TypeError):
        boardDefault.setTileValue(None, 5)


def test_setTileValue_IndexOutOfRange(boardDefault):
    with pytest.raises(IndexError):
        boardDefault.setTileValue(-1, 5)


def test_checkValidSettlement_OK(boardDefault, defaultValues):
    rStatusOK = boardDefault.checkValidSettlement(defaultValues['uVertices'][5])
    assert rStatusOK == 1


def test_CheckValidSettlement_LocationInUse(boardDefault, defaultValues):
    _ = boardDefault.placeASettlement(defaultValues['uVertices'][0], Colors.BLUE)
    rStatusInvalid = boardDefault.checkValidSettlement(defaultValues['uVertices'][0])
    assert rStatusInvalid == 0


def test_CheckValidSettlement_NearbySettlement(boardDefault, defaultValues):
    _ = boardDefault.placeASettlement(defaultValues['uVertices'][0], Colors.BLUE)
    rStatusInvalid = boardDefault.checkValidSettlement(defaultValues['uVertices'][1])
    assert rStatusInvalid == 0


def test_CheckValidSettlement_InvalidArgumentType(boardDefault):
    with pytest.raises(TypeError):
        rValue = boardDefault.checkValidSettlement([0.0, -60.0])


def test_placeASettlement_OK(boardDefault, defaultValues):
    rStatus = boardDefault.placeASettlement(defaultValues['uVertices'][3], Colors.BLUE)
    assert rStatus == 0
    
    for p in range(19):
        someTile = boardDefault.getATile(p)
        for q in range(6):
            if someTile.getTileVertex(q).getCoords() == defaultValues['uVertices'][3]:
                someSettlement = someTile.getTileVertex(q)
                assert someSettlement.getValue() == 1


def test_placeASettlement_NotValidPosition(boardDefault, defaultValues):
    _ = boardDefault.placeASettlement(defaultValues['uVertices'][3], Colors.BLUE)
    rStatus = boardDefault.placeASettlement(defaultValues['uVertices'][3], Colors.ORANGE)
    assert rStatus == -1
    
    rStatus = boardDefault.placeASettlement(defaultValues['uVertices'][4], Colors.ORANGE)
    assert rStatus == -1


def test_upgradeToCity_OK(boardDefault, defaultValues):
    _ = boardDefault.placeASettlement(defaultValues['uVertices'][3], Colors.BLUE)
    rStatus = boardDefault.upgradeToCity(defaultValues['uVertices'][3], Colors.BLUE)
    assert rStatus == 0
    
    for p in range(19):
        someTile = boardDefault.getATile(p)
        for q in range(6):
            if someTile.getTileVertex(q).getCoords() == defaultValues['uVertices'][3]:
                someSettlement = someTile.getTileVertex(q)
                assert someSettlement.getValue() == 2


def test_upgradeToCity_NoValidSettlement(boardDefault, defaultValues):
    rStatus = boardDefault.upgradeToCity(defaultValues['uVertices'][3], Colors.BLUE)
    assert rStatus == -1


def test_upgradeToCity_NoMatchingColor(boardDefault, defaultValues):
    _ = boardDefault.placeASettlement(defaultValues['uVertices'][3], Colors.BLUE)
    rStatus = boardDefault.upgradeToCity(defaultValues['uVertices'][3], Colors.RED)
    assert rStatus == -1


def test_generateGameBoard_OK(boardDefault):
    expectedResources = [ResourceTypes.OAR, ResourceTypes.WOOL, ResourceTypes.LUMBER, ResourceTypes.GRAIN,
             ResourceTypes.BRICK, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.LUMBER,
             ResourceTypes.NONE, ResourceTypes.LUMBER, ResourceTypes.OAR, ResourceTypes.LUMBER, ResourceTypes.OAR,
             ResourceTypes.GRAIN, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.WOOL]
    expectedNumbers = [10, 2, 9, 11,
             6, 4, 10, 9, 11,
             0, 3, 8, 8, 3,
             4, 5, 5, 6, 12]
    boardDefault.generateGameBoard()
    
    for k in range(19):
        rTile = boardDefault.getATile(k)
        assert rTile.getResourceType() == expectedResources[k]
        assert rTile.getTileValue() == expectedNumbers[k]
        if rTile.getResourceType() == ResourceTypes.NONE:
            assert rTile.checkTileHasRobber() == True
        else:
            assert rTile.checkTileHasRobber() == False
    
