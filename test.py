import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    hello = QtWidgets.QLabel('Hello, World!')
    hello.show()
    sys.exit(app.exec_())
