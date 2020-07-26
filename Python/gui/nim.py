# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:46:27 2020

@author: Raymart Ballesteros
@brief This is a class of useful functions for playing Nim
"""


import random

class Nim:
    def __init__(self):
        self.piles = [0, 0, 0]
        
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

    # This function checks to see if all the piles are empty; hence the game is over
    def game_over(self):
        for i in range(0, len(self.piles)):
            if self.piles[i] != 0:
                return False
        return True
    
    # This function randomly assigns values to each pile
    def generate_piles(self):
        random.seed()
        self.piles[0] = random.randint(0,30)+1
        self.piles[1] = random.randint(0,30)+1
        self.piles[2] = random.randint(0,30)+1
        
    # This functions prints the number of rocks in each pile to the screen
    def print_piles(self):
        print("Current number of rocks in piles: %d  %d  %d" % (self.piles[0], self.piles[1], self.piles[2]))
        
    def nim_sum(self):
        b1 = "%08d" % int(bin(self.piles[0])[2:])
        b2 = "%08d" % int(bin(self.piles[1])[2:])
        b3 = "%08d" % int(bin(self.piles[2])[2:])
        
        # iterate through strings and perform sum of digits mod 2
        nimSum = "0b"
        for i in range(len(b1)):
            temp = (int(b1[i]) + int(b2[i]) + int(b3[i])) % 2
            nimSum += str(temp)
            
        return int(nimSum, 2)
    
    def cp_moves(self):
        # Find all piles that a 1 place that matches with far left
        # nonzero digit of the nim sum (binary form)
        # Then randomly choose on of those piles to make a move
        print("Now it's the cpu's turn to make a move...")
        print()
        
        b_piles = ["%08d" % int(bin(self.piles[0])[2:]),
                   "%08d" % int(bin(self.piles[1])[2:]),
                   "%08d" % int(bin(self.piles[2])[2:])]
        nimSum = self.nim_sum()
        b_nimSum = "%08d" % int(bin(nimSum)[2:])
        idx = b_nimSum.find('1')
        choices = [i for i in range(3) if b_piles[i][idx]=='1']
        
        random.seed()
        if nimSum != 0:
            ix = random.randint(0,10) % len(choices)
            ix = choices[ix]
            # Now we add the binary forms of the number in piles ix
            # and the nim sum to determine the number of rocks to leave in that pile
            result = "0b"
            t1 = "%08d" % int(bin(self.piles[ix])[2:])
            t2 = "%08d" % int(bin(nimSum)[2:])
            for j in range(0,len(t1)):
                result += str((int(t1[j]) + int(t2[j])) % 2)
                
            self.piles[ix] = int(result,2)
        else:
            choices = [i for i in range(3) if self.piles[i] != 0]
            ix = random.randint(0,13) % len(choices)
            ix = choices[ix]
            if self.piles[ix] == 1:
                val = 1
            else:
                val = (random.randint(0,30) % self.piles[ix]) + 1
            self.piles[ix] -=  val
            
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
        elif self.piles[pile-1] == 0:
            print("That pile is empty, Choose another pile")
            pile = self.ask_user_pile()
            
        return pile-1
    
    def ask_user_rocks(self, pile_ix):
        # This function asks the user for number of rocks to remove
        print("How many 'rocks' do you want to remove from Pile %d" % (pile_ix+1))
        rem = int(input())
        if (rem <= 0) or (rem > self.piles[pile_ix]):
            print("Not a valid move, Try again")
            rem = self.ask_user_rocks(pile_ix)
            
        return int(rem)
    
    def user_moves(self, pile=None, n_rem=None):
        if (pile == None) or (n_rem == None):
            pile = self.ask_user_pile()
            n_rem = self.ask_user_rocks(pile)
        print()
        self.piles[pile] -= n_rem
        
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
