# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from view.sushi import Ui_main
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MinhaJanelaMain(QMainWindow, Ui_main):

    def __init__(self, parent=None):
        super(MinhaJanelaMain, self).__init__(parent)
        self.setupUi(self)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MinhaJanelaMain()
    myWin.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
