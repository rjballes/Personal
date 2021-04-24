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
            self.m_tileVertices.append([])
            for j in range(2):
                tmp = CatanRoads()
                self.m_tileVertices[i].append(tmp)
                
                
    """
    getResourceType()
    ----------------
    
    Returns
    self.m_resourceType  An enum for the resource types in the game
    """
    def getResourceType(self):
        return self.m_resourceType
    
    
    """
    getTileValue()
    ---------------
    
    Returns
    self.m_tileValue  An integer of the dice value for the tile
    """
    def getTileValue(self):
        return self.m_tileValue
    
    
    """
    checkTileHasRobber()
    ----------------
    
    Returns
    self.m_tileHasRobber  A boolean value indicating if the robber is on the tile
    """
    def checkTileHasRobber(self):
        return self.m_tileHasRobber
    
    
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
    
