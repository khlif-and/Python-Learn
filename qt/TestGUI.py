import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def jalankan_tes():
    # 1. Aplikasi utama (Wajib ada di setiap aplikasi PyQt)
    app = QApplication(sys.argv) if hasattr(sys, "argv") else QApplication([])

    # 2. Membuat "Jendela" aplikasi (Window)
    jendela = QWidget()
    jendela.setWindowTitle("Uji Coba Pertama WSL GUI")
    jendela.setGeometry(100, 100, 400, 200) # (x, y, lebar, tinggi)

    # 3. Menambahkan Teks ke dalam jendela
    teks = QLabel("🎉 HORE! GUI dari WSL Berhasil Muncul! 🎉")
    teks.setStyleSheet("font-size: 16px; font-weight: bold; color: green;")

    # 4. Mengatur tata letak (Layout)
    layout = QVBoxLayout()
    layout.addWidget(teks)
    jendela.setLayout(layout)

    # 5. Tampilkan Jendela ke layar
    jendela.show()

    # 6. Jalankan "loop" aplikasi agar jendela tidak langsung menutup
    sys.exit(app.exec())

if __name__ == "__main__":
    jalankan_tes()
