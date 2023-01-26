# 导入需要的包和模块
from PyQt5.Qt import *
import sys
from menu import window



# 创建一个应用程序对象
app = QApplication(sys.argv)
# 控件的操作
# 创建控件
window = window()
# 设置控件
# window.setWindowTitle("")
# window.resize(500, 400)


# 展示控件
window.show()
# 应用程序执行，进入消息循环
sys.exit(app.exec_())
