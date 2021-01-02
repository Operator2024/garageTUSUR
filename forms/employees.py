# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employees.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QLocale, QMetaObject, QCoreApplication, QDate
from PySide2.QtGui import Qt, QFont, QIcon
from PySide2.QtWidgets import QSizePolicy, QSpacerItem, QLabel, QGridLayout, QPushButton, QComboBox, QDateEdit, QFormLayout, QLineEdit, QTabWidget, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(580, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(580, 400))
        Form.setMaximumSize(QSize(580, 400))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/python.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(560, 380))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.tab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(150, 30))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)
        self.dateEdit.setDate(QDate(2020, 10, 1))

        self.gridLayout_2.addWidget(self.dateEdit, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(150, 30))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_2)


        self.gridLayout_3.addLayout(self.formLayout, 1, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(150, 30))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lineEdit_3)


        self.gridLayout_3.addLayout(self.formLayout_2, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(15, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(310, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_9 = QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.tab_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(150, 30))
        self.dateEdit_2.setReadOnly(True)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setTimeSpec(Qt.LocalTime)
        self.dateEdit_2.setDate(QDate(2020, 10, 1))

        self.gridLayout_8.addWidget(self.dateEdit_2, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 3, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(150, 30))
        self.lineEdit_6.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.lineEdit_6)


        self.gridLayout_6.addLayout(self.formLayout_4, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(150, 30))
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_7.addWidget(self.lineEdit_4, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(150, 30))
        self.lineEdit_5.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lineEdit_5)


        self.gridLayout_6.addLayout(self.formLayout_3, 1, 1, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(150, 30))
        self.lineEdit_7.setReadOnly(True)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lineEdit_7)


        self.gridLayout_6.addLayout(self.formLayout_6, 1, 3, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_6, 4, 0, 1, 2)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.gridLayout_9.addLayout(self.formLayout_5, 0, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_10, 2, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0415\u0441\u043b\u0438 \u0443 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430 \u043d\u0435\u0442 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u0430, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u044b\u043c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e (\u0435\u0441\u043b\u0438 \u0438\u043c\u0435\u0435\u0442\u0441\u044f)", None))
        self.lineEdit_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 \u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e (\u0435\u0441\u043b\u0438 \u0438\u043c\u0435\u0435\u0442\u0441\u044f)", None))
        self.lineEdit_6.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_4.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.lineEdit_5.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0432 \u0431\u0430\u0437\u0435", None))
        self.lineEdit_7.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0415\u0441\u043b\u0438 \u0443 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430 \u043d\u0435\u0442 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u0430, \u0432 \u043f\u043e\u043b\u0435 \u0431\u0443\u0434\u0435\u0442 \u0441\u0438\u043c\u0432\u043e\u043b -", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430\u0445", None))
    # retranslateUi

