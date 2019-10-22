import sys
from PyQt5 import QtCore, QtWidgets
from Main import Ui_MainWindow
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        
        
        self.create_DB()

        self.ui.pushButton.clicked.connect(self.print_data)
        self.model = None
        self.ui.pushButton.clicked.connect(self.sql_tableview_model)
        self.ui.pushButton_2.clicked.connect(self.sql_add_row)
        self.ui.pushButton_3.clicked.connect(self.sql_delete_row)
       

        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
  
    def sql_delete_row(self):
        if self.model:
          
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            
        else:
            self.sql_tableview_model()
              
                

    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
          
        else:
            self.sql_tableview_model()
          


    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Ordenes.db')
        
        tableview = self.ui.tableView
      
        
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        tableview.setModel(self.model)
        
        self.model.setTable('ORDEN')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "orderNumber")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "orderDate")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "requiredDate")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "shippedDate")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "status")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "comments")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "customerNumber")
        


    def print_data(self):
        sqlite_file = 'Ordenes.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'ORDEN' ORDER BY orderNumber")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       
        conn.close()        
        

    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Ordenes.db')
        db.open()
    
        query = QtSql.QSqlQuery()
        
        
        query.exec_("create table ORDEN (orderNumber int(10) primary key,"
                    "orderDate date, requiredDate date, shippedDate date,"
                    "status varchar(15), comments varchar(10), customerNumber int(10))")
      
        query.exec_("insert into ORDEN values(1000, '2018-10-2', '2018-10-5', '2018-10-3', 'In progress', 'All green', '2000')")
        query.exec_("insert into ORDEN values(3000, '2018-10-8', '2018-10-9', '2018-10-10', 'Stopped', 'Rejected', '4000')")
        query.exec_("insert into ORDEN values(5000, '2018-10-13', '2018-10-15', '2018-10-15', 'In progress', 'All green', '6000')")
        query.exec_("insert into ORDEN values(7000, '2018-10-20', '2018-10-22', '2018-10-22', 'Received', 'All green', '8000')")
        

if __name__ == "__main__":
    MainWindow_EXEC()
