# app001_basic_window.py
# Import necessary modules

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and sidplkay its contents to the screen.
        """
        self.setGeometry(100,100, 400,300)
        self.setWindowTitle('Empty Window in PyQt')
        self.show()

# run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())