import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QApplication
from pathlib import Path
from modules import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1100, 600)

        self.ui.btn_exit.clicked.connect(self.quit_system)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_restore_down.clicked.connect(self.fullscreen_application)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.btn_chart1.clicked.connect(self.switch_to_page1)
        self.ui.btn_chart2.clicked.connect(self.switch_to_page2)
        self.ui.btn_chart3.clicked.connect(self.switch_to_page3)
        self.ui.btn_menu.clicked.connect(self.change_size_left_frame)

        self.ui.check_box.stateChanged.connect(self.change_mode)

        # Trạng thái ban đầu của screen là False
        self.is_fullscreen = False


        ##################
        self.trans = QtCore.QTranslator(self)
        self.ui.combo_box.currentIndexChanged.connect(self.change_func)
        options = ([('English', ''), ('Vietnamese', 'eng-vi'), ])

        for i, (text, lang) in enumerate(options):
            self.ui.combo_box.addItem(text)
            self.ui.combo_box.setItemData(i, lang)
        self.ui.retranslateUi(self)

    @Slot(int)
    def change_func(self, index):
        data = self.ui.combo_box.itemData(index)
        print('index:', index)
        if data:
            self.trans.load(f'./locate/{data}.qm')
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)

    def change_mode(self, state):
        if self.ui.check_box.isChecked():
            app.setStyleSheet(Path('themes/dark.qss').read_text())
        else:
            app.setStyleSheet(Path('themes/light.qss').read_text())

    def switch_to_page1(self):
        print('page 1')
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def switch_to_page2(self):
        print('page 2')
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def switch_to_page3(self):
        print('page 3')
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)



    def quit_system(self):
        sys.exit()

    def fullscreen_application(self):
        if not self.is_fullscreen:
            self.showFullScreen()
            self.is_fullscreen = True
        else:
            self.showNormal()
            self.is_fullscreen = False

    def change_size_left_frame(self):
        self.ui.frm_left.resize(0, self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('themes/light.qss').read_text())
    win = MainWindow()
    win.show()
    app.exec()

'''
lệnh để chuyển đổi reaources.qrc thành class python có the sử dụng trong chương trình
pyside6-rcc resources.qrc -o resources_rc.py

'''