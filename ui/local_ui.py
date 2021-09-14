from enum import auto

import time
import threading


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QBoxLayout, QScrollArea, QHBoxLayout
from qtpy import QtGui, QtCore

from res.resource_loader import get_style_sheet, get_strings, get_resource
from res.R import RegistryId
from ui.abstract_ui import AbstractUI

import re

CONSOLE_CHARACTER_PATTERN = re.compile("[\d\w()+\-*/\s]")



class CustomLayoutScheme:
    HORIZONTAL = 0
    VERTICAL = 1


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # QApplication.desktop().screenGeometry
        screen_geo = QApplication.desktop().screenGeometry()

        self.resize(screen_geo.width() - 40, screen_geo.height() - 100)
        self.setWindowOpacity(float(get_resource(RegistryId.WindowOpacity)))
        self.setObjectName("window")
        self.setWindowTitle(get_resource(RegistryId.AppName))
        self.setStyleSheet(get_style_sheet())
        self.main_layout: QBoxLayout = QBoxLayout(QBoxLayout.Direction.LeftToRight, self)
        self.layout_scheme = CustomLayoutScheme.HORIZONTAL
        self.setLayout(self.main_layout)
        self.main_layout.setSpacing(0)

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

    def switch_layout_orientation(self):
        if self.layout_scheme is CustomLayoutScheme.VERTICAL:
            self.main_layout.setDirection(QBoxLayout.Direction.LeftToRight)
            self.layout_scheme = CustomLayoutScheme.HORIZONTAL
        elif self.layout_scheme is CustomLayoutScheme.HORIZONTAL:
            self.main_layout.setDirection(QBoxLayout.Direction.TopToBottom)
            self.layout_scheme = CustomLayoutScheme.VERTICAL

    def keyReleaseEvent(self, e: QtGui.QKeyEvent):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ControlModifier and e.key() == QtCore.Qt.Key.Key_R:
            self.sidebar_widget.switch_layout_orientation()
            self.switch_layout_orientation()
        as_str = e.text()
        if CONSOLE_CHARACTER_PATTERN.fullmatch(as_str):
            if not self.terminal_widget.is_focused():
                self.terminal_widget.append_to_input(as_str)
            self.terminal_widget.focus_on()
            self.terminal_scroll.verticalScrollBar().setValue(self.terminal_scroll.height())

    # def resizeEvent(self, e: QtGui.QResizeEvent):
    #     super().resizeEvent(e)
    #     # old_height = e.oldSize().height()
    #     new_width = e.size().width()
    #     # new_height = e.size().height()
    #     break_pt = int(get_resource(RegistryId.HorizontalBreakPoint))
    #     print(str(self.layout_type), new_width, break_pt)
    #     if new_width <= break_pt and self.layout_type is MainLayoutTypes.STANDARD:
    #         self.set_layout_orientation(MainLayoutTypes.VERTICAL)


