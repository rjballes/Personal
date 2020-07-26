# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:27:02 2020

@author: Raymart Ballesteros
@brief support functions for main gui window
@details This contains any supporting functions for the nimGameGUI window to
play the game of Nim.
"""

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import sys
import time

from nim import Nim


class PlayGameThread(QThread):
    def __init__(self, guiWindowClass):
        QThread.__init__(self, None)
        self.guiWindowClass = guiWindowClass
        
    def run(self):
        self.guiWindowClass.playGame()
        self.quit()
        

class GUIWindow(QtWidgets.QMainWindow):
    ## constructor
    def __init__(self, inputUI, parent=None):
        super(GUIWindow, self).__init__(parent)
        self.m_ui = inputUI
        self.m_ui.setupUi(self)
        self.m_Nim = Nim()
        
        ## Actions to functions linkage
        self.m_ui.playButton.clicked.connect(self.startGame)
        self.m_ui.resetButton.clicked.connect(self.resetGame)
        
    
    ## Helper functions
    
    # @brief starts the game
    # @details Randomly generates three piles and asks the user if they want to go 
    # first or to let the computer go first.
    def startGame(self):
        if self.m_ui.playButton.text() == 'PLAY':
            self.m_Nim.generate_piles()
            self.m_ui.leftStack.setText(str(self.m_Nim.piles[0]))
            self.m_ui.middleStack.setText(str(self.m_Nim.piles[1]))
            self.m_ui.rightStack.setText(str(self.m_Nim.piles[2]))
            
            # asks user if they want to go first
            self.getFirstPlayer()
            
            # disable play button and enable reset button
            #self.m_ui.playButton.setEnabled(False)
            self.m_ui.playButton.setText("Enter")
            self.m_ui.resetButton.setEnabled(True)
            # disconnect startGame function to playButton
            self.m_ui.playButton.disconnect()
            # connect updatePiles function to playButton
            self.m_ui.playButton.clicked.connect(self.updatePiles)
            
            # start thread to play game
            #gameWorker = PlayGameThread(self)
            #gameWorker.start()
        
    # @brief asks user if they want to make the first move
    # @details Opens a message window and asks the user if they want to make the
    # first move.
    def getFirstPlayer(self):
        # create a message window asking if user wants to make the first move
        firstMsgBox = QMessageBox(QMessageBox.Question, "First Player", "Would you like to go first?")
        firstMsgBox.addButton(QMessageBox.Yes)
        firstMsgBox.addButton(QMessageBox.No)
        firstMsgBox.setDefaultButton(QMessageBox.No)
        
        # save the user's reply to message box
        reply = firstMsgBox.exec()
        if reply == QMessageBox.Yes:
            print('You are making the first move...')
            self.NextPlayer = 0  # user
        elif reply == QMessageBox.No:
            print('The computer is making the first move...')
            self.NextPlayer = 1  # computer
            time.sleep(1)
        else:
            print('Invalid selection')
            sys.exit()
            
    
    # @brief updates the piles and displays with players' moves
    # @details The next player's move updates the piles and the stack displays 
    # are updated accordingly.
    def updatePiles(self):
        # check that button says 'Enter'
        if self.m_ui.playButton.text() == 'Enter':
            # check which player is next and apply their move
            #if self.NextPlayer == 0:
            # Get the user's move
            pile, n_rem = self.checkUserInput()
            # check that the user has given a valid move
            if (pile != None) and (n_rem != None):
                self.m_Nim.user_moves(pile, n_rem)
                self.NextPlayer = 1
                #time.sleep(1)
            
            # check if game is over
            if self.m_Nim.game_over():
                self.printEndMessage()
                
            if self.NextPlayer == 1:
                # update piles with the computer's move
                self.m_Nim.cp_moves()
                self.NextPlayer = 0
                print("Now it's your turn to make a move...")
                #time.sleep(1)
                
            # check if game is over
            if self.m_Nim.game_over():
                self.printEndMessage()
            
        # update stack displays
        self.m_ui.leftStack.setText(str(self.m_Nim.piles[0]))
        self.m_ui.middleStack.setText(str(self.m_Nim.piles[1]))
        self.m_ui.rightStack.setText(str(self.m_Nim.piles[2]))
        
    # @brief Checks pile inputs for the user's move
    # @details Checks the inputs for each pile to determine what pile the user has
    # selected to remove from and the amount the want to take away.
    def checkUserInput(self):
        #if self.m_ui.playButton.text() == 'Enter':
        stackInputs = [self.m_ui.userInput.itemAt(i).widget() for i in range(self.m_ui.userInput.count())]
        count = 0
        pile = 0
        n_rem = 0
        for i in range(len(stackInputs)):  # check that input is not empty
            if stackInputs[i].text():
                count += 1  # keeps track of how many piles had input
                pile = i  # save the pile user entered input for
                n_rem = int(stackInputs[i].text())
            # clear the QLineEdit widgets
            stackInputs[i].clear()
                
        # check that the user's input are valid moves
        if count > 1 or count < 1:
            print('You can only remove rocks from one pile, Try again')
            pile = None
            n_rem = None
        elif pile not in range(3):
            print('Not a valid pile choice, Try again')
            pile = None
            n_rem = None
        elif self.m_Nim.piles[pile] <= 0:
            print('That pile is empty, Choose another pile')
            pile = None
            n_rem = None
        elif (n_rem <= 0) or (n_rem > self.m_Nim.piles[pile]):
            print('Not a valid amount to remove, Try again')
            pile = None
            n_rem = None
               
        return pile, n_rem
                    
            
    def playGame(self):
        # chcek piles and see if game is over
        while self.m_Nim.game_over():
            # update piles with players' moves
            self.updatePiles()
            QtGui.qApp.processEvents()
            time.sleep(1)
        
        # game is over; print closing messages
        self.printEndMessage()
    
    # @brief prints a message when the game is over
    # @details Prints a game over banner to the terminal window and presetns a message
    # based on whether the user wins or loses.
    def printEndMessage(self):
        self.m_Nim.print_game_over()
        if self.NextPlayer == 0:
            print("Congratulations!! You have won...Tell me how you did it")
        else:
            print("Sorry, but you LOST! You should keep trying.")
            
        # reset the game
        self.resetGame()
    
    # @brief resets the pile displays
    # @details This function resets the piles to 0 and updates the stack displays.
    def resetGame(self):
        print('The game has been reset...')
        # reset the stacks to 0
        self.m_ui.leftStack.setText(str(0))
        self.m_ui.middleStack.setText(str(0))
        self.m_ui.rightStack.setText(str(0))
        
        # enable play button and disable reset button
        #self.m_ui.playButton.setEnabled(True)
        self.m_ui.playButton.setText("PLAY")
        self.m_ui.resetButton.setEnabled(False)
        # disconnect updatePiles function from playButton
        self.m_ui.playButton.disconnect()
        # connect startGame function to playButton
        self.m_ui.playButton.clicked.connect(self.startGame)
    
