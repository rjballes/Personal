# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:15:20 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is a class to represent the settlement and city pieces on the 
Catan board.
"""


# imports
import enum


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
    """
    def __init__(self, aValue=0, aColor=Colors.UNINITIALIZED):
        self.setValue(aValue)
        self.setColor(aColor)


    """
    setValue()
    -------------
    This method takes an integer input and assigns it to the m_value attribute 
    of the object.
    
    Parameters
    aValue  Either 0, 1, or 2 to represent the value of the piece. A 0 means that 
            no player has built a settlement/city yet. 
    """
    def setValue(self, aValue):
        # check valid value for settlement
        if aValue < 0 or aValue > 2:
            raise ValueError("Did not provide a valid value for settlement/city...")
            self.m_value = 0
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
    setColor()
    -------------
    This method takes an enum of type Colors and assigns it to the color attribute.
    
    Parameters
    aColor  Will either be UNINITIALIZED(-1), BLUE(0), ORANGE(1), RED(2), WHITE(3) 
    """
    def setColor(self, aColor):
        # check valid input for color; value is within Colors array
        if (aColor.value < Colors.LOWER.value) or (aColor.value > Colors.UPPER.value):
            raise ValueError("Did not procide a valid input for settlement/city color...")
            self.m_color = Colors.UNINITIALIZED
            
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
        