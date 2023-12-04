#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import multiprocessing
import os
import sys


os.environ["QT_MAC_WANTS_LAYER"] = "1"  # https://stackoverflow.com/a/66204842/1166461


from PySide2 import QtWidgets, QtGui


if __name__ == '__main__':
    multiprocessing.freeze_support()

    app = QtWidgets.QApplication(sys.argv)

    app.processEvents()
    window = QtWidgets.QDialog()
    window.resize(1344, 800)
    window_rect = window.frameGeometry()
    center_point = QtWidgets.QDesktopWidget().availableGeometry(window).center()
    window_rect.moveCenter(center_point)
    window.move(window_rect.topLeft())
    window.show()

    exit_code = app.exec_()
