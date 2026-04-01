import sys
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


class MyApplicationFirst(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pelajaran 1: Dasar PyQt6")
        self.setMinimumSize(1200, 800)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplicationFirst()
    window.show()
    sys.exit(app.exec())
