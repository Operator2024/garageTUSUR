# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spravka.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QLocale, QMetaObject, QCoreApplication
from PySide2.QtGui import Qt, QFont, QIcon
from PySide2.QtWidgets import QGridLayout, QPushButton, QTextEdit, QTabWidget, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(538, 596)
        Form.setMinimumSize(QSize(538, 596))
        Form.setMaximumSize(QSize(538, 596))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(10)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/python.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textEdit_2 = QTextEdit(self.tab_2)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_3.addWidget(self.textEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u041e\u041e &quot;\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f \u0420\u043e\u0433\u0430 \u0438 \u041a\u043e\u043f\u044b\u0442\u0430&quot;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u041d\u041d: 12397854690</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">\u0420/c: 494949492339494 \u0432 \u0411\u0430\u043d\u043a\u0435 &quot;\u0410\u041e \u0410\u043b\u044c\u0444\u0430 \u0431\u0430\u043d\u043a&quot;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041a/\u0441: 88006594930404; \u0411\u0418\u041a: 23030203023</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042e\u0440. \u0430\u0434\u0440\u0435\u0441: \u0433.\u041f\u0443\u0448\u043a\u0438\u043d, \u0443\u043b\u0438\u0446\u0430 \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0434. 11 \u043e\u0444\u0438\u0441 800</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0442. \u0430\u0434\u0440\u0435\u0441: \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u042e\u0440. \u0430\u0434\u0440\u0435\u0441\u043e\u043c.</p>\n"
"<p style=\" margi"
                        "n-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043b\u0435\u0444\u043e\u043d: +7 345 7773515</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442 11/11/1111 \u0433.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u0421\u041f\u0420\u0410\u0412\u041a\u0410</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0441\u0442\u043e\u044f\u0449\u044f\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0435\u0442 \u0434\u043e\u0445\u043e\u0434\u044b \u0444\u0438\u0440\u043c\u044b \u0432 \u043f\u0435\u0440\u0438\u043e\u0434 \u0441 00/00/0000 \u043f\u043e 11/11/1111 \u0432 \u0440\u0430\u0437\u043c\u0435\u0440\u0435 {\u0441\u0443\u043c\u043c\u0430} \u0440\u0443\u0431\u043b\u0435\u0439</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e"
                        "\u0440 ______________________/ </p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 PDF \u0444\u043e\u0440\u043c\u0430\u0442\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0414\u043e\u0445\u043e\u0434\u044b \u0437\u0430 \u0433\u043e\u0434", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u041e\u041e &quot;\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f \u0420\u043e\u0433\u0430 \u0438 \u041a\u043e\u043f\u044b\u0442\u0430&quot;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u041d\u041d: 12397854690</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">\u0420/c: 494949492339494 \u0432 \u0411\u0430\u043d\u043a\u0435 &quot;\u0410\u041e \u0410\u043b\u044c\u0444\u0430 \u0431\u0430\u043d\u043a&quot;</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041a/\u0441: 88006594930404; \u0411\u0418\u041a: 23030203023</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042e\u0440. \u0430\u0434\u0440\u0435\u0441: \u0433.\u041f\u0443\u0448\u043a\u0438\u043d, \u0443\u043b\u0438\u0446\u0430 \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0434. 11 \u043e\u0444\u0438\u0441 800</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0442. \u0430\u0434\u0440\u0435\u0441: \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u0435\u0442 \u0441 \u042e\u0440. \u0430\u0434\u0440\u0435\u0441\u043e\u043c.</p>\n"
"<p style=\" margi"
                        "n-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043b\u0435\u0444\u043e\u043d: +7 345 7773515</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442 11/11/1111 \u0433.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u0421\u041f\u0420\u0410\u0412\u041a\u0410</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0430\u0441\u0442\u043e\u044f\u0449\u044f\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u0435\u0442 \u0434\u043e\u0445\u043e\u0434\u044b \u0444\u0438\u0440\u043c\u044b \u0432 \u043f\u0435\u0440\u0438\u043e\u0434 \u0441 00/00/0000 \u043f\u043e 11/11/1111 \u0432 \u0440\u0430\u0437\u043c\u0435\u0440\u0435 {\u0441\u0443\u043c\u043c\u0430} \u0440\u0443\u0431\u043b\u0435\u0439</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e"
                        "\u0440 ______________________/ </p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 PDF \u0444\u043e\u0440\u043c\u0430\u0442\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0414\u043e\u0445\u043e\u0434\u044b \u0437\u0430 \u043f\u043e\u043b\u0433\u043e\u0434\u0430", None))
    # retranslateUi

