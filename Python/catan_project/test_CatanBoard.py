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
import pytest


@pytest.fixture
def boardDefault():
    boardDefault = CatanBoard()
    return boardDefault


def test_BoardConstructor_Default(boardDefault):
    # verify all elements of tiles array
    for i in range(5):
        for j in range(5):
            if (i == 0 or i == 4) and (j == 3 or j == 4):
                assert boardDefault.getATile(i, j) == None
            elif (i == 1 or i == 3) and (j == 4):
                assert boardDefault.getATile(i, j) == None
            else:
                retTile = boardDefault.getATile(i, j)
                assert retTile.getResourceType() == ResourceTypes.NONE
                assert retTile.getTileValue() == 0
                assert retTile.checkTileHasRobber() == False
    
                for m in range(2):
                    for n in range(3):
                        retVertex = retTile.getTileVertex(m, n)
                        assert retVertex.getValue() == 0
                        assert retVertex.getColor() == Colors.UNINITIALIZED
            
                for m in range(3):
                    for n in range(2):
                        retEdge = retTile.getTileEdge(m, n)
                        assert retEdge.getColor() == Colors.UNINITIALIZED
    
    # verify all elements of vertices array
    for i in range(6):
        for j in range(11):
            retVertex = boardDefault.getAVertex(i, j)
            assert retVertex.getValue() == 0
            assert retVertex.getColor() == Colors.UNINITIALIZED
    
    #verify all elements of edges array
    for i in range(11):
        for j in range(16):
            retEdge = boardDefault.getAnEdge(i, j)
            assert retEdge.getColor() == Colors.UNINITIALIZED
