# app001_Menubar.py
# impoer necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")

        self.setUpMainWindow()
        self.createActions()
        self.createMenus()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        pass

    def createActions(self):
        """Create the application's menu actions."""
        # Create action for File menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenus(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
