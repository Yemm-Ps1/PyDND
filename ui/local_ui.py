from enum import auto

import time
import threading


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QBoxLayout, QScrollArea
from qtpy import QtGui

from res.resource_loader import get_style_sheet, get_strings
from ui.abstract_ui import AbstractUI

import re

CONSOLE_CHARACTER_PATTERN = re.compile("[\d\w()+\-*/\s]")



class MainLayoutTypes:
    STANDARD = auto()
    HORIZONTAL = auto()


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setObjectName("window")
        self.setWindowTitle(get_strings()["app_name"])
        self.setStyleSheet(get_style_sheet())
        print("Stylesheet:", self.styleSheet())
        self.main_layout: QBoxLayout = None
        self.set_layout_orientation(MainLayoutTypes.STANDARD)

        self.terminal_scroll: QScrollArea = QScrollArea()
        self.terminal_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.terminal_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.terminal_scroll.setWidgetResizable(True)

        self.terminal_widget: TerminalWidget = TerminalWidget(self.terminal_scroll)
        self.terminal_scroll.setWidget(self.terminal_widget)

        self.main_layout.addWidget(self.terminal_scroll)

        self.sidebar_widget = SidebarWidget()
        self.main_layout.addWidget(self.sidebar_widget)
        self.terminal_widget.focus_on()

    def set_layout_orientation(self, layout_type: int):
        if layout_type is MainLayoutTypes.STANDARD:
            self.main_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, self)
            self.setLayout(self.main_layout)

    def keyReleaseEvent(self, e: QtGui.QKeyEvent):
        as_str = e.text()
        print(as_str)
        if CONSOLE_CHARACTER_PATTERN.fullmatch(as_str):
            if not self.terminal_widget.is_focused():
                self.terminal_widget.append_to_input(as_str)
            self.terminal_widget.focus_on()
            self.terminal_scroll.verticalScrollBar().setValue(self.terminal_scroll.height())


class TerminalWidget(QWidget):
    def __init__(self, scroll_container: QScrollArea = None):
        QWidget.__init__(self)
        self.setObjectName("terminal")
        self.scroll_container: QScrollArea = scroll_container

        self.scroll_container.verticalScrollBar().setVisible(False)
        # self.scroll_container.setFrameShape(QtFrame.)
        self.terminal_layout: QVBoxLayout = QVBoxLayout()
        self.terminal_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.terminal_layout)

        self.history_text: QLabel = QLabel()
        self.history_text.setText((40 * "Wow\n") + "Wow")
        self.history_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.terminal_layout.addWidget(self.history_text)
        self.input_text: QLineEdit = QLineEdit()
        self.input_text.returnPressed.connect(self.on_pressed)
        self.terminal_layout.addWidget(self.input_text)
        self.input_text.setFocus()

    def on_pressed(self):
        self.history_text.setText(self.history_text.text() + "\n" + self.input_text.text())
        # self.link_click_to_terminal(self.history_text)
        self.input_text.clear()
        print("Pressed")
        threading.Thread(target=self.scroll_to_bottom).start()
        # self.scroll_to_bottom()
        # self.focus_on()

    def scroll_to_bottom(self):
        time.sleep(0.05)
        if self.scroll_container:
            self.scroll_container.verticalScrollBar().setValue(100000)
            v_bar = self.scroll_container.verticalScrollBar()
            v_bar.setValue(v_bar.maximum())
            self.focus_on()

    def focus_on(self):
        self.input_text.setFocus()

    def is_focused(self):
        return self.input_text.hasFocus()

    def append_to_input(self, s: str):
        self.input_text.insert(s)


class SidebarWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(40)

        self.health_text = QLabel()
        self.health_text.setObjectName("healthBox")
        self.health_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.health_text.setText("Health:\n\nCharacter #1: 100 / 120\nCharacter #2: 50 / 70\nCharacter #3: 0 / 150")

        self.inventory_text = QLabel()
        self.inventory_text.setObjectName("inventoryBox")
        self.inventory_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.inventory_text.setText("Inventory:\n\nCharacter #1:\nCharacter #2:\nCharacter #3:")

        layout.addWidget(self.health_text)
        layout.addWidget(self.inventory_text)
        self.setLayout(layout)


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

    # window = TerminalWidget()
    # window = SidebarWidget()
    window.showMaximized()
    app.exec()
