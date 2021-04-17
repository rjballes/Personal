# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:46:27 2020

@author: Raymart Ballesteros
@brief This is a class of useful functions for playing Nim
"""


import random

class NimStack:
    def __init__(self, aNumRocks = 0):
        self.m_numRocks = aNumRocks
    
    def getNumRocks(self):
        return self.m_numRocks
    
    def setNumRocks(self, aNumRocks):
        self.m_numRocks = aNumRocks
    
    # returns True if the stack is empty; False otherwise
    def checkEmpty(self):
        return (self.m_numRocks == 0)
    
    # takes the number of rocks to take away from the stack and updates it by removing that amount
    def subtractRocks(self, numToSubtract):
        self.m_numRocks -= numToSubtract




class NimPiles:
    def __init__(self):
        self.m_piles = [NimStack(), NimStack(), NimStack()]
        
    def getNumPiles(self):
        return len(self.m_piles)
        
    def getPile(self, pileIndex):
        if (pileIndex < 0) or (pileIndex >= len(self.m_piles)):
            print("Invalid index\n")
            return -1
        
        return self.m_piles[pileIndex].getNumRocks()
        

    # This function checks to see if all the piles are empty; hence the game is over
    def gameOver(self):
        for i in range(0, len(self.m_piles)):
            if self.m_piles[i].checkEmpty() == False:
                return False
        return True
    
    # This function randomly assigns values to each pile
    def generatePiles(self):
        random.seed()
        for i in range(0, len(self.m_piles)):
            self.m_piles[i].setNumRocks(random.randint(0,30) + 1)
            
    def updatePiles(self, pileIndex, numRocksToRemove):
        self.m_piles[pileIndex].subtractRocks(numRocksToRemove)
        
    # This functions prints the number of rocks in each pile to the screen
    def printPiles(self):
        print("Current number of rocks in piles: %d  %d  %d" % 
              (self.m_piles[0].getNumRocks(), self.m_piles[1].getNumRocks(), self.m_piles[2].getNumRocks()))
        
    def calcNimSum(self):
        nimSum = self.m_piles[0].getNumRocks()
        for i in range(1, len(self.m_piles)):
            nimSum ^= self.m_piles[i].getNumRocks()
            
        return nimSum
        


class NimGame:
    def __init__(self):
        self.piles = NimPiles()
        
    # This function displays a welcome message explaining the game of Nim
    def welcome(self):
        print("---------------------")
        print("  N   N  I  M     M")
        print("  NN  N  I  MM   MM")
        print("  N N N  I  M M M M")
        print("  N  NN  I  M  M  M")
        print("---------------------")
        print("Nim is a mathematical game in which two players take turns \
              removing 'rocks' from ditinct piles.")
        print("On each turn, a player must remove at least one 'rock', \
              but can remove as many 'rocks' from only one pile.")
        print("The game is over when all of the 'rocks' have been removed\
              from each pile.")
        print("To win the game, you have to take the last 'rock.'\n\n")
    
    def print_game_over(self):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(" GGGG    A    M   M  EEEEE")
        print("G       AAA   MM MM  E    ")
        print("G GGG   A A   MM MM  EEEEE")
        print("G   G  AAAAA  M M M  E    ")
        print(" GGGG  A   A  M   M  EEEEE")
        print("----------------------------")
        print(" OOO   V   V  EEEEE  RRRR ")
        print("O   O  V   V  E      R   R")
        print("O   O  V   V  EEEEE  RRRR ")
        print("O   O   V V   E      R  R ")
        print(" OOO     V    EEEEE  R   R")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        
    def cp_moves(self):
        # Find all piles that a 1 place that matches with far left
        # nonzero digit of the nim sum (binary form)
        # Then randomly choose on of those piles to make a move
        print("Now it's the cpu's turn to make a move...")
        print()
        
        b_piles = ["%08d" % int(bin(self.piles.getPile(0))[2:]),
                   "%08d" % int(bin(self.piles.getPile(1))[2:]),
                   "%08d" % int(bin(self.piles.getPile(2))[2:])]
        nimSum = self.piles.calcNimSum()
        b_nimSum = "%08d" % int(bin(nimSum)[2:])
        idx = b_nimSum.find('1')
        choices = [i for i in range(3) if b_piles[i][idx]=='1']
        
        random.seed()
        if nimSum != 0:
            ix = random.randint(0,10) % len(choices)
            ix = choices[ix]
            # Now we add the binary forms of the number in pile ix
            # and the nim sum to determine the number of rocks to leave in that pile
            newNumRocks = self.piles.getPile(ix) ^ nimSum    
            self.piles.updatePiles(ix, newNumRocks)
        else:
            choices = [i for i in range(3) if self.piles.getPile(i) != 0]
            ix = random.randint(0,13) % len(choices)
            ix = choices[ix]
            if self.piles.getPile(ix) == 1:
                val = 1
            else:
                val = (random.randint(0,30) % self.piles.getPile(ix)) + 1
            self.piles.updatePiles(ix, val)
            
    def ask_user_pile(self):
        # This functions asks the user for their choice of pile to remove from
        print("Now it's your turn to make a move...")
        print("Which pile would you like to remove 'rocks' from: ")
        print("1) Pile 1")
        print("2) Pile 2")
        print("3) Pile 3")
        pile = int(input())
        if pile not in range(1, 4):
            print("Invalid input, Try again")
            pile = self.ask_user_pile()
        elif self.piles.getPile(pile-1) == 0:
            print("That pile is empty, Choose another pile")
            pile = self.ask_user_pile()
            
        return pile-1
    
    def ask_user_rocks(self, pile_ix):
        # This function asks the user for number of rocks to remove
        print("How many 'rocks' do you want to remove from Pile %d" % (pile_ix+1))
        numToRemove = int(input())
        if (numToRemove <= 0) or (numToRemove > self.piles.getPile(pile_ix)):
            print("Not a valid move, Try again")
            numToRemove = self.ask_user_rocks(pile_ix)
            
        return int(numToRemove)
    
    def user_moves(self, pileId=None, numToRemove=None):
        if (pileId == None) or (numToRemove == None):
            pileId = self.ask_user_pile()
            numToRemove = self.ask_user_rocks(pileId)
        print()
        self.piles.updatePiles(pileId, numToRemove)
            
    