# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:59:12 2021

@author: Raymart Ballesteros
@brief: Unittest for nim classes
"""

from nim import NimStack, NimPiles


def test_NimStack_ConstructorDefault():
    stack1 = NimStack()
    assert stack1.getNumRocks() == 0
    
def test_NimStack_Constructor():
    stack2 = NimStack(10)
    assert stack2.getNumRocks() == 10
    
def test_NimStack_CheckEmptyTrue():
    stack3 = NimStack()
    assert stack3.checkEmpty() == True
    
def test_NimStack_CheckEmptyFalse():
    stack4 = NimStack(10)
    assert stack4.checkEmpty() == False

def test_NimPiles_Constructor():
    game = NimPiles()
    for i in range(0, len(game.m_piles)):
        retVal = game.getPile(i)
        assert retVal == 0
        
def test_NimPiles_GetPile_InvalidIndex():
    game2 = NimPiles()
    retVal = game2.getPile(-1)
    assert retVal == -1
    
def test_NimPiles_GeneratePiles():
    game3 = NimPiles()
    game3.generatePiles()
    for i in range(0, len(game3.m_piles)):
        assert game3.getPile(i) != 0
    
def test_NimPiles_GameOverTrue():
    game4 = NimPiles()
    assert game4.gameOver() == True
    
def test_NimPiles_GameOverFalse():
    game5 = NimPiles()
    game5.generatePiles()
    assert game5.gameOver() == False
    
def test_NimPiles_CalculateNimSum():
    game6 = NimPiles()
    game6.m_piles[0].setNumRocks(11)
    game6.m_piles[1].setNumRocks(2)
    game6.m_piles[2].setNumRocks(8)
    retVal = game6.calcNimSum()
    assert retVal == 1
    
def test_NimPiles_UpdatePiles():
    game7 = NimPiles()
    game7.m_piles[0].setNumRocks(11)
    game7.m_piles[1].setNumRocks(2)
    game7.m_piles[2].setNumRocks(8)
    game7.updatePiles(0, 4)
    assert game7.getPile(0) == 7
