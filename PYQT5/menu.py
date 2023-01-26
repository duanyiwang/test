from PyQt5.Qt import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500, 400)
        self.setup_UI()

    def setup_UI(self):


print(__name__)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
