from PyQt5.QtWidgets import QWidget

from pyqtspinner import WaitingSpinner


def test_spinner_creation(qtbot):
    parent = QWidget()
    spinner = WaitingSpinner(parent)

    spinner.start()
    spinner.stop()
