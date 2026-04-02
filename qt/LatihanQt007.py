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

        self.setWindowTitle("Pelajaran ke 7 : Pengulangan Materi")

        self.mainLayout = QVBoxLayout()
        self.buttonRow = QHBoxLayout()

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        self.nameInput = QLineEdit()

        self.headerLabel = QLabel(f"Hello {self.nameInput.text()}")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: blue;"
        )
        self.mainLayout.addWidget(self.headerLabel)

        self.buttonClick = QPushButton("Click me")
        self.buttonClick.setStyleSheet(
            """
    QPushButton {
        background-color: #FFFFFF;
        color: #2D3436;
        border: 1px solid #DFE6E9;
        border-radius: 5px;
        font-size: 14px;
        padding: 10px;
        /* Shadow disimulasikan dengan border bawah yang tebal */
        border-bottom: 3px solid #B2BEC3;
    }
    QPushButton:pressed {
        border-bottom: 1px solid #B2BEC3;
        margin-top: 2px;
    }
"""
        )
        self.buttonClick.clicked.connect(self.on_button_clicked)
        self.buttonRow.addWidget(self.buttonClick)
        self.mainLayout.addLayout(self.buttonRow)

        self.nameInput.setPlaceholderText("masukan nama kamu")
        self.nameInput.setStyleSheet(
            """
    QLineEdit {
        border: none;
        border-bottom: 2px solid #B2BEC3;
        background-color: transparent;
        padding: 5px;
        font-size: 15px;
        color: #333;
    }
    QLineEdit:focus {
        border-bottom: 2px solid #0078D4;
    }
"""
        )
        self.mainLayout.addWidget(self.nameInput)

    def on_button_clicked(self):
        self.name = self.nameInput.text()
        self.headerLabel.setText(f"hello {self.name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
