# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tournament.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QGridLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Tournament(object):
    def setupUi(self, Tournament):
        if not Tournament.objectName():
            Tournament.setObjectName(u"Tournament")
        Tournament.resize(921, 438)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tournament.sizePolicy().hasHeightForWidth())
        Tournament.setSizePolicy(sizePolicy)
        Tournament.setFocusPolicy(Qt.StrongFocus)
        Tournament.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Tournament.setWindowIcon(icon)
        Tournament.setLayoutDirection(Qt.LeftToRight)
        Tournament.setStyleSheet(u"background-color: rgb(122, 122, 122)")
        self.gridLayout = QGridLayout(Tournament)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.tournament_tableWidget = QTableWidget(Tournament)
        if (self.tournament_tableWidget.columnCount() < 9):
            self.tournament_tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tournament_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tournament_tableWidget.setObjectName(u"tournament_tableWidget")
        font = QFont()
        font.setPointSize(11)
        self.tournament_tableWidget.setFont(font)
        self.tournament_tableWidget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tournament_tableWidget.setAutoFillBackground(False)
        self.tournament_tableWidget.setStyleSheet(u"\n"
"QTableWidget{\n"
"color:#DCDCDC;\n"
"background:#444444;\n"
"border:1px solid #242424;\n"
"alternate-background-color:#525252;\n"
"gridline-color:#242424;\n"
"}\n"
" \n"
"QTableWidget::item:selected{\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
" \n"
"QTableWidget::item:hover{\n"
"background:#5B5B5B;\n"
"}\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#5E5E5E;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
" \n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
" \n"
" \n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
" \n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
" \n"
" \n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
""
                        " \n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}")
        self.tournament_tableWidget.setFrameShape(QFrame.Box)
        self.tournament_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tournament_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tournament_tableWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.tournament_tableWidget.setAlternatingRowColors(True)
        self.tournament_tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tournament_tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tournament_tableWidget.setTextElideMode(Qt.ElideRight)
        self.tournament_tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tournament_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tournament_tableWidget.setShowGrid(True)
        self.tournament_tableWidget.setGridStyle(Qt.SolidLine)
        self.tournament_tableWidget.setWordWrap(True)
        self.tournament_tableWidget.horizontalHeader().setVisible(True)
        self.tournament_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tournament_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tournament_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tournament_tableWidget.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tournament_tableWidget, 0, 0, 1, 1)

        self.pushButton = QPushButton(Tournament)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)


        self.retranslateUi(Tournament)
        self.pushButton.clicked.connect(Tournament.close)

        QMetaObject.connectSlotsByName(Tournament)
    # setupUi

    def retranslateUi(self, Tournament):
        Tournament.setWindowTitle(QCoreApplication.translate("Tournament", u"Tournament info", None))
        ___qtablewidgetitem = self.tournament_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tournament", u"RANK", None));
        ___qtablewidgetitem1 = self.tournament_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tournament", u"COMPETITOR", None));
        ___qtablewidgetitem2 = self.tournament_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tournament", u"PLAYED", None));
        ___qtablewidgetitem3 = self.tournament_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tournament", u"WIN", None));
        ___qtablewidgetitem4 = self.tournament_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tournament", u"LOSS", None));
        ___qtablewidgetitem5 = self.tournament_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Tournament", u"DRAW", None));
        ___qtablewidgetitem6 = self.tournament_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Tournament", u"GOALS FOR", None));
        ___qtablewidgetitem7 = self.tournament_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Tournament", u"GOALS AGAINST", None));
        ___qtablewidgetitem8 = self.tournament_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Tournament", u"POINTS", None));
        self.pushButton.setText(QCoreApplication.translate("Tournament", u"Close", None))
    # retranslateUi

