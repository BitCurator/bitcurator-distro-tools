from PyQt5.QtCore import QThread
from libbcreports import Reporter


class ReportsWorker(QThread):

    def __init__(self, parent=None):

        QThread.__init__(self, parent)
        self.exiting = False

    def redact(self, Reporter):

        self.size = size
        self.stars = stars
        self.start()

    def run(self):
        Reporter.execute()

    def updateProgress(offset, total):
        self.emit(SIGNAL("progress(int, int)"), offset, total)

    def __del__(self):

        self.exiting = True
        self.wait()
