# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QSizePolicy, QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 445)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sourceLabel = QLabel(Form)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.sourceLabel.setMinimumSize(QSize(0, 15))
        self.sourceLabel.setMaximumSize(QSize(16777215, 15))

        self.gridLayout.addWidget(self.sourceLabel, 0, 0, 1, 4)

        self.dirEdit = QLineEdit(Form)
        self.dirEdit.setObjectName(u"dirEdit")
        self.dirEdit.setMinimumSize(QSize(0, 30))
        self.dirEdit.setMaximumSize(QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 3)

        self.loadFilesButton = QPushButton(Form)
        self.loadFilesButton.setObjectName(u"loadFilesButton")
        self.loadFilesButton.setMinimumSize(QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.loadFilesButton, 1, 3, 1, 1)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.srcFileList = QListWidget(self.widget)
        self.srcFileList.setObjectName(u"srcFileList")

        self.verticalLayout.addWidget(self.srcFileList)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.dstFileList = QListWidget(self.widget1)
        self.dstFileList.setObjectName(u"dstFileList")

        self.verticalLayout_2.addWidget(self.dstFileList)

        self.splitter.addWidget(self.widget1)

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 4)

        self.filenamePrefixLabel = QLabel(Form)
        self.filenamePrefixLabel.setObjectName(u"filenamePrefixLabel")
        self.filenamePrefixLabel.setMinimumSize(QSize(0, 15))
        self.filenamePrefixLabel.setMaximumSize(QSize(16777215, 15))

        self.gridLayout.addWidget(self.filenamePrefixLabel, 3, 0, 1, 4)

        self.prefixEdit = QLineEdit(Form)
        self.prefixEdit.setObjectName(u"prefixEdit")
        self.prefixEdit.setMinimumSize(QSize(0, 30))
        self.prefixEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.prefixEdit, 4, 0, 1, 1)

        self.extensionLabel = QLabel(Form)
        self.extensionLabel.setObjectName(u"extensionLabel")
        self.extensionLabel.setMinimumSize(QSize(0, 30))
        self.extensionLabel.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.extensionLabel, 4, 1, 1, 1)

        self.renameFilesButton = QPushButton(Form)
        self.renameFilesButton.setObjectName(u"renameFilesButton")
        self.renameFilesButton.setMinimumSize(QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.renameFilesButton, 4, 2, 1, 2)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RP Renamer", None))
        self.sourceLabel.setText(QCoreApplication.translate("Form", u"Last Source Directory", None))
        self.loadFilesButton.setText(QCoreApplication.translate("Form", u"&Load Files", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Files to Rename", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Renamed Files", None))
        self.filenamePrefixLabel.setText(QCoreApplication.translate("Form", u"Filename Prefix:", None))
        self.prefixEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Rename your files to ...", None))
        self.extensionLabel.setText(QCoreApplication.translate("Form", u".jpg", None))
        self.renameFilesButton.setText(QCoreApplication.translate("Form", u"&Rename", None))
    # retranslateUi

