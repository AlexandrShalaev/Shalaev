# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_noinfo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Ui_warning(object):
    def setupUi(self, Ui_warning):
        if not Ui_warning.objectName():
            Ui_warning.setObjectName(u"Ui_warning")
        Ui_warning.resize(325, 300)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Ui_warning.setWindowIcon(icon)
        Ui_warning.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 76, 76)\n"
"}\n"
"QDialog {\n"
"	background-color: rgb(122, 122, 122);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Ui_warning)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Ui_warning)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(Ui_warning)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Ui_warning)
        self.buttonBox.accepted.connect(Ui_warning.accept)
        self.buttonBox.rejected.connect(Ui_warning.reject)

        QMetaObject.connectSlotsByName(Ui_warning)
    # setupUi

    def retranslateUi(self, Ui_warning):
        Ui_warning.setWindowTitle(QCoreApplication.translate("Ui_warning", u"No info", None))
        self.label.setText(QCoreApplication.translate("Ui_warning", u"Sorry, there's no information here yet...", None))
    # retranslateUi

