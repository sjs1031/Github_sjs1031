# app001_labels.py
# import necessary modules

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("QLabel Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create QLabel to be displayed in the main window."""
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(105, 15)

        image = "images/RuleXuan.jpg"
        try:
            with open(image):
                rulexuan_image= QLabel(self)
                pixmap = QPixmap(image)
                rulexuan_image.setPixmap(pixmap)
                rulexuan_image.move(50, 60)
        except FileNotFoundError as error:
            print(f"Image not Found.\nError: {error}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())