class TerminalWidget(QWidget):
    def __init__(self, scroll_container: QScrollArea = None):
        QWidget.__init__(self)
        self.setObjectName("terminal")
        # self.input_lead = get_resource(R.id)
        self.lead_input_str: str = get_resource(RegistryId.LeadInputText)
        # Initiates scroll container
        self.scroll_container: QScrollArea = scroll_container

        self.scroll_container.verticalScrollBar().setVisible(False)
        # self.scroll_container.setFrameShape(QtFrame.)
        self.terminal_layout: QVBoxLayout = QVBoxLayout()
        self.terminal_layout.setAlignment(Qt.AlignTop)
        self.terminal_layout.setSpacing(0)
        self.setLayout(self.terminal_layout)

        # Initiates terminal log
        self.history_text: QLabel = QLabel()
        self.history_text.setObjectName("historyText")
        # TODO replace sample text
        sample_text = "> Players\n\tJamuel Sven Varys Woodrow Whiskers\n" \
                      "> !ra 1d20 + 5\n\tRolled: 20\n\tRolled: 20\n\tResult: 20\n> !r 2d15 + 5\n\tRolled: 15\n\tRolled: 15\n\tResult: 30\n> Hit Arnac 30\n\tArnac has taken 742 damage.\n" \
                      "> !rd 1d20\n\tRolled: 20\n\tRolled: 20\n\tResult: 20\n> !r 4d15 + 5\n\tRolled: 15\n\tRolled: 15\n\tRolled: 15\n\tRolled: 15\n\tResult: 60\n" \
                      "> Hit Whiskers 60\n\tWhiskers is at 0 health.\n\tWhiskers is dead."
        self.history_text.setText(sample_text)
        self.history_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.terminal_layout.addWidget(self.history_text)

        # Initiates terminal input row
        self.input_row_holder: QWidget = QWidget()
        # self.input_row_holder.setFixedHeight(self.history_text.fontMetrics().)
        self.input_row_holder.setObjectName("inputRow")
        self.input_row_holder.setContentsMargins(0, 0, 0, 0)
        self.input_row_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, self.input_row_holder)
        self.input_row_layout.setContentsMargins(0, 0, 0, 0)
        self.input_row_layout.setSpacing(0)
        self.input_row_holder.setLayout(self.input_row_layout)

        self.input_lead_icon = QLabel()
        self.input_lead_icon.setObjectName("inputLead")
        self.input_lead_icon.setText(self.lead_input_str + " ")
        self.input_row_layout.addWidget(self.input_lead_icon)
        self.input_text: QLineEdit = QLineEdit()
        self.input_text.setObjectName("userInputBox")
        self.input_text.setFrame(False)
        # self.input_text.setFixedHeight(self.input_lead_icon.fontMetrics().height())
        self.input_text.returnPressed.connect(self.on_pressed)
        self.input_text.setContentsMargins(0, 0, 0, 0)

        self.input_row_layout.addWidget(self.input_text)

        self.terminal_layout.addWidget(self.input_row_holder)


        self.input_text.setFocus()

    def on_pressed(self):
        self.history_text.setText(self.history_text.text() + f"\n{self.lead_input_str} " + self.input_text.text())
        # self.link_click_to_terminal(self.history_text)
        self.input_text.clear()
        threading.Thread(target=self.scroll_to_bottom).start()
        # self.scroll_to_bottom()
        # self.focus_on()

    def scroll_to_bottom(self):
        time.sleep(0.1)
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
        self.layout_scheme = CustomLayoutScheme.VERTICAL
        self.main_layout: QBoxLayout = QBoxLayout(QBoxLayout.Direction.TopToBottom, self)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setSpacing(40)

        self.health_text = QLabel()
        self.health_text.setObjectName("healthBox")
        self.health_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        health_lbl = get_resource(RegistryId.HealthLbl)
        self.health_text.setText(f"{health_lbl}:\n\nCharacter #1: 100 / 120\nCharacter #2: 50 / 70\nCharacter #3: 0 / 150")

        self.inventory_text = QLabel()
        self.inventory_text.setObjectName("inventoryBox")
        self.inventory_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.inventory_text.setText("Inventory:\n\nCharacter #1:\nCharacter #2:\nCharacter #3:")

        self.main_layout.addWidget(self.health_text)
        self.main_layout.addWidget(self.inventory_text)
        self.setLayout(self.main_layout)

    def switch_layout_orientation(self):
        if self.layout_scheme is CustomLayoutScheme.VERTICAL:
            self.main_layout.setDirection(QBoxLayout.Direction.LeftToRight)
            self.layout_scheme = CustomLayoutScheme.HORIZONTAL
        elif self.layout_scheme is CustomLayoutScheme.HORIZONTAL:
            self.main_layout.setDirection(QBoxLayout.Direction.TopToBottom)
            self.layout_scheme = CustomLayoutScheme.VERTICAL


'''
UI which can be used locally.
This is not the PyQt5 window itself but acts as a generic med
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

    window.showMaximized()
    app.exec()
