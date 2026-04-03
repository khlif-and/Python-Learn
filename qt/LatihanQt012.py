import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic


class MyApplication(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("LatihanQt012.ui", self)

        self.btn_add.clicked.connect(self.on_btn_add_clicked)

    def on_btn_add_clicked(self):
        print(self.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.showMaximized()
    window.setMinimumSize(1200, 800)
    sys.exit(app.exec())
