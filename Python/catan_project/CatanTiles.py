# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:20:32 2021

@package: CatanTiles
@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This contains the class definitions related to the Catan tiles on the board.
"""

# imports
import enum
from CatanSettlements import Colors, CatanSettlements
from CatanRoads import CatanRoads



"""
@class: ResourceTypes(enum.Enum)
@brief: This is an enum class containing the different resource types in the game.
"""
class ResourceTypes(enum.Enum):
    BRICK = 0
    GRAIN = 1
    LUMBER = 2
    OAR = 3
    WOOL = 4
    NUM_RESOURCES = 5
    NONE = -1
    LOWER = NONE
    UPPER = WOOL



"""
@class: CatanTiles
@brief: This is a class to represent 
"""
class CatanTiles:
    """
    Constructor
    ------------------
    
    Parameters
    aResourceType  An instance of the ResourceTypes enum to indicate the type 
                   of resource for the game tile
    
    aValue  An integer for the dice value with which players collect this resource
    
    aHasRobber  A boolean value indicating whether or not the robber is on the tile
    """
    def __init__(self, aResourceType=ResourceTypes.NONE, aValue=0, aHasRobber=False):
        self.m_resourceType = aResourceType
        self.m_tileValue = aValue
        self.m_tileHasRobber = aHasRobber
        
        # initialize lists for the vertices and edges of tile
        self.m_tileVertices = []
        for i in range(2):
            self.m_tileVertices.append([])
            for j in range(3):
                tmp = CatanSettlements()
                self.m_tileVertices[i].append(tmp)
        
        self.m_tileEdges = []
        for i in range(3):
            self.m_tileEdges.append([])
            for j in range(2):
                tmp = CatanRoads()
                self.m_tileEdges[i].append(tmp)
                
                
    """
    getResourceType()
    ----------------
    
    Returns
    self.m_resourceType  An enum for the resource types in the game
    """
    def getResourceType(self):
        return self.m_resourceType
    
    
    """
    setResourceType()
    ----------------
    
    Inputs
    aResourceType  A ResourceTypes enum value to assign the tiles resource
    """
    def setResourceType(self, aResourceType):
        # valid that the input is a valid resource type
        if (aResourceType.value < ResourceTypes.LOWER.value) or (aResourceType.value > ResourceTypes.UPPER.value):
            raise ValueError("Did not provide a valid resource type...")

        self.m_resourceType = aResourceType
    
    
    """
    getTileValue()
    ---------------
    
    Returns
    self.m_tileValue  An integer of the dice value for the tile
    """
    def getTileValue(self):
        return self.m_tileValue
    
    
    """
    setTileValue()
    ---------------
    
    Inputs
    aValue  An integer of the dice value for the tile
    """
    def setTileValue(self, aValue):
        # validate valid input for tile value
        if (aValue < 0) or (aValue > 12):
            raise ValueError("Did not provide a valid input for tile value...")

        self.m_tileValue = aValue
    
    
    """
    checkTileHasRobber()
    ----------------
    
    Returns
    self.m_tileHasRobber  A boolean value indicating if the robber is on the tile
    """
    def checkTileHasRobber(self):
        return self.m_tileHasRobber
    
    
    """
    setTileHasRobber()
    ----------------
    
    Input
    aHasRobber  A boolean value indicating if the robber is on the tile
    """
    def setTileHasRobber(self, aHasRobber):
        # validate vaid input
        if type(aHasRobber) != bool:
            raise ValueError("Did not provide valid boolean input...")

        self.m_tileHasRobber = aHasRobber
    
    
    """
    getTileVertex(row, col)
    ----------------
    
    Inputs
    row  An integer for the row index for the tile grid of vertices
    
    col  An integer for the col index for the tile grid of vertices
    
    Returns
    self.m_tileVertices[row][col]  The object at that vertex of the tile.
    """
    def getTileVertex(self, row, col):
        return self.m_tileVertices[row][col]
    
    
    """
    setTileVertex(row, col, aSettlement)
    ----------------
    
    Inputs
    row  An integer for the row index for the tile grid of vertices
    
    col  An integer for the col index for the tile grid of vertices
    
    aSettlement  A CatanSettlement instance to place at the tile vertex
    """
    def setTileVertex(self, row, col, aSettlement):
        # validate inputs
        if (row < 0) or (row > 1) or (col < 0) or (col > 2):
            raise ValueError("Invalid index to row/col...")
        elif (type(aSettlement) != CatanSettlements):
            raise ValueError("Invalid input for catan settlement...")
        self.m_tileVertices[row][col] = aSettlement
    
    
    """
    getTileEdge(row, col)
    ----------------
    
    Inputs
    row  An integer for the row index for the tile grid of edges
    
    col  An integer for the col index for the tile grid of edges
    
    Returns
    self.m_tileEdges[row][col]  The object at that edge of the tile.
    """
    def getTileEdge(self, row, col):
        return self.m_tileEdges[row][col]
    
    
    """
    getTileEdge(row, col, aRoad)
    ----------------
    
    Inputs
    row  An integer for the row index for the tile grid of edges
    
    col  An integer for the col index for the tile grid of edges
    
    aRoad  A CatanRoad instance to place on the tile edge
    """
    def setTileEdge(self, row, col, aRoad):
        # validate inputs
        if (row < 0) or (row > 2) or (col < 0) or (col > 1):
            raise ValueError("Invalid index to row/col...")
        elif (type(aRoad) != CatanRoads):
            raise ValueError("Invalid input for catan road...")
        self.m_tileEdges[row][col] = aRoad
    
