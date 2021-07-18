# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:51:16 2021

@package: CatanBoard
@author: Raymart Ballesteros
@date: 6/3/2021
@brief: This contains the classes to represent the Catan board
"""

# imports
from CatanSettlements import CatanSettlements, Colors
from CatanRoads import CatanRoads
from CatanTiles import CatanTiles, ResourceTypes
from configparser import ConfigParser
from PyQt5 import QtCore
import math
import random


class CatanBoard:
    """
    Constructor
    
    """
    def __init__(self, aEdgeLength):
        self.m_allTiles = []
        for i in range(5):
            #self.m_allTiles.append([])
            for j in range(5):
                if (i == 0 or i == 4) and (j == 0 or j == 4):
                    #self.m_allTiles[i].append(None)
                    continue
                elif (i == 1 or i == 3) and (j == 0):
                    #self.m_allTiles[i].append(None)
                    continue
                else:
                    tmp = CatanTiles(i, j, aEdgeLength)
                    self.m_allTiles.append(tmp)

        self.m_allVertices = []
        self.m_allEdges = []
        for tile in self.m_allTiles:
            for i in range(6):
                tmp = tile.getTileVertex(i).getCoords()
                self.m_allVertices.append(tmp)
                
                tmp, tmp2 = tile.getTileEdge(i).getPoints()
                self.m_allEdges.append([tmp, tmp2])
                
        self.generateUniqueVertices()
        
        self.generateUniqueEdges()
        
        self.listOfResources = [ResourceTypes.OAR, ResourceTypes.WOOL, ResourceTypes.LUMBER, ResourceTypes.GRAIN,
              ResourceTypes.BRICK, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.LUMBER,
              ResourceTypes.NONE, ResourceTypes.LUMBER, ResourceTypes.OAR, ResourceTypes.LUMBER, ResourceTypes.OAR,
              ResourceTypes.GRAIN, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.WOOL]
        
        self.listOfNumbers = [10, 2, 9, 11,
              6, 4, 10, 9, 11,
              0, 3, 8, 8, 3,
              4, 5, 5, 6, 12]
    
    
    """
    findAllMatchingVertices(aPoint)
    --------------------
    Searches through the list of vertices for the specified point and saves the
    indices of all matching elements.
    
    Inputs
    aPoint  A QPointF object. Used to search for matching points.
    
    Returns
    allIds  An array of the indices of the matching elements in list of all vertices.
    """
    def findAllMatchingVertices(self, aPoint):
        if type(aPoint) != QtCore.QPointF:
            raise TypeError("Did not provide input of type QPointF...")
        
        allIds = []
        for i in range(len(self.m_allVertices)):
            if self.m_allVertices[i] == aPoint:
                allIds.append(i)
        
        return allIds
    
    
    """
    generateUniqueVertices()
    -----------------
    Creates a list of all unique vertices. Points that are essentially the same get averaged
    to get a single point for that vertex.
    
    Returns
    newVerticesList   A list of only the 'unique' vertices on the game board. Updates m_allVertices
                      with this new list of unique points.
    """
    def generateUniqueVertices(self):
        #TODO: consider creating a dict that saves the tile indices with matching point
        newVerticesList = []
        usedIds = []
        for m in range(len(self.m_allVertices)-1):
            if m in usedIds:
                continue
            listMatchingVertexIds = self.findAllMatchingVertices(self.m_allVertices[m])
            sumPoints = QtCore.QPointF(0,0)
            for id in listMatchingVertexIds:
                sumPoints = sumPoints + self.m_allVertices[id]
            newVerticesList.append(sumPoints / len(listMatchingVertexIds))
            usedIds += listMatchingVertexIds
        
        if len(self.m_allVertices)-1 not in usedIds:
            newVerticesList.append(self.m_allVertices[len(self.m_allVertices)-1])
            
        self.m_allVertices = newVerticesList
                
    
    """
    findAllMatchingEdges(aPoint1, aPoint2)
    --------------------
    Searches through the list of edges for the specified pair of points and saves the
    indices of all matching elements.
    
    Inputs
    aPoint1, aPoint2  A QPointF object used to find the matching endpoints of the edge/road.
    
    Returns
    allIds  An array of the indices of the matching elements in list of all edges.
    """
    def findAllMatchingEdges(self, aPoint1, aPoint2):
        if (type(aPoint1) != QtCore.QPointF) or (type(aPoint2) != QtCore.QPointF):
            raise TypeError("Did not provide inputs of type QPointF...")
        
        allIds = []
        for i in range(len(self.m_allEdges)):
            if (self.m_allEdges[i][0] == aPoint1) and (self.m_allEdges[i][1] == aPoint2):
                allIds.append(i)
            elif (self.m_allEdges[i][0] == aPoint2) and (self.m_allEdges[i][1] == aPoint1):
                allIds.append(i)
        
        return allIds
    
    
    """
    generateUniqueEdges()
    -----------------
    Creates a list of all unique edges/roads. Edges that are essentially the same get averaged
    to get a single set of endpoints.
    
    Returns
    newEdgesList   A list of only the 'unique' edges on the game board. Updates m_allEdges
                      with this new list of unique edges.
    """
    def generateUniqueEdges(self):
        #TODO: consider creating a dict that saves the tile indices with matching point
        newEdgesList = []
        usedIds = []
        for m in range(len(self.m_allEdges)-1):
            if m in usedIds:
                continue
            listMatchingEdgeIds = self.findAllMatchingEdges(self.m_allEdges[m][0], self.m_allEdges[m][1])
            if len(listMatchingEdgeIds) == 1:
                newEdgesList.append(self.m_allEdges[listMatchingEdgeIds[0]])
            elif len(listMatchingEdgeIds) == 0:
                raise ValueError("Should not get here...")
            else:
                sumEdges = [QtCore.QPointF(0,0), QtCore.QPointF(0,0)]
                for id in listMatchingEdgeIds:
                    if self.m_allEdges[id][0] == self.m_allEdges[m][0]:
                        sumEdges = [sumEdges[0] + self.m_allEdges[id][0], sumEdges[1] + self.m_allEdges[id][1]]
                    else:
                        sumEdges = [sumEdges[0] + self.m_allEdges[id][1], sumEdges[1] + self.m_allEdges[id][0]]
                pairPoints = [sumEdges[0] / len(listMatchingEdgeIds), sumEdges[1] / len(listMatchingEdgeIds)]
                newEdgesList.append(pairPoints)
            usedIds += listMatchingEdgeIds
        
        if len(self.m_allEdges)-1 not in usedIds:
            newEdgesList.append(self.m_allEdges[len(self.m_allEdges)-1])
            
        self.m_allEdges = newEdgesList
    
    
    """
    getATile(aIndex)
    -------------------
    
    Inputs
    aIndex  An integer for the index in the tiles array
    
    Returns
    self.m_allTiles[aIndex]  Returns the tile object at the specified index
    """
    def getATile(self, aIndex):
        # validate inputs
        if type(aIndex) != int:
            raise TypeError("Did not provide an integer value for the index...")
        elif (aIndex < 0) or (aIndex > len(self.m_allTiles)-1):
            raise IndexError("Did not provide a valid index to the tiles array (out of range)...")
        
        return self.m_allTiles[aIndex]
    
    
    """
    setTileResourceType(aIndex, aResourceEnumType)
    -------------------
    Assigns the specified resource type to the specified game tile.
    
    Inputs
    aIndex  An index to the list of tiles; specifies the tile that will be modified
    aResourceEnumType  An enum value of the ResourceTypes; specifies which resource to assign to
                       the desired tile
    """
    def setTileResourceType(self, aIndex, aResourceEnumType):
        # verify valid input arguments
        if type(aIndex) != int:
            raise TypeError("Did not provide an integer as the index...")
        elif (aIndex < 0) or (aIndex > len(self.m_allTiles)):
            raise IndexError("The provided index is out of range...")
        
        self.m_allTiles[aIndex].setResourceType(aResourceEnumType)
    
    
    """
    setTileValue(aIndex, aTileValue)
    -------------------
    Assigns the specified value (dice roll value) to the specified game tile.
    
    Inputs
    aIndex  An index to the list of tiles; specifies the tile that will be modified
    aTileValue  An integer value between two and twelve (not including seven) representing
                       a possible roll with two dice
    """
    def setTileValue(self, aIndex, aTileValue):
        # verify valid input arguments
        if type(aIndex) != int:
            raise TypeError("Did not provide an integer as the index...")
        elif (aIndex < 0) or (aIndex > len(self.m_allTiles)):
            raise IndexError("The provided index is out of range...")
        
        self.m_allTiles[aIndex].setTileValue(aTileValue)
    
    
    """
    checkValidSettlement(aVertexPoint)
    -------------------
    Takes a QPointF objects and verifies that whether or not it's a valid location
    for a player to place a setttlment. That is, checks whether it already has a settlement/city
    or if there is enough distance from a nearby city.
    
    Inputs
    aVertexPoint  A QPointF object of the coordinates of the point to place the settlement
    
    Returns
    Returns a 0 if the location is not valid; and returns a 1 if the location is good
    """
    def checkValidSettlement(self, aVertexPoint):
        
        if type(aVertexPoint) != QtCore.QPointF:
            raise TypeError("The provided argument is not of type QtCore.QPointF...")
        
        for aTile in self.m_allTiles:
            for k in range(6):
                tVertex = aTile.getTileVertex(k)
                if (tVertex.getValue() != 0):
                    tmpPoint = tVertex.getCoords()
                    if (tmpPoint == aVertexPoint):
                        print("A player already has a piece in this location...")
                        return 0
                    elif math.sqrt( (tmpPoint.x() - aVertexPoint.x())**2 + (tmpPoint.y() - aVertexPoint.y())**2 ) <= aTile.getEdgeLength():
                        print("There is a settlement too close to the specified location...")
                        return 0
                
        # This location/point is valid
        return 1
                
    
    
    """
    placeASettlement(aVertexPoint, aColor)
    -------------------
    This function takes a vertex point to place a settlement of a certain color if the
    location is valid (i.e., does not already have a settlement/city nearby). Will check
    if the location is valid and updates the tile/vertex object(s) appropriately.
    
    Inputs
    aVertexPoint  A QPointF object of the location that the player wants to place a settlement
    
    aColor  The color enum value  the player's game pieces
    
    Returns
    Returns a value of -1 if the location is not valid; and returns a 0 if the location
    was valid and the game board was updated appropriately updating the tiles with
    that matching vertex point/position.
    """
    def placeASettlement(self, aVertexPoint, aColor):
        if self.checkValidSettlement(aVertexPoint) == 0:
            print("The specified location is not valid for placing your settlement...")
            print("Please choose another location.")
            return -1
        
        #TODO: consider a new implementation using saved indices for tiles with matching point
        for p in range(len(self.m_allTiles)):
            for q in range(6):
                if aVertexPoint == self.m_allTiles[p].getTileVertex(q).getCoords():
                    self.m_allTiles[p].updateTileVertex(q, 1, aColor)
        
        return 0
        
    
    
    """
    upgradeToCity(aVertexPoint)
    -------------------
    We search for matching tile vertices as the provided QPointF position and update
    the value from a 1 to a 2 (i.e., settlement to a city) if a settlement already
    was placed in that location.
    
    Inputs
    aVertexPoint  A QPointF object representing a location/tile vertex on the game board
    
    aColor  A Colors enum value representing the color of the player's game pieces
    
    Returns
    Returns a -1 if there is not a settlement already in that position or the player's
    color and the settlement on the board do not matchl; otherwise, returns a 0 if
    the settlements were appropriately udpated.
    """
    def upgradeToCity(self, aVertexPoint, aColor):
        # check if a settlement is at this point
        for p in range(len(self.m_allTiles)):
            for q in range(6):
                if self.m_allTiles[p].getTileVertex(q).getCoords() == aVertexPoint:
                    if (self.m_allTiles[p].getTileVertex(q).getValue() == 1) and \
                       (self.m_allTiles[p].getTileVertex(q).getColor() == aColor):
                        self.m_allTiles[p].updateTileVertex(q, 2)
                    elif self.m_allTiles[p].getTileVertex(q).getValue() < 1:
                        print("There is no settlement in this position to upgrade...")
                        return -1
                    elif self.m_allTiles[p].getTileVertex(q).getColor != aColor:
                        print("The color of the current game piece does not match your color...")
                        return -1
        
        return 0
    
    
    """
    placeARoad(aPoint1, aPoint2, aColor)
    -------------------
    
    """
    def placeARoad(self, aPoint1, aPoint2, aColor):
        # check if a road is alread at this location
        pass
    
    
    """
    placeTheRobber(aTileIndex)
    -------------------
    
    """
    def placeTheRobber(self):
        pass
    
    
    """
    randomizeListOfResources()
    -------------------
    
    """
    def randomizeListOfResources(self):
        # self.m_listOfResources = [ResourceTypes.OAR, ResourceTypes.WOOL, ResourceTypes.LUMBER, ResourceTypes.GRAIN,
        #      ResourceTypes.BRICK, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.LUMBER,
        #      ResourceTypes.NONE, ResourceTypes.LUMBER, ResourceTypes.OAR, ResourceTypes.LUMBER, ResourceTypes.OAR,
        #      ResourceTypes.GRAIN, ResourceTypes.WOOL, ResourceTypes.BRICK, ResourceTypes.GRAIN, ResourceTypes.WOOL]
        
        random.shuffle(self.listOfResources)
    
    
    """
    randomizeListOfNumbers()
    ------------------
    
    """
    def randomizeListOfNumbers(self):
        # self.m_listOfNumbers = [10, 2, 9, 11,
        #      6, 4, 10, 9, 11,
        #      0, 3, 8, 8, 3,
        #      4, 5, 5, 6, 12]
        
        random.shuffle(self.listOfNumbers)
    
    
    """
    generateGameBoard()
    -----------------
    
    """
    def generateGameBoard(self, randomizeFlag=False):        
        if randomizeFlag == True:
            self.randomizeListOfResources()
            self.randomizeListOfNumbers()
        
        for k in range(len(self.m_allTiles)):
            if self.listOfResources[k] == ResourceTypes.NONE:
                self.m_allTiles[k].setTileHasRobber(True)
            self.m_allTiles[k].setResourceType(self.listOfResources[k])
            self.m_allTiles[k].setTileValue(self.listOfNumbers[k])
    
    
    """
    getAVertex(aIndex)
    -------------------
    
    Inputs
    aIndex  An integer for the index of an element in the vertices array
    
    Returns
    self.m_allVertices[aIndex]  Returns a QPointF object storing the position of the settlement/vertex
    """
    # def getAVertex(self, aIndex):
    #     # validate inputs
    #     if type(aIndex) != int:
    #         raise TypeError("Did not provide an integer value for the index...")
    #     elif (aIndex < 0) or (aIndex > len(self.m_allVertices)-1):
    #         raise ValueError("Did not provide a valid index to the vertices array (out of range)...")
        
    #     return self.m_allVertices[aIndex]
    
    
    """
    setAVertex(row, col, aSettlement)
    ------------------
    
    Inputs
    row  An int for the row number for the desired vertex
    col  An into for the column number for the desired vertex
    aSettlement  An instance of CatanSettlements
    """
    # def setAVertex(self, row, col, aSettlement):
    #     pass
    
    
    """
    getAnEdge(aIndex)
    -------------------
    
    Inputs
    aIndex  An integer for the index of an element in the edges array
    
    Returns
    self.m_allEdges[aIndex]  Returns an array of two QPointF objects storing the points
                             for the edge/road.
    """
    # def getAnEdge(self, aIndex):
    #     # validate inputs
    #     if type(aIndex) != int:
    #         raise TypeError("Did not provide a valid input of type integer for the index...")
    #     elif (aIndex < 0) or (aIndex > len(self.m_allEdges)-1):
    #         raise ValueError("Did not provide a valid index to the edges array (out of range)...")
        
    #     return self.m_allEdges[aIndex]
    
    
    """
    setAnEdge(row, col, aRoad)
    ------------------
    
    Inputs
    row  An int for the row number for the desired edge/road
    col  An into for the column number for the desired edge/road
    aSettlement  An instance of CatanRoads
    """
    # def setAnEdge(self, row, col, aSettlement):
    #     pass
    
    
    """
    parseConfigParams(fileName)
    ------------------
    
    Inputs
    fileName  Full path and name of the config file (.ini) containing the necessary parameters
              to setup the game board. Such as resources, tile numbers, and tile image names (etc.).
    
    Returns
    paramsDict  A dictionary with all the parameters; the section option names are the keys
                and the option values are the values in the dictionary.
    """
    def parseConfigParams(self, fileName):
        #@TODO Complete implementation and write tests
        parser = ConfigParser()
        if parser.read(fileName) == []:
            raise IOError(f"Was not able to read the config file: {fileName}")
        
        paramsDict = {}
        # Retrieve a list of the resources to be assigned to the tiles objects
        paramsDict['Types'] = [ResourceTypes(item) for item in parser.get('Resources', 'Types').split('\n')]
        # Retrieve the parameters for the file names of the images for the tiles
        paramsDict['BRICK'] = parser.get('Resources', 'BRICK')
        paramsDict['GRAIN'] = parser.get('Resources', 'GRAIN')
        paramsDict['LUMBER'] = parser.get('Resources', 'LUMBER')
        paramsDict['OAR'] = parser.get('Resources', 'OAR')
        paramsDict['WOOL'] = parser.get('Resources', 'WOOL')
        paramsDict['NONE'] = parser.get('Resources', 'NONE')
        # Retrieve the list of numbers to be assigned to the tiles objects
        paramsDict['Numbers'] = [int(x) for x in parser.get('Numbers', 'Values').split('\n')]
        
        return paramsDict
