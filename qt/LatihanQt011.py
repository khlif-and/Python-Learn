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
    QListWidget,
    QListWidgetItem,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Latihan 10: Membuat List Widget")
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.mainLayout.setContentsMargins(50, 50, 50, 50)
        self.mainLayout.setSpacing(25)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.centralWidget.setStyleSheet(
            """
            #centralWidget {
                background-color: #121212;
            }
            QLineEdit {
                background-color: #2A2A2A;
                color: #FFFFFF;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
                padding: 15px 20px;
                border: 1px solid transparent;
                border-radius: 12px;
            }
            QLineEdit:focus {
                background-color: #333333;
                border: 1px solid #1DB954;
            }
            QPushButton {
                background-color: #1DB954;
                color: #000000;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: bold;
                padding: 15px 30px;
                border: none;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
            QPushButton:pressed {
                background-color: #14833b;
            }
            QPushButton#btnHapus {
                background-color: transparent;
                color: #EF4444; 
                border: 2px solid #EF4444;
            }
            QPushButton#btnHapus:hover {
                background-color: #EF4444;
                color: #FFFFFF;
            }
            QListWidget {
                background-color: #1A1A1A;
                color: #E5E5E5;
                font-family: 'Segoe UI', sans-serif;
                font-size: 18px;
                border: 1px solid #333333;
                border-radius: 16px;
                padding: 10px;
                outline: none;
            }
            QListWidget::item {
                padding: 15px;
                border-radius: 8px;
            }
            QListWidget::item:selected {
                background-color: #2A2A2A;
                color: #1DB954; 
            }
            QListWidget::item:hover {
                background-color: #333333;
                color: #FFFFFF;
            }
            """
        )

        self.button = QPushButton("submit")
        self.button.clicked.connect(self.on_button_submit_clicked)
        self.mainLayout.addWidget(self.button)

        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText("masukan nama disini")

        self.listWidget = QListWidget()
        self.listWidget.setDragEnabled(True)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDragDropMode(QListWidget.DragDropMode.InternalMove)
        self.listWidget.addItems(
            ["main HP", "nonton bola", "pacaran video call full percakapan"]
        )
        self.mainLayout.addWidget(self.listWidget)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.addWidget(self.nameInput)

        self.buttonAdd = QPushButton("tambah")
        self.buttonAdd.clicked.connect(self.btn_on_clicked)
        self.inputLayout.addWidget(self.buttonAdd)

        self.buttonDelete = QPushButton("hapus")
        self.buttonDelete.setObjectName("btnHapus")
        self.buttonDelete.clicked.connect(self.delete_item)
        self.inputLayout.addWidget(self.buttonDelete)

        self.mainLayout.addLayout(self.inputLayout)

        self.playlistItem = QListWidgetItem()
        self.playlistItem.setText("main HP")
        self.listWidget.addItem(self.playlistItem)

    def btn_on_clicked(self):
        self.nameInput.text()
        self.listWidget.addItem(self.nameInput.text())

    def delete_item(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def on_button_submit_clicked(self):
        self.nameInput.text()
        self.listWidget.addItem(self.nameInput.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
