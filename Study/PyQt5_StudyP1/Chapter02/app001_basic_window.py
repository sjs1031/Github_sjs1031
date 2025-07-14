# app001_basic_window.py
# import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100,100, 400,300)
        self.setWindowTitle('Empty Window in PyQT')
        self.show()

# Run Program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())