# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekran.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_yardimci(object):
    def setupUi(self, yardimci):
        yardimci.setObjectName("yardimci")
        yardimci.resize(609, 494)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(yardimci)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(yardimci)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editModul = QtWidgets.QLineEdit(yardimci)
        self.editModul.setObjectName("editModul")
        self.horizontalLayout.addWidget(self.editModul)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listModuller = QtWidgets.QListWidget(yardimci)
        self.listModuller.setObjectName("listModuller")
        self.horizontalLayout_2.addWidget(self.listModuller)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editTip = QtWidgets.QLineEdit(yardimci)
        self.editTip.setObjectName("editTip")
        self.verticalLayout.addWidget(self.editTip)
        self.textYardim = QtWidgets.QTextEdit(yardimci)
        self.textYardim.setObjectName("textYardim")
        self.verticalLayout.addWidget(self.textYardim)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(yardimci)
        self.editModul.returnPressed.connect(yardimci.doldur)
        self.listModuller.itemClicked['QListWidgetItem*'].connect(yardimci.detay)
        QtCore.QMetaObject.connectSlotsByName(yardimci)

    def retranslateUi(self, yardimci):
        _translate = QtCore.QCoreApplication.translate
        yardimci.setWindowTitle(_translate("yardimci", "Dialog"))
        self.label.setText(_translate("yardimci", "Modul Adi"))

