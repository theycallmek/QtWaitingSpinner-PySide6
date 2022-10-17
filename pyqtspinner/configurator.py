import math
import sys
from random import random

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (
    QApplication,
    QColorDialog,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QWidget,
)

from .spinner import WaitingSpinner


# pylint: disable=too-many-instance-attributes,too-many-statements
class SpinnerConfigurator(QWidget):
    sb_roundness = None
    sb_opacity = None
    sb_fadeperc = None
    sb_lines = None
    sb_line_length = None
    sb_line_width = None
    sb_inner_radius = None
    sb_rev_s = None

    btn_start = None
    btn_stop = None
    btn_pick_color = None

    spinner = None

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize ui."""
        grid = QGridLayout()
        groupbox1 = QGroupBox()
        groupbox1_layout = QHBoxLayout()
        groupbox2 = QGroupBox()
        groupbox2_layout = QGridLayout()
        button_hbox = QHBoxLayout()
        self.setLayout(grid)
        self.setWindowTitle("QtWaitingSpinner Configurator")
        self.setWindowFlags(Qt.Dialog)

        # SPINNER
        self.spinner = WaitingSpinner(self)

        # Spinboxes
        self.sb_roundness = QDoubleSpinBox()
        self.sb_opacity = QDoubleSpinBox()
        self.sb_fadeperc = QDoubleSpinBox()
        self.sb_lines = QSpinBox()
        self.sb_line_length = QSpinBox()
        self.sb_line_width = QSpinBox()
        self.sb_inner_radius = QSpinBox()
        self.sb_rev_s = QDoubleSpinBox()

        # set spinbox default values
        self.sb_roundness.setValue(100)
        self.sb_roundness.setRange(0, 9999)
        self.sb_opacity.setValue(math.pi)
        self.sb_opacity.setRange(0, 9999)
        self.sb_fadeperc.setValue(80)
        self.sb_fadeperc.setRange(0, 9999)
        self.sb_lines.setValue(20)
        self.sb_lines.setRange(1, 9999)
        self.sb_line_length.setValue(10)
        self.sb_line_length.setRange(0, 9999)
        self.sb_line_width.setValue(2)
        self.sb_line_width.setRange(0, 9999)
        self.sb_inner_radius.setValue(10)
        self.sb_inner_radius.setRange(0, 9999)
        self.sb_rev_s.setValue(math.pi / 2)
        self.sb_rev_s.setRange(0.1, 9999)

        # Buttons
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")
        self.btn_pick_color = QPushButton("Pick Color")
        self.btn_randomize = QPushButton("Randomize")
        self.btn_show_init = QPushButton("Show init args")

        # Connects
        self.sb_roundness.valueChanged.connect(
            lambda x: setattr(self.spinner, "roundness", x)
        )
        self.sb_opacity.valueChanged.connect(
            lambda x: setattr(self.spinner, "minimum_trail_opacity", x)
        )
        self.sb_fadeperc.valueChanged.connect(
            lambda x: setattr(self.spinner, "trail_fade_percentage", x)
        )
        self.sb_lines.valueChanged.connect(
            lambda x: setattr(self.spinner, "number_of_lines", x)
        )
        self.sb_line_length.valueChanged.connect(
            lambda x: setattr(self.spinner, "line_length", x)
        )
        self.sb_line_width.valueChanged.connect(
            lambda x: setattr(self.spinner, "line_width", x)
        )
        self.sb_inner_radius.valueChanged.connect(
            lambda x: setattr(self.spinner, "inner_radius", x)
        )
        self.sb_rev_s.valueChanged.connect(
            lambda x: setattr(self.spinner, "revolutions_per_second", x)
        )

        self.btn_start.clicked.connect(self.spinner.start)
        self.btn_stop.clicked.connect(self.spinner.stop)
        self.btn_pick_color.clicked.connect(self.show_color_picker)
        self.btn_randomize.clicked.connect(self._randomize)
        self.btn_show_init.clicked.connect(self.show_init_args)

        # Layout adds
        groupbox1_layout.addWidget(self.spinner)
        groupbox1.setLayout(groupbox1_layout)

        groupbox2_layout.addWidget(QLabel("Roundness:"), *(1, 1))
        groupbox2_layout.addWidget(self.sb_roundness, *(1, 2))
        groupbox2_layout.addWidget(QLabel("Opacity:"), *(2, 1))
        groupbox2_layout.addWidget(self.sb_opacity, *(2, 2))
        groupbox2_layout.addWidget(QLabel("Fade Perc:"), *(3, 1))
        groupbox2_layout.addWidget(self.sb_fadeperc, *(3, 2))
        groupbox2_layout.addWidget(QLabel("Lines:"), *(4, 1))
        groupbox2_layout.addWidget(self.sb_lines, *(4, 2))
        groupbox2_layout.addWidget(QLabel("Line Length:"), *(5, 1))
        groupbox2_layout.addWidget(self.sb_line_length, *(5, 2))
        groupbox2_layout.addWidget(QLabel("Line Width:"), *(6, 1))
        groupbox2_layout.addWidget(self.sb_line_width, *(6, 2))
        groupbox2_layout.addWidget(QLabel("Inner Radius:"), *(7, 1))
        groupbox2_layout.addWidget(self.sb_inner_radius, *(7, 2))
        groupbox2_layout.addWidget(QLabel("Rev/s:"), *(8, 1))
        groupbox2_layout.addWidget(self.sb_rev_s, *(8, 2))

        groupbox2.setLayout(groupbox2_layout)

        button_hbox.addWidget(self.btn_start)
        button_hbox.addWidget(self.btn_stop)
        button_hbox.addWidget(self.btn_pick_color)
        button_hbox.addWidget(self.btn_randomize)
        button_hbox.addWidget(self.btn_show_init)

        grid.addWidget(groupbox1, *(1, 1))
        grid.addWidget(groupbox2, *(1, 2))
        grid.addLayout(button_hbox, *(2, 1))

        self.spinner.start()
        self.show()

    @pyqtSlot(name="randomize")
    def _randomize(self) -> None:
        self.sb_roundness.setValue(random() * 1000)
        self.sb_opacity.setValue(random() * 50)
        self.sb_fadeperc.setValue(random() * 100)
        self.sb_lines.setValue(math.floor(random() * 150))
        self.sb_line_length.setValue(math.floor(10 + random() * 20))
        self.sb_line_width.setValue(math.floor(random() * 30))
        self.sb_inner_radius.setValue(math.floor(random() * 30))
        self.sb_rev_s.setValue(random())

    @pyqtSlot(name="show_color_picker")
    def show_color_picker(self) -> None:
        """Set the color for the spinner."""
        assert self.spinner
        self.spinner.color = QColorDialog.getColor()

    @pyqtSlot(name="show_init_args")
    def show_init_args(self) -> None:
        """Display used arguments."""
        assert self.spinner
        text = (
            f"WaitingSpinner(\n    parent,\n    "
            f"roundness={self.spinner.roundness},\n    "
            f"opacity={self.spinner.minimum_trail_opacity},\n    "
            f"fade={self.spinner.trail_fade_percentage},\n    "
            f"radius={self.spinner.inner_radius},\n    "
            f"lines={self.spinner.number_of_lines},\n    "
            f"line_length={self.spinner.line_length},\n    "
            f"line_width={self.spinner.line_width},\n    "
            f"speed={self.spinner.revolutions_per_second},\n    "
            f"color={self.spinner.color.getRgb()[:3]}\n)\n"
        )
        msg_box = QMessageBox()
        msg_box.setText(text)
        msg_box.setWindowTitle("Text was copied to clipboard")
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(text, mode=clipboard.Clipboard)
        print(text)
        msg_box.exec_()


def main():
    app = QApplication(sys.argv)
    configurator = SpinnerConfigurator()  # noqa
    sys.exit(app.exec())
