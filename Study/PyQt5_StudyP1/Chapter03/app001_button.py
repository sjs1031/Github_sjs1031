# app001_button.py
# import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        initialize the window and display its contents to the screen.
        """
        self.setGeometry(100,100, 200,150)
        self.setWindowTitle("QPushButton Widget")
        self.displayButton() # Call our diaplayButton Function

        self.show()
    
    def displayButton(self):
        """
        Setup the button widget
        """
        name_label = QLabel(self)
        name_label.setText("Don't push the button.")
        name_label.move(60,30) # arrange label

        button = QPushButton('Push Me', self)
        button.clicked.connect(self.buttonClicked)
        button.move(80,70) # arrange button

    def buttonClicked(self):
        '''
        Print Message to the terminal, and close the window button is clicked.
        '''
        print("The window has been closed.")
        self.close()
    
# Run Program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window  = ButtonWindow()
    sys.exit(app.exec_())