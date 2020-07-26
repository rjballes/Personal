# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:02:53 2020

@author: Raymart Ballesteros
"""


# Filename: signals_slots.py
# signals and slots example

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def greeting():
    """ Slot function """
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")
        
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
