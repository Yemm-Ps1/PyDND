from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit
from PyQt5 import QtCore
from ui.abstract_ui import AbstractUI


class MainWindow(QWidget):
    STANDARD_FONT = QFont("Consolas", 20)

    COLOR_BLACK = "#010b32"
    COLOR_WHITE = "#FFF"
    REGULAR_FONT_SIZE = 18

    def __init__(self):
        QWidget.__init__(self)
        self.showMaximized()
        self.main_layout: QVBoxLayout = QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setStyleSheet(f"""
            background-color: {self.COLOR_BLACK};
            color: {self.COLOR_WHITE};
        """)

        self.history_text: QLabel = QLabel()
        self.history_text.setFont(self.STANDARD_FONT)
        self.history_text.setText("This is some text.\nThis is some more.")
        self.history_text.setStyleSheet("line-spacing: 40px")
        self.input_text: QConsole = QConsole()

        self.input_text.returnPressed.connect(self.on_pressed)
        self.input_text.setFont(self.STANDARD_FONT)
        self.input_text.setStyleSheet("qproperty-frame: false; padding-top:-7px; padding-left:-2px")
        # self.input_text.setStyleSheet("qproperty-frame: false; padding:0px;")

        self.main_layout.addWidget(self.history_text)
        self.main_layout.addWidget(self.input_text)

        self.setLayout(self.main_layout)

    def on_pressed(self):
        self.history_text.setText(self.history_text.text() + "\n" + self.input_text.text())
        self.input_text.clear()


class QConsole(QLineEdit):
    WIDTH = 480
    HEIGHT = 320

    def __init__(self):
        QLineEdit.__init__(self)


'''
UI which can be used locally.
'''


class LocalUI(AbstractUI):
    def __init__(self):
        pass

    def submit_main_terminal_message(self, message):
        pass

    def submit_main_terminal_error_message(self, message):
        pass

    def invalidate_health_display(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
