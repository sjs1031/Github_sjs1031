# app003_checkboxes.py
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QCheckBox)
from PyQt5.QtCore import Qt

class CheckBoxWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100,100, 250,250)
        self.setWindowTitle("QcheckBOX Widget")
        self.displayCheckBoxes()

        self.show()
    
    def displayCheckBoxes(self):
        '''
        Setup the checkboxes and other widgets
        '''
        header_label = QLabel(self)
        header_label.setText("Which shift can you work? (Please check all that apply.)")
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        # Set up checkboxes
        morning_cb = QCheckBox("Morning [8 AM-2 PM]", self) # text, parent 
        morning_cb.move(20, 80)
        #morning_cb.toggle() # Uncomment if you wnat box to start off checked, show as an example here.add()
        morning_cb.stateChanged.connect(self.printToTerminal)

        after_cb = QCheckBox("Afternoon [1 PM-8 PM]", self) # text, parent
        after_cb.move(20, 100)
        after_cb.stateChanged.connect(self.printToTerminal)

        night_cb = QCheckBox("Night [7 PM-3 AM]", self) # text, parent
        night_cb.move(20, 120)
        night_cb.stateChanged.connect(self.printToTerminal)

    def printToTerminal(self, state): # pass state of checkbox
        '''
        Simple function to show how to determain the state of a checkbox. Prints the txtt label of the checkbox by determining which widget is sending the signal.
        '''
        sender = self.sender()
        if state == Qt.Checked:
            print("{} Selected.".format(sender.text()))
        else:
            print("{} DeSelected.".format(sender.text()))
    
# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())
        
