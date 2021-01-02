# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QLocale, QMetaObject, QCoreApplication
from PySide2.QtGui import Qt, QFont, QIcon
from PySide2.QtWidgets import QSizePolicy, QVBoxLayout, QFrame, QHBoxLayout, QSpacerItem, QLabel, QGridLayout, QLayout, QPushButton


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(450, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(450, 200))
        Dialog.setMaximumSize(QSize(450, 200))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(14)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/python.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_about_2 = QFrame(Dialog)
        self.frame_about_2.setObjectName(u"frame_about_2")
        self.frame_about_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_about_2.sizePolicy().hasHeightForWidth())
        self.frame_about_2.setSizePolicy(sizePolicy1)
        self.frame_about_2.setStyleSheet(u"background-color: #FFFFFF;")
        self.frame_about_2.setFrameShape(QFrame.StyledPanel)
        self.frame_about_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_about_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_about_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_about_2)

        self.label_about = QLabel(self.frame_about_2)
        self.label_about.setObjectName(u"label_about")

        self.horizontalLayout.addWidget(self.label_about)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_about_2 = QLabel(self.frame_about_2)
        self.label_about_2.setObjectName(u"label_about_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_about_2.sizePolicy().hasHeightForWidth())
        self.label_about_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_about_2)

        self.verticalLayout.addWidget(self.frame_about_2)

        self.frame_about = QFrame(Dialog)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_about.sizePolicy().hasHeightForWidth())
        self.frame_about.setSizePolicy(sizePolicy)
        self.frame_about.setMinimumSize(QSize(450, 45))
        self.frame_about.setMaximumSize(QSize(450, 45))
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(10)
        self.frame_about.setFont(font1)
        self.frame_about.setStyleSheet(u"")
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_about)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 10, 14, 14)
        self.horizontalSpacer_about = QSpacerItem(352, 16, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_about, 1, 0, 1, 1)

        self.pushButton_about_2 = QPushButton(self.frame_about)
        self.pushButton_about_2.setObjectName(u"pushButton_about_2")
        self.pushButton_about_2.setMinimumSize(QSize(72, 20))
        font2 = QFont()
        font2.setFamily(u"Comic Sans MS")
        font2.setPointSize(9)
        self.pushButton_about_2.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_about_2, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.frame_about)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_about.setText(QCoreApplication.translate("Dialog", u"<html>\n"
                                                                      "<head/>\n"
                                                                      "<body>\n"
                                                                      "<p>\n"
                                                                      "<img src=\":/newPrefix/images/information-mark.png\" width=\"64\" height=\"64\" />\n"
                                                                      "</p>\n"
                                                                      "</body>\n"
                                                                      "</html>", None))
        self.label_about_2.setText(QCoreApplication.translate("Dialog",
                                                              u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435</span></p><p><span style=\" font-size:10pt;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438: </span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Qt 5.15.1 (PySide2) </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyInstaller </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shiboken</li></ul><p>Email \u0434\u043b\u044f \u0441\u0432\u044f\u0437\u0438 \u0441 \u0430\u0432\u0442\u043e\u0440\u043e\u043c - <span sty"
                                                              "le=\" font-weight:600;\">pavlyuchenko_196@mail.ru</span></p><p><br/></p></body></html>",
                                                              None))
        self.pushButton_about_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi
