# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import msgbox
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#    print_hi('PyCharm !')

    app = QApplication(sys.argv)

    ex = msgbox.App()

    sys.exit(app.exec_())

    # text file handling - for grub.cfg  error edit - divide by 'menuentry'




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
