import re
import threading
import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QBoxLayout, QScrollArea
from qtpy import QtGui, QtCore

from res.R import RegistryId
# from controller.command_mediator import CommandMediator
from res.resource_loader import get_style_sheet, get_resource
from ui.abstract_ui import AbstractUI

CONSOLE_CHARACTER_PATTERN = re.compile("[\d\w()+\-*/\s]")
ERROR_TEXT_HEX = get_resource(RegistryId.ColorError)
ERROR_TEXT_FORMAT = '<font color="{error_hex}">{text}</font>'


class CustomLayoutScheme:
    HORIZONTAL = 0
    VERTICAL = 1


class LocalUI(QWidget, AbstractUI):
    def __init__(self):
        QWidget.__init__(self)
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

        self.terminal_widget: TerminalWidget = TerminalWidget(self, self.terminal_scroll)
        self.terminal_scroll.setWidget(self.terminal_widget)

        self.main_layout.addWidget(self.terminal_scroll)

        self.sidebar_widget = SidebarWidget()
        self.main_layout.addWidget(self.sidebar_widget)
        self.terminal_widget.focus_on()

        # self.command_mediator: CommandMediator = CommandMediator(self)

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

    def submit_main_terminal_message(self, message):
        self.terminal_widget.append_line_to_terminal(message)

    def submit_main_terminal_error_message(self, message):
        # self.terminal_widget.append_line_to_terminal(ERROR_TEXT_FORMAT.format(error_hex="red", text=message))
        self.terminal_widget.append_line_to_terminal(message)

    def invalidate_health_display(self):
        print("Health display invalidated.")

    def on_user_input_entered(self, user_input: str):
        # self.command_mediator.process_command(user_input)
        pass

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
    def __init__(self, parent_ui: LocalUI, scroll_container: QScrollArea = None):
        QWidget.__init__(self)
        self.parent_ui: LocalUI = parent_ui
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
        sample_text = """
            <p><span>&gt; Players</span></p>
<p style="margin-left:30px"><span style="color:#1E81B0">Jamuel </span><span style="color:#FF0000">Sven </span><span style="color:#00cc00">Varys </span><span style="color:#FFFF00">Woodrow </span><span style="color:#ff9900">Whiskers</span></p>
<p>&gt; !ra <span style="color:#FFFF00">1d20</span> + 5</p>
<p style="margin-left:30px"><span>Rolled: 20</span></p>
<p style="margin-left:30px"><span>Rolled: 20</span></p>
<p style="margin-left:30px"><span>Result: 20</span></p>
<p><span>&gt; !r 2d15 + 5</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Result: 30</span></p>
<p><span>&gt; Hit Arnac 30</span></p>
<p style="margin-left:30px"><span>Arnac has taken 742 damage.</span></p>
<p><span>&gt; !rd 1d20</span></p>
<p style="margin-left:30px"><span>Rolled: 20</span></p>
<p style="margin-left:30px"><span>Rolled: 20</span></p>
<p style="margin-left:30px"><span>Result: 20</span></p>
<p><span>&gt; !r 4d15 + 5</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Rolled: 15</span></p>
<p style="margin-left:30px"><span>Result: 60</span></p>
<p><span>&gt; Hit Whiskers 60</span></p>
<p style="margin-left:30px"><span>Whiskers is at 0 health.</span></p>
<p style="margin-left:30px"><span>Whiskers is dead.</span></p>
        """
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
        self.input_text.returnPressed.connect(self.on_text_entered)
        self.input_text.setContentsMargins(0, 0, 0, 0)

        self.input_row_layout.addWidget(self.input_text)

        self.terminal_layout.addWidget(self.input_row_holder)

        self.input_text.setFocus()

    def on_text_entered(self):
        user_input = self.input_text.text()
        self.input_text.clear()
        self.append_line_to_terminal(f"{self.lead_input_str} {user_input}")
        self.parent_ui.on_user_input_entered(user_input)
        threading.Thread(target=self.scroll_to_bottom).start()

    def append_line_to_terminal(self, to_append: str):
        self.history_text.setText(self.history_text.text() + "\n" + to_append)

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
        self.health_text.setText(
            f"{health_lbl}:\n\nCharacter #1: 100 / 120\nCharacter #2: 50 / 70\nCharacter #3: 0 / 150")

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


def test_func(ui: LocalUI, delay, message):
    time.sleep(delay)
    print(message)
    ui.submit_main_terminal_message(message)


if __name__ == '__main__':
    app = QApplication([])
    ui = LocalUI()

    ui.showMaximized()
    # threading = threading.Thread(target=partial(test_func, ui, 3, "Something")).start()
    # threading = threading.Thread(target=partial(test_func, ui, 3, "Something Else")).start()
    app.exec()
