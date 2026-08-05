from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QFormLayout
import sys
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(480, 320)
        form = QFormLayout()
        self.username = QLineEdit()
        self.username.setPlaceholderText("نام کاربری")
        form.addRow("نام کاربری", self.username)
        self.password = QLineEdit()
        self.password.setPlaceholderText("کلمه عبور")
        form.addRow("کلمه عبور", self.password)
        button = QPushButton("ورود")
        form.addRow(button)
        button.clicked.connect(self.on_click)
        widget = QWidget()
        widget.setLayout(form)
        self.setCentralWidget(widget)

    def on_click(self):
        username = self.username.text()
        password = self.password.text()
        print(f"hello {username} {password}")


app = QApplication(sys.argv)
app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
window = MainWindow()
window.show()
sys.exit(app.exec())
