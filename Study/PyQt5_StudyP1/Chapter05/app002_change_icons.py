# app002_change_icons.py
# import necessary modules

import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import random

class ChangeIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("Set Icons Example")
        self.setWindowIcon(QIcon('images/logo01.png'))

        self.createWidgets()

        self.show()

    def createWidgets(self):
        """
        Set up widgets.
        """
        info_label = QLabel("Click on the button and select a fruit.")

        self.images = [
            "images/logo02.png",
            "images/logo03.png",
            "images/logo04.png",
            "images/logo05.png"
        ]

        self.icon_button = QPushButton(self)
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonICon)

        # Create vertical layout and add widgets.
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)

        # Set main layout of window.
        self.setLayout(v_box)

    def changeButtonICon(self):
        """
        When the button is clicked, change the icon to one of the images in the list.
        """
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))

# Run application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeIcon()
    sys.exit(app.exec_())