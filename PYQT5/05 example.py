from PyQt5.Qt import *


class myobject(QObject):
    def timerEvent(self, evt):
        print(evt, '1')


class mylabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('10')
        self.move(100, 200)
        self.setStyleSheet('font-size:100px')

        self.time_ID1 = self.startTimer(1000)
    def setsec(self,sec):
        self.setText(str(sec))

    def timerEvent(self, evt):
        c_t = int(self.text())

        c_t -= 1

        self.setText(str(c_t))
        if c_t == 0:
            self.killTimer(self.time_ID1)


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器的使用")
        self.resize(500, 400)
        self.setup_UI()

    def setup_UI(self):
        # btn = QPushButton(self)
        # btn.setText('点我')
        # btn.move(100, 100)
        label1 = mylabel(self)
        label1.setsec(20)


        obj = myobject(self)
        time_id = obj.startTimer(1000)
        # obj.killTimer(time_id)


# print(__name__)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
