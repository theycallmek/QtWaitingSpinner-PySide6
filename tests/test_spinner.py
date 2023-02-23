from PySide6.QtWidgets import QWidget

from pyqtspinner import WaitingSpinner
from pyqtspinner.configurator import SpinnerConfigurator


def test_spinner_creation(qtbot):
    parent = QWidget()
    spinner = WaitingSpinner(parent)

    spinner.start()
    spinner.stop()


def test_randomization_not_raising_value_errors(qtbot):
    configurator = SpinnerConfigurator()

    configurator._randomize()
