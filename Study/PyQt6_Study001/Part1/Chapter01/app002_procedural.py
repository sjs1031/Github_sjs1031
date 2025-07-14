# app002_procedural.py
# 1. Import necessary modules
import sys # use sys to accept command line arguments
from PyQt6.QtWidgets import QApplication, QWidget

# 2. Create QApplication object
app = QApplication(sys.argv)

# 3. Create window from QWidget object
window = QWidget()

# 4. Call show to display GUI window
window.show()

# 4. Start the event loop. use sys.exit to close program
sys.exit(app.exec())