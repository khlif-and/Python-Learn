import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.setWindowTitle("Pelajaran ke 2 : Memasukan widget ke dalam window")

        self.mainLayout = QVBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.centralWidget.setLayout(self.mainLayout)

        self.welcomeLabel = QLabel("hello user")
        self.mainLayout.addWidget(self.welcomeLabel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
