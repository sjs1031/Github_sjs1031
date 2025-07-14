# app003_user_profile_GUI.py
# import necessary modules

import sys, os.path
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont, QPixmap

class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(50,50, 250,400)
        self.setWindowTitle('2.1 - User Profile GUI')
        self.displayImages()
        self.displayUserInfo()

        self.show()

    def displayImages(self):
        """
        Display background and profile images.
        Check to see if image files exist, if not throw an exception.
        """
        background_image = "images/background.jpg"
        profile_image = "images/rulexuan.jpg"

        try :
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found")

        try :
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80, 20)
        except FileNotFoundError:
            print("Image not found")
        
    def displayUserInfo(self):
        """
        Create the labels to be displayed for the USer Profile.
        """
        user_name = QLabel(self)
        
        