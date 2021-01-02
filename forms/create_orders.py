# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_orders.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize, QLocale, QMetaObject, QCoreApplication, QDate
from PySide2.QtGui import Qt, QFont, QIcon
from PySide2.QtWidgets import QSizePolicy, QSpacerItem, QLabel, QGridLayout, QPushButton, QComboBox, QGroupBox, QDateEdit, QFormLayout, QLineEdit, QTextEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(680, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(680, 350))
        Form.setMaximumSize(QSize(680, 350))
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
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QSize(160, 25))
        self.dateEdit.setMaximumSize(QSize(160, 25))
        self.dateEdit.setDate(QDate(2020, 1, 1))

        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.groupBox)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setMinimumSize(QSize(160, 25))
        self.dateEdit_2.setMaximumSize(QSize(160, 25))
        self.dateEdit_2.setDate(QDate(2020, 1, 1))

        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 2, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(250, 20))
        self.comboBox.setMaximumSize(QSize(250, 25))

        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.vehicle_brand = QLineEdit(self.groupBox)
        self.vehicle_brand.setObjectName(u"vehicle_brand")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vehicle_brand)


        self.gridLayout_3.addLayout(self.formLayout, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.breakdown_description = QTextEdit(self.groupBox)
        self.breakdown_description.setObjectName(u"breakdown_description")
        sizePolicy.setHeightForWidth(self.breakdown_description.sizePolicy().hasHeightForWidth())
        self.breakdown_description.setSizePolicy(sizePolicy)
        self.breakdown_description.setMinimumSize(QSize(340, 140))
        self.breakdown_description.setMaximumSize(QSize(340, 150))

        self.gridLayout_2.addWidget(self.breakdown_description, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 1, 3, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.vehicle_model = QLineEdit(self.groupBox)
        self.vehicle_model.setObjectName(u"vehicle_model")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.vehicle_model)


        self.gridLayout_3.addLayout(self.formLayout_2, 3, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(6)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(0, 20))
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.repair_cost = QLineEdit(self.groupBox)
        self.repair_cost.setObjectName(u"repair_cost")
        sizePolicy.setHeightForWidth(self.repair_cost.sizePolicy().hasHeightForWidth())
        self.repair_cost.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.repair_cost)


        self.gridLayout_3.addLayout(self.formLayout_3, 4, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(6)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.reg_number = QLineEdit(self.groupBox)
        self.reg_number.setObjectName(u"reg_number")
        sizePolicy.setHeightForWidth(self.reg_number.sizePolicy().hasHeightForWidth())
        self.reg_number.setSizePolicy(sizePolicy)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.reg_number)


        self.gridLayout_3.addLayout(self.formLayout_4, 5, 0, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 6, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u043e\u0432", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("Form", u"d/M/yyyy", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u0440\u043a\u0430 \u0422\u0421", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u043e\u043c\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0434\u0435\u043b\u044c \u0422\u0421", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0435\u043c\u043e\u043d\u0442\u0430, \u0440\u0443\u0431.", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0441. \u041d\u043e\u043c\u0435\u0440 \u0422\u0421", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
    # retranslateUi

