import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.setWindowTitle("Pelajaran ke 5 : Menggunakan Clicked")

        self.mainLayout = QVBoxLayout()
        self.buttonRow = QHBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        self.HeaderLabel = QLabel("Hello User")
        self.HeaderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HeaderLabel.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: blue;"
        )
        self.mainLayout.addWidget(self.HeaderLabel)

        self.buttonHello = QPushButton()
        self.buttonHello.setStyleSheet(
            "font-size: 20px; color: #ffffff; background-color: #000000; border-radius: 10px; padding: 10px;"
        )
        self.buttonHello.setText("Click Me")
        self.buttonRow.addWidget(self.buttonHello)

        self.mainLayout.addLayout(self.buttonRow)

        self.buttonHello.clicked.connect(self.handle_click)

    def handle_click(self):
        QMessageBox.information(self, "Info", "Button berhasil di klik")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
