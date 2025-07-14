# app005_restration.py
# import necessary modules

import sys
from PyQt6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap

class NewUserDialog(QDialog):
    """"""
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(360,320)
        self.setWindowTitle("3.1 - Restration GUI")
        self.setUpWindow()

    def setUpWindow(self):
        """Creating and arrange widgets in the windows for collecting new account information."""
        login_label = QLabel("Create New Account", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(90, 20)

        # Create QLabel for image
        user_image = "images/RuleXuan.jpg"

        try:
            with open(user_image):
                user_label = QLabel(self)
                pixmap = QPixmap(user_image)
                user_label.setPixmap(pixmap)
                user_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found. ERROR: {error}")
    
        # Create name Qlabel and QlineEdit widgets
        name_label = QLabel("Username:", self)
        name_label.move(20, 144)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(250, 24)
        self.name_edit.move(90, 140)

        full_name_label = QLabel("Full Name:", self)
        full_name_label.move(20, 174)

        full_name_edit = QLineEdit(self)
        full_name_edit.resize(250, 24)
        full_name_edit.move(90, 170)

        # Create password Qlabel and QlineEdit widgets
        new_pswd_label = QLabel("Password:", self)
        new_pswd_label.move(20, 204)

        self.new_pswd_edit = QLineEdit(self)
        self.new_pswd_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_pswd_edit.resize(250, 24)
        self.new_pswd_edit.move(90, 200)

        confirm_label = QLabel("Confirm:", self)
        confirm_label.move(20, 234)

        self.confirm_edit = QLineEdit(self)
        self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_edit.resize(250, 24)
        self.confirm_edit.move(90, 230)

        # Create sign up Qpushbutton
        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20, 270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        """check if user information is entered and correct. If so, append username and password text to file."""
        name_text = self.name_edit.text()
        pswd_text = self.new_pswd_edit.text()
        confirm_text = self.confirm_edit.text()

        if name_text == "" or pswd_text == "" or confirm_text == "":
            # Display QmessageBox if passwords don't match
            QMessageBox.warning(self, "Error Message", "Please enter username or password values.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        elif pswd_text != confirm_text:
            # Display QmessageBox if passwords do not match
            QMessageBox.warning(self, "Error Message", "The Passwords you entered  do not match.", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else :
            # Rerurn to login window if passwords match
            with open("files/user.txt", "a+") as f:
                f.write("\n"+ name_text + " ")
                f.write(pswd_text)
            self.close()