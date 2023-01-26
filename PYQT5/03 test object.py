from PyQt5.Qt import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Object的测试")
        self.resize(500, 400)
        # self.setup_UI()
        self.setup_UI3()

    def setup_UI(self):
        # 测试API
        # obj = QObject()
        # obj.setObjectName("lai")
        # print(obj.objectName())
        #
        # obj.setProperty("lai1", 'error')
        # obj.setProperty('lai2', 'warning')
        # print(obj)
        #
        # print(obj.property('lai2'))
        # print(obj.dynamicPropertyNames())

        with open('css.qss', mode='r') as fin:
            qApp.setStyleSheet(fin.read())

        label = QLabel(self)
        label.setObjectName('1')
        label.setProperty('A', 'error')
        label.setText("妹妹哦，来打屁股咯")
        # label.setStyleSheet('font-size:100px;color:red')

        label2 = QLabel(self)
        label2.setObjectName('1')
        label2.setProperty('A', 'warning')
        label2.setText('no no no')
        label2.move(100, 100)

        label3 = QLabel(self)
        label3.setObjectName('1')
        label3.setProperty('A', 'out')
        label3.setText('XXXX')
        label3.move(200, 200)

        label4 = QLabel(self)
        label4.setObjectName('1')

        label4.setText('BBB')
        label4.move(100, 200)

    def setup_UI2(self):
        obj1 = QObject()
        obj2 = QObject()

        print(obj1)

        print(obj2)
        obj1.setParent(obj2)
        print(obj1.parent())

    def setup_UI3(self):
        with open('css.qss', mode='r') as fin:
            qApp.setStyleSheet(fin.read())

        txt = QLabel(self)
        txt.setText("去点击吧")
        txt.move(100, 100)
        txt.resize(500, 100)
        txt.setObjectName('1')

        def jingxi():
            print('中奖2000万')
            txt.setText('中奖2000万')
            but.deleteLater()

        but = QPushButton(self)
        but.setText('点我有惊喜')
        but.clicked.connect(jingxi)

        txt2 = QLabel(self)
        txt2.setText('恭喜中奖')
        txt2.move(0, 100)

        obj = QObject()
        obj.setObjectName('111')

        # for wi in self.findChildren(QLabel):
        #     print(wi)

        for o in self.children():
            print(o.isWidgetType())

    def test1(self):
        obj1 = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        OBJS = [obj1, w, btn, label]

        for o in OBJS:
            # print(o.isWidgetType())
            # print(o.inherits('QWidget'))
            print(o.inherits('QPushButton'))

    def test2(self):
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda: print('obj1被释放了'))
        obj2.destroyed.connect(lambda: print('obj2被释放了'))
        obj3.destroyed.connect(lambda: print('obj3被释放了'))


# print(__name__)
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = window()
    window.show()
    # win1 = QWidget()
    # win1.setWindowTitle("1")
    # win1.setStyleSheet("background-color:green")
    # win1.show()
    #
    # win2 = QWidget()
    # win2.setWindowTitle("2")
    # win2.move(300, 300)
    # win2.setParent(win1)
    # win2.resize(1000, 1000)
    # win2.setStyleSheet("background-color:yellow")
    # win2.show()
    #
    #
    #
    # win3 = QWidget()
    # win3.setWindowTitle("2")
    # win3.move(10, 10)
    # win3.setParent(win1)
    # win3.resize(10, 10)
    # win3.setStyleSheet("background-color:red")
    # win3.show()

    sys.exit(app.exec_())
