# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_welcome.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QLocale, QMetaObject, QCoreApplication, QRect
from PySide2.QtGui import Qt, QFont, QIcon
from PySide2.QtWidgets import QSizePolicy, QSpacerItem, QGridLayout, QPushButton, QMainWindow, QAction, \
        QWidget, QVBoxLayout, QFrame, QMenuBar, QMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(384, 384)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(384, 384))
        MainWindow.setMaximumSize(QSize(384, 384))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/python.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"\n"
"QMenu\n"
"{\n"
"color: red;\n"
"}\n"
"\n"
"")
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(9)
        self.action_3.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(10)
        self.centralwidget.setFont(font2)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 9, 0)
        self.centralwidget_line = QFrame(self.centralwidget)
        self.centralwidget_line.setObjectName(u"centralwidget_line")
        self.centralwidget_line.setFrameShape(QFrame.HLine)
        self.centralwidget_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.centralwidget_line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.horizontalSpacer = QSpacerItem(42, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(300, 20))
        self.pushButton.setMaximumSize(QSize(384, 30))
        self.pushButton.setFont(font2)

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(300, 20))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f (\u0441\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432)")

        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(300, 20))
        self.pushButton_4.setMaximumSize(QSize(384, 30))
        self.pushButton_4.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(300, 20))
        self.pushButton_3.setMaximumSize(QSize(384, 30))
        self.pushButton_3.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(300, 20))
        self.pushButton_2.setMaximumSize(QSize(384, 30))
        self.pushButton_2.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(42, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.centralwidget_line_2 = QFrame(self.centralwidget)
        self.centralwidget_line_2.setObjectName(u"centralwidget_line_2")
        self.centralwidget_line_2.setFrameShadow(QFrame.Sunken)
        self.centralwidget_line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.centralwidget_line_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QRect(0, 0, 384, 21))
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setLayoutDirection(Qt.RightToLeft)
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0441\u0435\u0440\u0432\u0438\u0441 \u0422\u0423\u0421\u0423\u0420", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u044c \u0441 \u0430\u0432\u0442\u043e\u0440\u043e\u043c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0435\n"
" \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f (\u0441\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

