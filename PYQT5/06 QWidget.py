import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle("QSplitter 例子")
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # 设置可拖动的布局为水平
        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        # 设置水平两个控件的宽
        splitter1.setSizes([300,300])

        # 设置可拖动的布局为垂直
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = Splitter()
    main.show()
    sys.exit(app.exec_())