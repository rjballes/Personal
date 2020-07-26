# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:49:57 2020

@author: Raymart Ballesteros
"""


# Filename: hello.py

# Simple hello world example with PyQt5

import sys

# import QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of application's gui
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,200,80)
window.move(60,15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60,15)

# Show application's gui
window.show()

# Run application's event loop (or main loop)
sys.exit(app.exec())

