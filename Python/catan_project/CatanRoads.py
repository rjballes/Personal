# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:25:39 2021

@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This is a class to represent the road pieces on the Catan board.
"""

from CatanSettlements import Colors
from PyQt5 import QtCore


"""
@class: CatanRoads
"""
class CatanRoads:
    """
    Constructor
    --------------
    
    Parameters   
    aColor  Can take on a value from the enum class Colors. Holds the color of
            the player that owns the road.
    
    aP1_x  The x-component of the first point used for the location of a road (float).
    
    aP1_y  The y-component of the first point used for the location of a road (float).
    
    aP2_x  The x-component of the second point used for the location of a road (float).
    
    aP2_y  The y-component of the second point used for the location of a road (float).
    """
    def __init__(self, aP1_x, aP1_y, aP2_x, aP2_y, aColor=Colors.UNINITIALIZED):
        self.m_point1 = QtCore.QPointF(aP1_x, aP1_y)
        self.m_point2 = QtCore.QPointF(aP2_x, aP2_y)        
        self.m_color = aColor


    """
    setColor(aColor)
    -------------
    This method takes an enum of type Colors and assigns it to the color attribute.
    
    Parameters
    aColor  Will either be UNINITIALIZED(-1), BLUE(0), ORANGE(1), RED(2), WHITE(3)  
    """
    def setColor(self, aColor):
        # check valid input for color; value is within Colors array
        if (type(aColor) != Colors):
            raise TypeError("Did not provide an enum value of type Colors...")
        elif (aColor.value < Colors.LOWER.value) or (aColor.value > Colors.UPPER.value):
            raise ValueError("Did not provide a valid input for road color...")
            
        self.m_color = aColor


    """
    getColor()
    -------------
    This method returns the color of the player's road.
    
    Returns
    self.m_color  Will either be UNINITIALIZED(-1), BLUE(0), ORANGE(1), RED(2), WHITE(3)
    """
    def getColor(self):
        return self.m_color
    
    
    """
    setPoints(aP1_x, aP1_y, aP2_x, aP2_y)
    -------------
    This method assigns the points used for the position of the road game piece.
    
    Parameters
    aP1_x  The x-component of the first point used for the location of a road (float).
    
    aP1_y  The y-component of the first point used for the location of a road (float).
    
    aP2_x  The x-component of the second point used for the location of a road (float).
    
    aP2_y  The y-component of the second point used for the location of a road (float).  
    """
    def setPoints(self, aP1_x, aP1_y, aP2_x, aP2_y):
        if (type(aP1_x) != float) or (type(aP1_y) != float) or (type(aP2_x) != float) or \
            (type(aP2_y) != float):
            raise ValueError("Did not provide a float value for the coordinates...")
        self.m_point1 = QtCore.QPointF(aP1_x, aP1_y)
        self.m_point2 = QtCore.QPointF(aP2_x, aP2_y)


    """
    getPoints()
    -------------
    This method returns the color of the player's road.
    
    Returns
    self.m_point1  The coordinates for the first point of the position of the road piece.
    
    self.m_point2  The coordinates for the second point of the position of the road piece.
    """
    def getPoints(self):
        return self.m_point1, self.m_point2
