from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys


class TonyWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Tony")

        self.setFixedSize(350, 150)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setWindowOpacity(0.9)

        # Dark theme
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                border-radius: 15px;
            }
        """)

        # Status label
        self.label = QLabel("⚫ Starting...", self)

        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.label.resize(350, 150)

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)

        self.label.setFont(font)

        # Move to bottom-right corner
        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.width() - 380
        y = screen.height() - 220

        self.move(x, y)

        self.show()

    def set_status(self, text):
        self.label.setText(text)


# Create application
app = QApplication(sys.argv)

# Create Tony window
window = TonyWindow()


def update_status(text):
    window.set_status(text)
    app.processEvents()