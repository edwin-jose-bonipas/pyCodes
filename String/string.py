print("hello world")


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
import sys


def main():
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")

    msg.show()
    sys.exit(app.exec_())


main()  # make sure to call the function