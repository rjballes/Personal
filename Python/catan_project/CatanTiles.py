# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:20:32 2021

@package: CatanTiles
@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This contains the class definitions related to the Catan tiles on the board.
"""

# imports
from CatanSettlements import CatanSettlements, Colors
from CatanRoads import CatanRoads
from PyQt5 import QtCore
import enum
import math



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
    aRow   An integer indicating what row the hexagon tile appears on the game board grid
    
    aCol   An integer indicating what column the hexagon appears on the game board grid
    
    aEdgeLength  An integer for the length of the edge of the hexagonal tile (assumes tiles are 
                 regular hexagons)
    
    aResourceType  An instance of the ResourceTypes enum to indicate the type 
                   of resource for the game tile
    
    aValue  An integer for the dice value with which players collect this resource
    
    aHasRobber  A boolean value indicating whether or not the robber is on the tile
    """
    def __init__(self, aRow, aCol, aEdgeLength, aResourceType=ResourceTypes.NONE, aValue=0, aHasRobber=False):
        self.m_row = aRow
        self.m_col = aCol
        self.m_edgeLength = aEdgeLength
        self.m_resourceType = aResourceType
        self.m_tileValue = aValue
        self.m_tileHasRobber = aHasRobber
        
        # initialize lists for the vertices and edges of tile
        self.m_tileVertices = []
        for x,y in self.genHexagonCoords():
            tmp = CatanSettlements(x, y)
            self.m_tileVertices.append(tmp)
        
        self.m_tileEdges = []
        for i in range(0, 6):
            if i != 5:
                p1, p2 = self.genEdgeCoords(self.getTileVertex(i).getCoords(), self.getTileVertex(i+1).getCoords())
            else:
                p1, p2 = self.genEdgeCoords(self.getTileVertex(i).getCoords(), self.getTileVertex(0).getCoords())
            tmp = CatanRoads(p1[0], p1[1], p2[0], p2[1])
            self.m_tileEdges.append(tmp)
                
                
    """
    getEdgeLength()
    ----------------
    
    Returns
    self.m_edgeLength  An enum for the resource types in the game
    """
    def getEdgeLength(self):
        return self.m_edgeLength
    
    
    """
    setEdgeLength()
    ----------------
    
    Inputs
    aEdgeLength  A float value to assign as the tile's length of its edges
    """
    def setEdgeLength(self, aEdgeLength):
        # valid that the input is a valid resource type
        if (aEdgeLength <= 0) or (type(aEdgeLength) != float):
            raise ValueError("Did not provide a valid float value for the tile's edge length...")

        self.m_edgeLength = aEdgeLength
    
    
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
        if (aValue < 0) or (aValue > 12) or (aValue == 1) or (type(aValue) != int):
            raise ValueError("Did not provide a valid input for the tile value...")

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
    getTileVertex(aIndex)
    ----------------
    
    Inputs
    aIndex  An integer for the index of the list of vertices/settlements
    
    Returns
    self.m_tileVertices[aIndex]  The object at that vertex/settlement of the tile.
    """
    def getTileVertex(self, aIndex):
        return self.m_tileVertices[aIndex]
    
    
    """
    setTileVertex(aIndex, aValue, aColor)
    ----------------
    
    Inputs
    aIndex  An integer for the index of the list of vertices/settlements
    
    aValue  An integer for the value of the settlement/city being placed/played
    
    aColor  An enum value for the color of the game piece (that is being played).
            Do not provide a color if only upgrading the settlement to a city.
            That is, the color stays the same.
    """
    def updateTileVertex(self, aIndex, aValue, aColor=Colors.UNINITIALIZED):
        # validate inputs
        if (aIndex < 0) or (aIndex > 5) or (type(aIndex) != int):
            raise ValueError("Invalid index to list of vertices/settlements...")

        self.m_tileVertices[aIndex].setValue(aValue)
        if aColor != Colors.UNINITIALIZED:
            self.m_tileVertices[aIndex].setColor(aColor)
    
    
    """
    getTileEdge(aIndex)
    ----------------
    
    Inputs
    aIndex  An integer for the index of the list of vertices/settlements
    
    Returns
    self.m_tileEdges[aIndex]  The object at that edge/road of the tile.
    """
    def getTileEdge(self, aIndex):
        return self.m_tileEdges[aIndex]
    
    
    """
    updateTileEdge(aIndex, aColor)
    ----------------
    
    Inputs
    aIndex  An integer for the index of the list of vertices/settlements
    
    aColor  An enum value for the color of the game piece (that is being played)
    """
    def updateTileEdge(self, aIndex, aColor):
        # validate inputs
        if (aIndex < 0) or (aIndex > 5) or (type(aIndex) != int):
            raise ValueError("Invalid index to list of edges/roads...")

        self.m_tileEdges[aIndex].setColor(aColor)
        
    
    """
    genHexagonCoords()
    ----------------
    
    Returns
    A generator object of (x,y) pairs/tuples for the coordinates of the vertices of the hexagon tile.
    Will need to save the returned generator within a list (or something else).
    """
    def genHexagonCoords(self):
        row_height = self.m_edgeLength * (3 / 2)
        col_width = math.sqrt(3) * self.m_edgeLength
        

        x = ( self.m_col - 0.5 * (self.m_row % 2) ) * col_width
        y = self.m_row * row_height
        
        for angle in range(0, 360, 60):
            x += math.sin(math.radians(angle + 240)) * self.m_edgeLength
            y += math.cos(math.radians(angle + 240)) * self.m_edgeLength
            yield x, y
            
            
    """
    genEdgeCoords(aPoint1, aPoint2)
    ----------------
    This method is used for the generation of the two points used to draw/represent
    the line for the road game piece.
    
    Inputs
    aPoint1   A QPointF object for the first point of the road/edge game piece
    
    aPoint2   A QPointF object for the second point of the road/edge game piece
    
    Returns
    roadPoint1, roadPoint2  Arrays holding x,y coordinate pairs 
                             used for representing the road/edge game pieces
    """
    def genEdgeCoords(self, aPoint1, aPoint2):
        newMagnitude = 14
        v1 = [(aPoint2.x()-aPoint1.x())/(self.m_edgeLength/newMagnitude), 
              (aPoint2.y()-aPoint1.y())/(self.m_edgeLength/newMagnitude)]
        v2 = [(aPoint1.x()-aPoint2.x())/(self.m_edgeLength/newMagnitude), 
              (aPoint1.y()-aPoint2.y())/(self.m_edgeLength/newMagnitude)]
        roadPoint1 = [aPoint1.x()+v1[0], aPoint1.y()+v1[1]]
        roadPoint2 = [aPoint2.x()+v2[0], aPoint2.y()+v2[1]]
        
        return roadPoint1, roadPoint2
    
    
    """
    findVertexIdFromPoint(aPoint)
    ----------------
    This method searches for the index of the vertex/settlement position that matches
    (or is closest) to the specified point.
    
    Inputs
    aPoint   A QPointF object for the first point of the road/edge game piece
    
    Returns
    savedId  Index to the tileVertices array that matches the specified point
    """
    def findVertexIdFromPoint(self, aPoint):
        if type(aPoint) != QtCore.QPointF:
            raise TypeError("Did not provide a valid input of type QPointF...")
        
        savedId = -1
        for i in range(6):
            if self.m_tileVertices[i].getCoords() == aPoint:
                savedId = i
                break
            
        return savedId
            
    
    
    """
    findEdgeIdFromPoints(aPoint1, aPoint2)
    ----------------
    This method searches for the index of the edge/road position that matches
    (or is closest) to the specified points. This assumes that the points in question
    are on the hexagonal tile.
    
    Inputs
    aPoint1   A QPointF object for the first point of a vertex on the hexagonal tile
    
    aPoint2   A QPointF object for the second point of a vertex on the hexagonal tile
    
    Returns
    savedId  Index to the tileEdges array that matches the specified points
    """
    def findEdgeIdFromPoints(self, aPoint1, aPoint2):
        if (type(aPoint1) != QtCore.QPointF) or (type(aPoint2) != QtCore.QPointF):
            raise TypeError("Did not provide input of type QPointF...")
        
        if (self.findVertexIdFromPoint(aPoint1) == -1) or (self.findVertexIdFromPoint(aPoint2) == -1):
            raise ValueError("Did not provide points/vertices on this particular tile...")
        
        savedId = -1
        minAverage = self.m_edgeLength
        for i in range(6):
            retPoint1, retPoint2 = self.m_tileEdges[i].getPoints()
            d1 = math.sqrt( (aPoint1.x() - retPoint1.x())**2 + (aPoint1.y() - retPoint1.y())**2 )
            d2 = math.sqrt( (aPoint2.x() - retPoint2.x())**2 + (aPoint2.y() - retPoint2.y())**2 )
            avg = (d1 + d2) / 2
            if ( avg <= minAverage ):
                savedId = i
                minAverage = avg
            
        return savedId
    
