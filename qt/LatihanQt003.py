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
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.setWindowTitle("Pelajaran ke 3 = Masukan widget ke dalam window")

        self.mainLayout = QVBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        self.welcomeLabel = QLabel("hello user ganteng")
        self.welcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcomeLabel.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: blue;"
        )
        self.mainLayout.addWidget(self.welcomeLabel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
