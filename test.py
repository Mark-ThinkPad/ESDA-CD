import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtSql import QSqlDatabase


def connection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(':memory:')
    if not db.open():
        QMessageBox.critical()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    connection()
    sys.exit(app.exec_())
