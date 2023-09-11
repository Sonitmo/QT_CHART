# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacebFgWpX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

from .switchbutton import SwitchButton
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stylesheet = QFrame(self.centralwidget)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"")
        self.stylesheet.setFrameShape(QFrame.StyledPanel)
        self.stylesheet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.stylesheet)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bg_app = QFrame(self.stylesheet)
        self.bg_app.setObjectName(u"bg_app")
        self.bg_app.setFrameShape(QFrame.StyledPanel)
        self.bg_app.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bg_app)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frm_left = QFrame(self.bg_app)
        self.frm_left.setObjectName(u"frm_left")
        self.frm_left.setStyleSheet(u"frm_left")
        self.frm_left.setFrameShape(QFrame.StyledPanel)
        self.frm_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_left)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frm_lelf_top = QFrame(self.frm_left)
        self.frm_lelf_top.setObjectName(u"frm_lelf_top")
        self.frm_lelf_top.setMinimumSize(QSize(0, 50))
        self.frm_lelf_top.setMaximumSize(QSize(16777215, 50))
        self.frm_lelf_top.setFrameShape(QFrame.StyledPanel)
        self.frm_lelf_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_lelf_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frm_lelf_top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frm_lelf_top)

        self.frame_8 = QFrame(self.frm_left)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_chart1 = QPushButton(self.frame_8)
        self.btn_chart1.setObjectName(u"btn_chart1")
        self.btn_chart1.setMinimumSize(QSize(40, 40))
        self.btn_chart1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/address-book-blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chart1.setIcon(icon)

        self.verticalLayout_6.addWidget(self.btn_chart1)

        self.btn_chart2 = QPushButton(self.frame_8)
        self.btn_chart2.setObjectName(u"btn_chart2")
        self.btn_chart2.setMinimumSize(QSize(40, 40))
        self.btn_chart2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/android.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chart2.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.btn_chart2)

        self.btn_chart3 = QPushButton(self.frame_8)
        self.btn_chart3.setObjectName(u"btn_chart3")
        self.btn_chart3.setMinimumSize(QSize(40, 40))
        self.btn_chart3.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/animal-dog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chart3.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.btn_chart3)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/animal-monkey.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/icons/animal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.pushButton_7)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frm_left)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(16777215, 80))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_12, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.check_box = SwitchButton(self.frame_9)
        self.check_box.setObjectName(u"check_box")
        self.check_box.setMinimumSize(QSize(0, 0))
        self.check_box.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.check_box)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frm_left)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout_10.addWidget(self.frm_left)

        self.frm_right = QFrame(self.bg_app)
        self.frm_right.setObjectName(u"frm_right")
        self.frm_right.setStyleSheet(u"")
        self.frm_right.setFrameShape(QFrame.StyledPanel)
        self.frm_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frm_right)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frm_right_top = QFrame(self.frm_right)
        self.frm_right_top.setObjectName(u"frm_right_top")
        self.frm_right_top.setStyleSheet(u"")
        self.frm_right_top.setFrameShape(QFrame.StyledPanel)
        self.frm_right_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_right_top)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frm_right_top)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_menu = QPushButton(self.frame_13)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/icons/menu-burger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.btn_menu)

        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.frame_13)

        self.label_10 = QLabel(self.frm_right_top)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.frame_14 = QFrame(self.frm_right_top)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.combo_box = QComboBox(self.frame_14)
        self.combo_box.setObjectName(u"combo_box")

        self.horizontalLayout_7.addWidget(self.combo_box)

        self.btn_minimize = QPushButton(self.frame_14)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setStyleSheet(u"color: #FFFFFF;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/resources/icons/icons8-minimize-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.btn_minimize)

        self.btn_restore_down = QPushButton(self.frame_14)
        self.btn_restore_down.setObjectName(u"btn_restore_down")
        icon7 = QIcon()
        icon7.addFile(u":/icons/resources/icons/icons8-restore-down-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restore_down.setIcon(icon7)

        self.horizontalLayout_7.addWidget(self.btn_restore_down)

        self.btn_exit = QPushButton(self.frame_14)
        self.btn_exit.setObjectName(u"btn_exit")
        icon8 = QIcon()
        icon8.addFile(u":/icons/resources/icons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon8)

        self.horizontalLayout_7.addWidget(self.btn_exit)


        self.horizontalLayout_4.addWidget(self.frame_14)


        self.verticalLayout_9.addWidget(self.frm_right_top)

        self.frm_right_main = QFrame(self.frm_right)
        self.frm_right_main.setObjectName(u"frm_right_main")
        self.frm_right_main.setFrameShape(QFrame.StyledPanel)
        self.frm_right_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frm_right_main)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frm_right_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_11 = QVBoxLayout(self.page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_16 = QFrame(self.page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.frm_page1 = QFrame(self.page)
        self.frm_page1.setObjectName(u"frm_page1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_page1.sizePolicy().hasHeightForWidth())
        self.frm_page1.setSizePolicy(sizePolicy)
        self.frm_page1.setStyleSheet(u"")
        self.frm_page1.setFrameShape(QFrame.StyledPanel)
        self.frm_page1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frm_page1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_18 = QFrame(self.page_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_18)

        self.frm_page2 = QFrame(self.page_2)
        self.frm_page2.setObjectName(u"frm_page2")
        sizePolicy.setHeightForWidth(self.frm_page2.sizePolicy().hasHeightForWidth())
        self.frm_page2.setSizePolicy(sizePolicy)
        self.frm_page2.setStyleSheet(u"")
        self.frm_page2.setFrameShape(QFrame.StyledPanel)
        self.frm_page2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frm_page2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_15 = QVBoxLayout(self.page_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_20 = QFrame(self.page_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.label_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.frm_page3 = QFrame(self.page_3)
        self.frm_page3.setObjectName(u"frm_page3")
        sizePolicy.setHeightForWidth(self.frm_page3.sizePolicy().hasHeightForWidth())
        self.frm_page3.setSizePolicy(sizePolicy)
        self.frm_page3.setStyleSheet(u"")
        self.frm_page3.setFrameShape(QFrame.StyledPanel)
        self.frm_page3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frm_page3)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_10.addWidget(self.stackedWidget)


        self.verticalLayout_9.addWidget(self.frm_right_main)

        self.frm_right_bottom = QFrame(self.frm_right)
        self.frm_right_bottom.setObjectName(u"frm_right_bottom")
        self.frm_right_bottom.setFrameShape(QFrame.StyledPanel)
        self.frm_right_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frm_right_bottom)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frm_right_bottom)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"color: #FFFFFF;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_16 = QLabel(self.frame_23)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_17.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.frame_23)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frm_right_bottom)


        self.horizontalLayout_10.addWidget(self.frm_right)


        self.horizontalLayout_9.addWidget(self.bg_app)


        self.horizontalLayout.addWidget(self.stylesheet)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QT CHART", None))
        self.btn_chart1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.btn_chart2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_chart3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Page 5", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Set Mode", None))
        self.check_box.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"NGUYEN NGOC SON", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"sonitmo@gmail.com", None))
        self.btn_menu.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.btn_minimize.setText("")
        self.btn_restore_down.setText("")
        self.btn_exit.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Copyright N.N.S", None))
    # retranslateUi

