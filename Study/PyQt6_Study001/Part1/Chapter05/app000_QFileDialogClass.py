# app000_QFileDialogClass.py
from PySide6.Qtwidgets import (QFileDialog, QInputDialog, QFontDialog, QColorDialog, QMessageBox)
from PySide6.QtGui import QFont, QIcon

class MainWindow(QMainWindow):
    """"""
    file_name, ok = QFileDialog.getOpenFileName(self, "Open File", "c:/Users/sjs10/OneDrive/git/CodeControl/Python/PyQtStudy001/images/", "Imgae FIles (*.png, *.jpg, *.bmp)")
    file_name, ok = QFileDialog.getSaveFileName(self, "Save File", "c:/Users/sjs10/OneDrive/git/CodeControl/Python/PyQtStudy001/Text", "Text Files (*.txt)")
    file_name, ok = QFileDialog.getOpenFileName(self, "Open File", "c:/Users/sjs10/OneDrive/git/CodeControl/Python/PyQtStudy001/Text","Image Files (*.png, *.jpg, *.bmp)", options = QFileDialog.Option.DontUseNativeDialog)

    find_text, ok = QInputDialog.getText(self, "Search Text", "Find:")

    font, ok = QFontDialog.getFont(QFont("Helvetica", 10), self)
    self.text_edit_widget.setCurrentFont(font)

    color = QColorDialog.getColor()

    if color.isValid():
        self.text_filed.setTextColor(color)

    QMessageBox.about(self, "About Notepad", """<p>Beginner's Practical Guide to PyQt</p><p>Project 5.1 -Notepad GUI</>""")

    app.setWindowIcon(QIcon("images/window.png"))
                      


