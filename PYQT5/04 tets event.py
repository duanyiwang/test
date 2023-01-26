import sys
from PyQt5.Qt import *


class APP(QApplication):
    def notify(self, recevier, Event):
        # print(recevier, Event)

        # if recevier.inherits('QPushButton') and Event.type() == QEvent.MouseButtonPress:
        #     print(recevier, Event)

        # if :#recevier.inherits('QPushButton') and Event == QEvent.MouseButtonPress
        #     print(recevier, Event)
        return super().notify(recevier, Event)


class btn(QPushButton):
    def event(self, Event):
        # print(Event)

        return super().event(Event)

    def mousePressEvent(self, Event):
        print('dianji')

        return super().mousePressEvent(Event)


app = APP(sys.argv)

window = QWidget()
window.resize(300, 300)


def cao():
    print('按钮被点击了')


btn = btn(window)
btn.setText('按钮')
btn.move(100, 100)
btn.resize(100, 100)
btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())
