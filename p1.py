import sys
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hello = QLabel('Hello, World!')
    hello.show()
    sys.exit(app.exec_())
