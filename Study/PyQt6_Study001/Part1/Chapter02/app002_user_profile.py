# app003_user_profile.py
# Import necessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    """"""
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setGeometry(50,50, 250,400)
        self.setWindowTitle("2.1 - User Profile GUI")

        self.setUpMainWindow()
        self.show()
    
    def setUpMainWindow(self):
        """Create the labels to be displayed in the window."""
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("RuleXuan")
        user_label.setFont(QFont("Arial",20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15,170)

        about_label = QLabel(self)
        about_label.setText("I'm a Software Engineer with 10 years\ experience creating awesome code.")
        about_label.setWordWrap(True)
        about_label.move(15, 190)

        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python  |  GO  |  SQL  |  Rust")
        languages_label.move(15, 260)

        experience_lebel = QLabel(self)
        experience_lebel.setText("Experience")
        experience_lebel.setFont(QFont("Arial", 17))
        experience_lebel.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python Developer")
        developer_label.move(15, 310)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Mar 2011 - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)

        driver_label = QLabel(self)
        driver_label.setText("Pizza Delivery Driver")
        driver_label.move(15,350)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)
    
    def createImageLabels(self):
        """Open image files and create image labels."""
        images = ["images/background.png","images/RuleXuan.jpg"]

        for image in images:
            try :
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/RuleXuan.jpg":
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

