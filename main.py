import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_magaz.triggered.connect(self.open_magaz_file)

    def open_magaz_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '.', 'Таблица(*.csv)')
        with open(filename) as f:
            head = f.readline().replace('\n', '').split(';')
            data = [line.replace('\n', '').split(';') for line in f.readlines()]
            print(data)

            self.table_magaz.setColumnCount(len(head))
            self.table_magaz.setRowCount(len(data))

            self.table_magaz.setHorizontalHeaderLabels(head)

            for row in range(self.table_magaz.rowCount()):
                for column in range(self.table_magaz.columnCount()):
                    item = QTableWidgetItem(data[row][column])
                    self.table_magaz.setItem(row, column, item)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
