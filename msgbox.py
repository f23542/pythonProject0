import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class App(QWidget):

    def __init__(self):

        super().__init__()

        buttonReply = QMessageBox.question(

            self, 'APPIA', "Message Box",

            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No,

            QMessageBox.No

        )

        if buttonReply == QMessageBox.Yes:

            print('Yes clicked.')

        elif buttonReply == QMessageBox.Save:

            print('Save clicked.')

        elif buttonReply == QMessageBox.Cancel:

            print('Cancel clicked.')

        elif buttonReply == QMessageBox.Close:

            print('Close clicked.')

        elif buttonReply == QMessageBox.Reset:

            print('Reply clicked.')

        else:

            print('No clicked.')

        self.show()

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()

    sys.exit(app.exec_())
'''