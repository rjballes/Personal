# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:15:20 2021

@author: Raymart Ballesteros
@date: 6/1/2021
@brief: This is a class to represent the settlement and city pieces on the 
Catan board.
"""


# imports
import enum
from PyQt5 import QtCore


"""
@class: Colors
@brief: This is a enum class representing the possible colors a player's pieces 
can be. 
"""
class Colors(enum.Enum):
    UNINITIALIZED = -1
    BLUE = 0
    ORANGE = 1
    RED = 2
    WHITE = 3
    NUM_COLORS = 4
    LOWER = UNINITIALIZED
    UPPER = WHITE
    
    

"""
@class: CatanSettlement
"""
class CatanSettlements:
    """
    Constructor
    --------------
    
    Parameters
    aValue  Either 0, 1, or 2 to represent the value of the piece. A 0 means that 
            no player has built a settlement/city yet. Default is 0.
            
    aColor  Can take on a value from the enum class Colors. Holds the color of
            the player that owns the settlement/city.
            
    aXCoord  Represents the x-component of the position of the settlement (float).
    
    aYCoord  Represents the y-component of the position of the settlement (float).
    """
    def __init__(self, aXCoord, aYCoord, aValue=0, aColor=Colors.UNINITIALIZED):
        self.m_position = QtCore.QPointF(aXCoord, aYCoord)
        self.m_value = aValue
        self.m_color = aColor


    """
    setValue(aValue)
    -------------
    This method takes an integer input and assigns it to the m_value attribute 
    of the object.
    
    Parameters
    aValue  Either 0, 1, or 2 to represent the value of the piece. A 0 means that 
            no player has built a settlement/city yet. 
    """
    def setValue(self, aValue):
        # check valid value for settlement
        if (aValue < 0 or aValue > 2) or (type(aValue) != int):
            raise ValueError("Did not provide a valid value for settlement/city...")

        self.m_value = aValue


    """
    getValue()
    -------------
    This method returns the settlement/city value.
    
    Returns
    self.m_value  Either 0, 1, or 2 to represent the value of the piece. A 0 means that 
                  no player has built a settlement/city yet. 
    """
    def getValue(self):
        return self.m_value


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
            raise ValueError("Did not provide a valid input for settlement/city color...")
            
        self.m_color = aColor


    """
    getColor()
    -------------
    This method returns the color of the player's settlement/city.
    
    Returns
    self.m_color  Will either be UNINITIALIZED(-1), BLUE(0), ORANGE(1), RED(2), WHITE(3)
    """
    def getColor(self):
        return self.m_color
    
    
    """
    setCoords(xc, yc)
    -------------
    This method takes x and y coordinates (floats) and assigns them for the position
    of the settlement on the bame board.
    
    Parameters
    xc  float
    yc  float
    """
    def setCoords(self, xc, yc):
        if (type(xc) != float) or (type(yc) != float):
            raise ValueError("Did not provide float values for the coordinates...")
                    
        self.m_position = QtCore.QPointF(xc,yc)


    """
    getCoords()
    -------------
    This method returns the x and y coordinates of the game piece on the board.
    
    Returns
    [self.m_x, self.m_y]  Returns a list of size two with the coordinates of 
                          the game piece on the game board (gui)
    """
    def getCoords(self):
        return self.m_position
        