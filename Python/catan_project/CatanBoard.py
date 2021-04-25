# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:51:16 2021

@package: CatanBoard
@author: Raymart Ballesteros
@date: 4/24/2021
@brief: This contains the classes to represent the Catan board
"""

# imports
from CatanSettlements import CatanSettlements, Colors
from CatanRoads import CatanRoads
from CatanTiles import CatanTiles, ResourceTypes


class CatanBoard:
    def __init__(self):
        self.m_allTiles = []
        for i in range(5):
            self.m_allTiles.append([])
            for j in range(5):
                if (i == 0 or i == 4) and (j == 3 or j == 4):
                    self.m_allTiles[i].append(None)
                elif (i == 1 or i == 3) and (j == 4):
                    self.m_allTiles[i].append(None)
                else:
                    tmp = CatanTiles()
                    self.m_allTiles[i].append(tmp)

        self.m_allVertices = []
        for i in range(6):
            self.m_allVertices.append([])
            for j in range(11):
                tmp = CatanSettlements()
                self.m_allVertices[i].append(tmp)

        self.m_allEdges = []
        for i in range(11):
            self.m_allEdges.append([])
            for j in range(16):
                tmp = CatanRoads()
                self.m_allEdges[i].append(tmp)
    
    
    """
    getATile(row, col)
    -------------------
    Inputs
    row  An int for the row number for the desired tile
    col  An int for the column number for the desired tile
    """
    def getATile(self, row, col):
        # validate inputs
        if (row < 0) or (row > 4):
            raise ValueError("Did not provide a valid input for the row of tiles...")
        elif (col < 0) or (col > 4):
            raise ValueError("Did not provide a valid input for the column of tiles...")
        
        return self.m_allTiles[row][col]
    
    
    """
    setATile(row, col, aTile)
    -------------------
    
    Inputs
    row  An int for the row number for the desired tile
    col  An int for the column number for the desired tile
    aTile A CatanTiles instance 
    """
    def setATile(self, row, col, aTile):
        pass
    
    
    """
    getAVertex(row, col)
    -------------------
    
    Inputs
    row  An int for the row number for the desired vertex
    col  An int for the column number for the desired vertex
    
    Returns
    self.m_allVertices[row][col]  Returns an instance of CatanSettlements
    """
    def getAVertex(self, row, col):
        # validate inputs
        if (row < 0) or (row > 5):
            raise ValueError("Did not provide a valid input for the row of vertices...")
        elif (col < 0) or (col > 10):
            raise ValueError("Did not provide a valid input for the column of vertices...")
        
        return self.m_allVertices[row][col]
    
    
    """
    setAVertex(row, col, aSettlement)
    ------------------
    
    Inputs
    row  An int for the row number for the desired vertex
    col  An into for the column number for the desired vertex
    aSettlement  An instance of CatanSettlements
    """
    def setAVertex(self, row, col, aSettlement):
        pass
    
    
    """
    getAnEdge(row, col)
    -------------------
    
    Inputs
    row  An int for the row number for the desired edge/road
    col  An int for the column number for the desired edge/road
    
    Returns
    self.m_allEdges[row][col]  Returns an instance of CatanRoads
    """
    def getAnEdge(self, row, col):
        # validate inputs
        if (row < 0) or (row > 10):
            raise ValueError("Did not provide a valid input for the row of edges...")
        elif (col < 0) or (col > 15):
            raise ValueError("Did not provide a valid input for the column of edges...")
        
        return self.m_allEdges[row][col]
    
    
    """
    setAnEdge(row, col, aRoad)
    ------------------
    
    Inputs
    row  An int for the row number for the desired edge/road
    col  An into for the column number for the desired edge/road
    aSettlement  An instance of CatanRoads
    """
    def setAnEdge(self, row, col, aSettlement):
        pass
