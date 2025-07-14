# app003_user_profile.py
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
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(50,50, 760,760)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.displayImages()
        self.displayUserInfo()

        self.show()

    def displayImages(self):
        """
        Display background and profile images.
        Check to see if image files exist, if not throw an exception.
        """
        background_image = "images/background.png"
        profile_image = "images/RuleXuan.jpg"

        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Background image not found.")
        
        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(18,18)
        except FileNotFoundError:
            print("Profile image not found.")

    def displayUserInfo(self):
        """
        Create the labels to be displayed for the user Profile.`
        """
        user_name = QLabel(self)
        user_name.setText("RuleXuan")
        user_name.move(20,100)
        user_name.setFont(QFont('Arial',20))

        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15,170)
        bio_title.setFont(QFont('Arial',17))

        about = QLabel(self)
        about.setText("I'm a Software Engineer with N years experience creating awesome code.")
        about.setWordWrap(True)
        about.move(15,190)

        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15,240)
        skills_title.setFont(QFont('Arial', 17))

        skills = QLabel(self)
        skills.setText("Python  |  JAVA  |  GO  |  RUST  | SQL")
        skills.move(15,260)

        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15,290)
        experience_title.setFont(QFont('Arial', 17))

        experience = QLabel(self)
        experience.setText("Python Developer")
        experience.move(15,310)

        dates = QLabel(self)
        dates.setText("Mar 2024 - Present")
        dates.move(15,330)
        dates.setFont(QFont('Arial', 10))

        experience = QLabel(self)
        experience.setText("Pizza Delivery Driver")
        experience.move(15,350)

        dates = QLabel(self)
        dates.setText("Aug 2014 - Dec 2017")
        dates.move(15,370)
        dates.setFont(QFont('Arial', 10))
    
# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = UserProfile()
    sys.exit(app.exec_())


    
