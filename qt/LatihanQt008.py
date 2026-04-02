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
    QComboBox,
)
from PyQt6.QtCore import Qt


class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1200, 800)
        self.showMaximized()
        self.setWindowTitle("pelajaran ke 8 : membuat commbobox")

        self.mainLayout = QVBoxLayout()
        self.buttonRow = QHBoxLayout()

        self.centraWidget = QWidget()
        self.setCentralWidget(self.centraWidget)
        self.centraWidget.setLayout(self.mainLayout)

        self.inputName = QLineEdit()
        self.mainlayout = QVBoxLayout()
        self.buttonRow = QHBoxLayout()
        self.comboBox = QComboBox()

        self.nameUser = QLabel("isi data dulu yuk")
        self.nameUser.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameUser.setStyleSheet(
            """
    QLabel {
        color: #F5F6FA;
        font-size: 20px;
        font-weight: 600;
        background-color: #353B48;
        border-left: 5px solid #00A8FF;
        padding: 10px 20px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
    }
"""
        )
        self.mainLayout.addWidget(self.nameUser)

        self.inputName.setPlaceholderText("masukan nama kamu")
        self.inputName.setStyleSheet(
            """
    QLineEdit {
        border: none;
        border-bottom: 2px solid #D2D6D9;
        background-color: transparent;
        padding: 8px 2px;
        font-size: 16px;
        color: #2D3436;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Efek saat kursor mendekat */
    QLineEdit:hover {
        border-bottom: 2px solid #B2BEC3;
    }
    
    /* Efek saat mulai mengetik */
    QLineEdit:focus {
        border-bottom: 3px solid #0984E3;
        color: #000000;
    }
    
    /* Warna teks petunjuk (placeholder) */
    QLineEdit::placeholder {
        color: #A0A0A0;
    }
"""
        )
        self.mainLayout.addWidget(self.inputName)

        self.comboHobby = QComboBox()
        self.comboHobby.addItems(["Berenang", "Membaca", "Bermain Game"])
        self.comboHobby.setStyleSheet(
            """
    QComboBox {
        border: 2px solid #DFE6E9;
        border-radius: 8px;
        padding: 5px 15px;
        font-size: 14px;
        color: #2D3436;
        background-color: #FFFFFF;
        min-width: 150px;
    }
    
    QComboBox:hover {
        border-color: #B2BEC3;
    }
    
    QComboBox:focus {
        border-color: #0984E3;
    }
    
    /* Area tombol panah */
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 30px;
        border-left: 1px solid #DFE6E9;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }
    
    /* Gambar panah - Jika tidak punya file .png, bisa pakai simbol bawaan */
    QComboBox::down-arrow {
        image: url(down_arrow.png); /* Pastikan file ada di folder */
        width: 14px;
        height: 14px;
    }

    /* Gaya untuk daftar pilihan (Popup) */
    QAbstractItemView {
        border: 2px solid #DFE6E9;
        border-radius: 8px;
        background-color: #FFFFFF;
        selection-background-color: #0984E3;
        selection-color: white;
        outline: none;
    }

    /* Gaya item di dalam list */
    QAbstractItemView::item {
        min-height: 35px;
        padding-left: 10px;
    }
"""
        )
        self.mainLayout.addWidget(self.comboHobby)

        self.buttonSubmit = QPushButton("Submit Here")
        self.buttonSubmit.setStyleSheet(
            """
    QPushButton {
        background-color: #0984E3;
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                    stop:0 #0984E3, stop:1 #00cec9);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
    }

    /* Efek saat kursor menyentuh tombol */
    QPushButton:hover {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                    stop:0 #74b9ff, stop:1 #81ecec);
        /* Sedikit efek shadow halus */
        border-bottom: 3px solid #0764AD;
    }

    /* Efek saat tombol ditekan (animasi klik) */
    QPushButton:pressed {
        background-color: #0764AD;
        padding-top: 14px; /* Membuat efek tombol tertekan ke bawah */
        border-bottom: none;
    }
"""
        )
        self.buttonSubmit.clicked.connect(self.on_button_submit_clicked)
        self.mainLayout.addWidget(self.buttonSubmit)

    def on_button_submit_clicked(self):
        name = self.inputName.text()
        hobby = self.comboHobby.currentText()
        self.nameUser.setText(f"nama kamu {name} dan hobi kamu {hobby}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
