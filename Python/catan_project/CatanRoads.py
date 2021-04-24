# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:25:39 2021

@author: Raymart Ballesteros
@date: 4/23/2021
@brief: This is a class to represent the road pieces on the Catan board.
"""

from CatanSettlements import Colors


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
    """
    def __init__(self, aColor=Colors.UNINITIALIZED):
        self.setColor(aColor)

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
            raise ValueError("Did not procide a valid input for road color...")
            
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
