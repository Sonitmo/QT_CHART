import sys

import PySide6
from PySide6.QtCore import QRect, QPoint, QPointF, Qt, QRectF, QSize, QEasingCurve, QPropertyAnimation, Property
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import QCheckBox, QApplication, QMainWindow, QVBoxLayout, QWidget


class SwitchButton(QCheckBox):
    def __init__(self, parent=None,
                 width=100,
                 bg_color='gray',
                 circle_color='red',
                 active_color='#a2fc05',
                 animation_curve=QEasingCurve.OutBounce
                 ):
        super().__init__(parent)

        # Set default parameters
        self.setFixedSize(width, 28)
        self.setCursor(Qt.PointingHandCursor)  # khi trỏ vào checkbox sẽ hiện con trỏ bàn tay

        # Color
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.active_color = active_color


    def paintEvent(self, e) -> None:
        # Set painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw circle
        if self.isChecked():
            # print('check')
            painter.setBrush(QColor(self.active_color))
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)
            painter.setBrush(QColor(self.circle_color))
            painter.drawEllipse(73, 1, 26, 26)
        else:
            # print('uncheck')
            painter.setBrush(QColor(self.bg_color))
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)
            painter.setBrush(QColor(self.circle_color))
            painter.drawEllipse(1, 1, 26, 26)

        painter.end()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.toggle = SwitchButton()
#         layout = QVBoxLayout()
#
#         layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
