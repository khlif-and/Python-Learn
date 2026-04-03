import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QPushButton,
    QMessageBox,
    QRadioButton,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pelajaran ke 9 : Premium Glassmorphism UI")
        self.setMinimumSize(1200, 800)
        self.showMaximized()

        # Central Widget & Main Layout
        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.mainLayout.setContentsMargins(50, 50, 50, 50)
        self.mainLayout.setSpacing(25)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Global Stylesheet for Glassmorphism
        self.centralWidget.setStyleSheet(
            """
            #centralWidget {
                background-color: #121212;
            }
            QLabel {
                color: #FFFFFF;
                font-family: 'Circular', 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', 'Helvetica Neue', sans-serif;
                font-size: 18px;
                font-weight: 700;
                background: transparent;
            }
            QLineEdit, QComboBox {
                background-color: #242424;
                color: #FFFFFF;
                font-family: 'Circular', 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
                font-size: 16px;
                font-weight: 500;
                padding: 14px 20px;
                border: 1px solid transparent;
                border-radius: 4px; /* Spotify doesn't use ultra-rounded inputs, just slight curves */
            }
            QLineEdit:hover, QComboBox:hover {
                background-color: #2A2A2A;
                border: 1px solid #727272;
            }
            QLineEdit:focus, QComboBox:focus {
                background-color: #333333;
                border: 1px solid #FFFFFF; /* High contrast focus */
            }
            QPushButton {
                background-color: #1DB954; /* Spotify Green */
                color: #000000;
                font-family: 'Circular', 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: 800;
                letter-spacing: 0.5px;
                padding: 16px 40px;
                border-radius: 26px; /* Pill shaped */
                border: none;
                min-width: 250px;
            }
            QPushButton:hover {
                background-color: #1ed760; /* Slightly lighter green on hover */
            }
            QPushButton:pressed {
                background-color: #14833b;
                padding-top: 18px;
                padding-bottom: 14px;
            }
            QComboBox::drop-down {
                border: none;
                width: 40px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #FFFFFF;
                margin-right: 15px;
            }
            QComboBox QAbstractItemView {
                background-color: #282828;
                color: #FFFFFF;
                font-family: 'Circular', 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
                border: 1px solid #3E3E3E;
                selection-background-color: #3E3E3E;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                padding: 10px;
                min-height: 25px;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #3E3E3E;
            }
            QRadioButton {
                color: #B3B3B3; /* Secondary text color */
                font-family: 'Circular', 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
                font-size: 16px;
                font-weight: 500;
                spacing: 12px;
                background: transparent;
            }
            QRadioButton:hover {
                color: #FFFFFF;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 11px;
                border: 2px solid #B3B3B3;
                background-color: transparent;
            }
            QRadioButton::indicator:hover {
                border: 2px solid #FFFFFF;
            }
            QRadioButton::indicator:checked {
                background-color: #1DB954;
                border: 5px solid #121212; /* Creates the inner dot effect */
            }
        """
        )

        # UI Components
        self.labelInput = QLabel("Pilih Data & Masukkan Nama")
        self.labelInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.labelInput)

        self.inputNameUser = QLineEdit()
        self.inputNameUser.setPlaceholderText("Siapa nama kamu?")
        self.mainLayout.addWidget(self.inputNameUser)

        self.comboHobby = QComboBox()
        self.comboHobby.addItems(["Berenang 🏊‍♂️", "Membaca 📚", "Bermain Game 🎮"])
        self.mainLayout.addWidget(self.comboHobby)

        self.buttonSubmit = QPushButton("🚀 SUBMIT DATA")
        self.buttonSubmit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.buttonSubmit.clicked.connect(self.on_button_submit_clicked)
        self.mainLayout.addWidget(self.buttonSubmit)

        self.radioButton = QRadioButton("Pilih Data & Masukan nama")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.on_radio_toggled)
        self.mainLayout.addWidget(self.radioButton)

        # Result Label
        self.resultLabel = QLabel("")
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultLabel.setStyleSheet(
            "font-size: 20px; color: #1DB954; font-weight: bold; margin-top: 20px;"
        )
        self.mainLayout.addWidget(self.resultLabel)

    def on_button_submit_clicked(self):
        name = self.inputNameUser.text()
        hobby = self.comboHobby.currentText()
        if not name:
            self.resultLabel.setText("Silakan isi nama kamu dulu ya! ✨")
        else:
            self.resultLabel.setText(
                f"Halo {name}! Hobi kamu {hobby} keren juga ya! 🔥"
            )

    def on_radio_toggled(self):
        if self.radioButton.isChecked():
            self.resultLabel.setText("Radio button is checked")
        else:
            self.resultLabel.setText("Radio button is unchecked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
