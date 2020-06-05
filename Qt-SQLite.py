import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtCore import Qt, QObject


def connect(app: QApplication) -> bool:
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(':memory:')
    if not db.open():
        QMessageBox.critical(None, app.tr('Cannot open database'),
                             app.tr('''
                             Unable to establish a database connection.
                             This example needs SQLite support. Please
                             read the Qt SQL driver documentation for
                             information how to build it.

                             Click Cancel to exit.    
                             '''), QMessageBox.Cancel)
        return False
    query = QSqlQuery()
    query.exec('''
    create table person
    (
        id int primary key,
        firstname varchar(20),
        lastname varchar(20)
    )
    ''')
    query.exec("insert into person values (201, '张', '三')")
    query.exec("insert into person values (202, '李', '四')")
    query.exec("insert into person values (203, '王', '五')")
    query.exec("insert into person values (204, '赵', '六')")
    query.exec("insert into person values (205, '孙', '七')")
    return True


def initModel(model: QSqlQueryModel):
    model.setQuery("select * from person")
    model.setHeaderData(0, Qt.Horizontal, 'ID')
    model.setHeaderData(1, Qt.Horizontal, 'First Name')
    model.setHeaderData(2, Qt.Horizontal, 'Last Name')


def createView(model: QSqlQueryModel, title: str = '') -> QTableView:
    view = QTableView()
    view.setModel(model)
    offset = 0
    view.setWindowTitle(title)
    view.move(offset+100, offset+100)
    offset += 20
    return view


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not connect(app):
        sys.exit(1)
    plainModel = QSqlQueryModel()
    initModel(plainModel)
    tableView = createView(plainModel, 'Plain Query Model')
    tableView.show()
    sys.exit(app.exec_())
