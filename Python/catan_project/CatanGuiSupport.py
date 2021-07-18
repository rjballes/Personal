# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:48:36 2021

@author: Raymart Ballesteros
@package: CatanGuiSupport
@brief: This package contains the supporting methods for the CatanBoardGui.
"""

# imports
# Catan classes
from CatanBoard import CatanBoard
# PyQt5 Utilities
from PyQt5 import QtWidgets, QtGui, QtCore
#from PyQt5.QtCore import QThread
#from PyQt5.QtWidgets import QMessageBox, QGraphicsScene
# other utilities
import sys
import os
import time
import math
import statistics


class GUIWindow(QtWidgets.QMainWindow):
    ## constructor
    def __init__(self, inputUI, parent=None):
        super(GUIWindow, self).__init__(parent)
        self.m_ui = inputUI
        self.m_ui.setupUi(self)
        
        edgeLength = math.floor( min(self.m_ui.verticalLayoutWidget.height(), self.m_ui.verticalLayoutWidget.width()) / 9 )
        self.m_catanBoard = CatanBoard(edgeLength)
        
        self.createHexMap()
        
        # Actions to functions linkage
        self.m_ui.genBoardButton.clicked.connect(self.generateBoardAction)
    
    
    def createHexMap(self):
        self.gameBoardScene = QtWidgets.QGraphicsScene()
        self.m_ui.gameBoardView.setScene(self.gameBoardScene)
        self.gameBoardPen = QtGui.QPen(QtCore.Qt.black, 6, QtCore.Qt.SolidLine)
        
        self.listOfPolygonTiles = []
        for k in range(19):
            #TODO: Add method for returning list of tile vertices
            points = [self.m_catanBoard.getATile(k).getTileVertex(m).getCoords() for m in range(6)]
            poly = self.gameBoardScene.addPolygon(QtGui.QPolygonF( points ))
            self.listOfPolygonTiles.append(poly)
            poly.setPen(self.gameBoardPen)
    
    
    def generateBoardAction(self):
        #TODO Possibly add a window for user to select type of generation
        self.m_catanBoard.generateGameBoard()
        
        fullPath = os.getcwd() + "\\catan_images"
        gameBoardBrush = QtGui.QBrush()
        self.tileBackgrounds = []
        #TODO Consider improvements to how to track the paths for the images and store this info
        pixmap = QtGui.QPixmap(fullPath + "\\tanjiro-water-breathing.jpg")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        pixmap = QtGui.QPixmap(fullPath + "\\kocho-insect-breathing.png")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        pixmap = QtGui.QPixmap(fullPath + "\\inosuke-beast-breathing.jpg")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        pixmap = QtGui.QPixmap(fullPath + "\\rengoku-fire-breathing.jpg")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        pixmap = QtGui.QPixmap(fullPath + "\\nezuko-blood-demon-art.png")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        pixmap = QtGui.QPixmap(fullPath + "\\zenitsu-thunder-breathing.jpg")
        pixmap = pixmap.scaledToHeight( math.floor(self.m_ui.verticalLayoutWidget.height() / 9) )
        self.tileBackgrounds.append(pixmap)
        
        # TODO Consider different approach for accessing the polygon tile objects
        for k in range(19):
            #TODO consider having different brushes for each image/pattern
            gameBoardBrush.setTexture(self.tileBackgrounds[self.m_catanBoard.getATile(k).getResourceType().value])
            self.listOfPolygonTiles[k].setBrush(gameBoardBrush)
            
            points = [self.m_catanBoard.getATile(k).getTileVertex(m).getCoords() for m in range(6)]
            x_c = statistics.mean( [p.x() for p in points] )
            y_c = statistics.mean( [p.y() for p in points] )
            elItem = self.gameBoardScene.addEllipse(x_c-20, y_c-20, 40, 40)
            elItem.setPen(QtGui.QPen(QtCore.Qt.black, 4, QtCore.Qt.SolidLine))
            elItem.setBrush(QtGui.QColor(114, 164, 225))
            textItem = self.gameBoardScene.addText(str( self.m_catanBoard.getATile(k).getTileValue() ))
            font = QtGui.QFont('Fantasy', 18, QtGui.QFont.Bold)
            textItem.setFont(font)
            textItem.setPos(QtCore.QPointF(x_c,y_c) - textItem.boundingRect().center())
        

    