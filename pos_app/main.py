from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(480, 320)
        label = QLabel("به اولین برنماه پای ساید 6 خوش آمدید")
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
