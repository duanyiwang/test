import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('NB-PLUS')

        self.resize(900, 600)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.show()
        # cp= QDesktopWidget.availableGeometry().center()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
