# app001_labels.py
# Import nexessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    """"""
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setGeometry(600,200,450,450)
        self.setWindowTitle("QLabel Example")

        self.setUpMainWindow()
        self.show()
    
    def setUpMainWindow(self):
        """Create QLabel to be displayed in the main window"""
        hello_label = QLabel(self)
        hello_label.setText("Hello")
        hello_label.move(205, 15)
        
        image = "images/world.jpg"
        try:
            world_label = QLabel(self)
            pixmap = QPixmap(image)
            world_label.setPixmap(pixmap)
            world_label.move(45,40)
        except FileNotFoundError as error:
            print(f"Image not found. \nERROR: {error}")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
