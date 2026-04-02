import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.setWindowTitle("Pelajaran ke 4 : Menggunakan Nested layout")

        self.mainLayout = QVBoxLayout()
        self.ButtonRow = QHBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        self.headerLabel = QLabel("Hallo apa kabar")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: blue;"
        )
        self.mainLayout.addWidget(self.headerLabel)

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")

        self.ButtonRow.addWidget(self.button1)
        self.ButtonRow.addWidget(self.button2)
        self.ButtonRow.addWidget(self.button3)

        self.mainLayout.addLayout(self.ButtonRow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
