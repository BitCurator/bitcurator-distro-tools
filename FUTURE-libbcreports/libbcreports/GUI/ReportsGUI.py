#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# BitCurator
#
# bcReportsTabv3.py
#
# Revised implementation of GUI interface in PyQT5 for generating files 
# and reports for Bitcurator project.
#
# Created: Sat Jul 16 19:17:21 2016
#

import os
import sys
import time
import logging
import threading

from PyQt5 import QtCore, QtWidgets

#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.Qt import *
#from PyQt5.QtWidgets import *

from os.path import expanduser
from subprocess import Popen,PIPE

from ReportsWindow import Ui_MainWindow


class ReportsGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ReportsGUI, self).__init__()
        self.ui=Ui_MainWindow()
        self.setupUi(self)        
        self.fname = None
        #self.show()

        # ALL CONTROL CODE GOES HERE, IN SUBSEQUENT FUNCTIONS, IN ADDITIONAL MODULES, OR MAIN!
        # *DO NOT* EDIT ReportsWindow,py! (USE ONLY QTCREATOR TO UPDATE IT)

class XStreamLogger(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        record = self.format(record)
        if record:
            XStream.stdout().write('%s\n' % record)

class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    messageWritten = QtCore.pyqtSignal(str)

    def flush(self):
        pass

    def fileno(self):
        return -1

    def write(self, msg):
        if (not self.signalsBlocked()):
            self.messageWritten.emit(unicode(msg))

    @staticmethod
    def stdout():
        if (not XStream._stdout):
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if (not XStream._stderr):
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr

# TBD: ReporterThread here


def main():
    app = QtWidgets.QApplication(sys.argv)

    # The ReportsGUI class performs UI setup
    form = ReportsGUI()

    # Connect reports generation loggin to text box
    # (MORE HERE)

    # Render and handle app
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()