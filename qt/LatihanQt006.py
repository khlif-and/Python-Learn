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
    QLineEdit,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.setWindowTitle("Pelajaran ke 6 : Membuat Kotak Dalam Input")

        self.mainLayout = QVBoxLayout()
        self.ButtonRow = QHBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        self.headerLabel = QLabel("Hello User")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: blue;"
        )
        self.mainLayout.addWidget(self.headerLabel)

        self.buttonClick = QPushButton("Click Here")
        self.buttonClick.setStyleSheet(
            "font-size: 20px; color: #ffffff; background-color: #000000; border-radius: 10px; padding: 10px; margin-left: 50px; margin-right: 50px;"
        )
        self.buttonClick.clicked.connect(self.on_button_clicked)
        self.ButtonRow.addWidget(self.buttonClick)
        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText("masukan nama kamu")
        self.mainLayout.addWidget(self.nameInput)
        # self.mainLayout.addWidget(self.buttonClick)
        self.mainLayout.addLayout(self.ButtonRow)

    def on_button_clicked(self):
        name = self.nameInput.text()
        QMessageBox.information(self, "Info", f"Hello {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
