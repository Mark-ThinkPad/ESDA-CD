import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('Available drivers:')
    drivers = QSqlDatabase.drivers()
    for driver in drivers:
        print(driver)
    sys.exit(app.exec_())
