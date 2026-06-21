from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit
)


class TonyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tony")

        self.setFixedSize(420, 520)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setWindowOpacity(0.95)

        self.setStyleSheet("""
            background-color: transparent;
        """)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 400, 350)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bottom-right position
        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.width() - 450
        y = screen.height() - 500

        self.move(x, y)
 
        self.drag_position = None
        self.input_box = QLineEdit(self)

        self.input_box.setGeometry(
            20,
            390,
            280,
            40
        )

        self.input_box.setPlaceholderText(
            "Talk to Tony..."
        )
        self.send_button = QPushButton(
            "Send",
            self
        )

        self.send_button.setGeometry(
            310,
            390,
            90,
            40
        )
        self.input_box.returnPressed.connect(
            self.send_message
        )

        self.send_button.clicked.connect(
            self.send_message
        )
        self.input_box.setStyleSheet("""
            background-color: white;
            color: black;
            border-radius: 10px;
            padding: 5px;
        """)
        self.input_box.setText("Start")
        self.send_button.setStyleSheet("""
            background-color: #6A5ACD;
            color: white;
            border-radius: 10px;
        """)
        self.user_text = ""
        self.show()
    def send_message(self):

        self.user_text = (
            self.input_box.text()
        )

        self.input_box.clear()

    def set_image(self, image_name):

        image_path = os.path.join(
            "assets",
            image_name
        )

        if os.path.exists(image_path):

            pixmap = QPixmap(image_path)

            pixmap = pixmap.scaled(
                400,
                400,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            self.image_label.setPixmap(pixmap)

        else:
            print(f"Image not found: {image_path}")
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(
                event.globalPosition().toPoint() - self.drag_position
            )
            event.accept()
def get_text_input():

    text = window.user_text

    window.user_text = ""

    return text

# Create application
app = QApplication(sys.argv)

# Create Tony window
window = TonyWindow()


def update_status(image_name):
    """
    Example:
    update_status("listening.png")
    update_status("thinking.png")
    update_status("speaking.png")
    """
    window.set_image(image_name)
    app.processEvents()