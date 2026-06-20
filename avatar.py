from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import os


class TonyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tony")

        self.setFixedSize(420, 420)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setWindowOpacity(0.95)

        self.setStyleSheet("""
            background-color: transparent;
        """)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 420, 420)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bottom-right position
        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.width() - 450
        y = screen.height() - 500

        self.move(x, y)

        self.show()
        self.drag_position = None

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