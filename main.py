from PyQt5 import QtWidgets
from PyQt5.Qt import QMessageBox
import sys
from guipoint import Ui_MainWindow
from point import Point

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.point = Point()

        try:
            self.point.download()
        except Exception:
            print("Error download")

        self.ui.labelKoor.setText(self.point.strKor())
        self.ui.labelSpeed.setText(self.point.strSpeed())

        self.ui.pushButton.clicked.connect(self.updatePoint)

    def updatePoint(self):
        F = []
        F.append(self.ui.doubleSpinBoxFx.value())
        F.append(self.ui.doubleSpinBoxFy.value())
        F.append(self.ui.doubleSpinBoxFz.value())
        t = self.ui.spinBoxTime.value()
        self.point.action(t, F)
        self.ui.labelKoor.setText(self.point.strKor())
        self.ui.labelSpeed.setText(self.point.strSpeed())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Выход", "Хотите выйти?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.point.save()
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec())
