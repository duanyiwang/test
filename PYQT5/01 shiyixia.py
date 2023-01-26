# 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 创建一个应用程序对象
app = QApplication(sys.argv)
# 控件的操作
# 创建控件
window = QWidget()
# 设置控件
window.setWindowTitle("AAA")
window.resize(500, 400)

lab = QLabel(window)
lab.setText("aaa")
lab.move(200, 100)

# 展示控件
window.show()
# 应用程序执行，进入消息循环
sys.exit(app.exec_())
