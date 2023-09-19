# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_menu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1504, 909)
        icon = QIcon()
        iconThemeName = u"applications-development"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"font-family: Noto Sans SC;\n"
"font-family-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.Update_btn = QPushButton(self.centralwidget)
        self.Update_btn.setObjectName(u"Update_btn")
        self.Update_btn.setMaximumSize(QSize(200, 16777215))
        self.Update_btn.setStyleSheet(u"QText{\n"
"color: rgb(255, 255, 255)\n"
"}")

        self.horizontalLayout_3.addWidget(self.Update_btn)

        self.apply_btn = QPushButton(self.centralwidget)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.apply_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(231, 231, 231)")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(68, 68, 68);\n"
"border-radius: 10px")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"color: white\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(9)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(209, 209, 209)")

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"")
        self.FOOTBALL = QWidget()
        self.FOOTBALL.setObjectName(u"FOOTBALL")
        self.FOOTBALL.setGeometry(QRect(0, 0, 1476, 631))
        self.verticalLayout_3 = QVBoxLayout(self.FOOTBALL)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget_football = QTableWidget(self.FOOTBALL)
        if (self.tableWidget_football.columnCount() < 9):
            self.tableWidget_football.setColumnCount(9)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget_football.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_football.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_football.setObjectName(u"tableWidget_football")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(12)
        self.tableWidget_football.setFont(font2)
        self.tableWidget_football.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tableWidget_football.setAutoFillBackground(False)
        self.tableWidget_football.setStyleSheet(u"\n"
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
        self.tableWidget_football.setFrameShape(QFrame.Box)
        self.tableWidget_football.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_football.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_football.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_football.setAlternatingRowColors(True)
        self.tableWidget_football.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_football.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_football.setTextElideMode(Qt.ElideRight)
        self.tableWidget_football.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_football.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_football.setShowGrid(True)
        self.tableWidget_football.setGridStyle(Qt.SolidLine)
        self.tableWidget_football.setWordWrap(True)
        self.tableWidget_football.horizontalHeader().setVisible(True)
        self.tableWidget_football.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_football.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_football.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_football.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableWidget_football)

        self.toolBox.addItem(self.FOOTBALL, u"FOOTBALL")
        self.HOCKEY = QWidget()
        self.HOCKEY.setObjectName(u"HOCKEY")
        self.HOCKEY.setGeometry(QRect(0, 0, 1476, 631))
        self.gridLayout = QGridLayout(self.HOCKEY)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_hockey = QTableWidget(self.HOCKEY)
        if (self.tableWidget_hockey.columnCount() < 9):
            self.tableWidget_hockey.setColumnCount(9)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setForeground(brush1);
        self.tableWidget_hockey.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_hockey.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.tableWidget_hockey.setObjectName(u"tableWidget_hockey")
        self.tableWidget_hockey.setFont(font2)
        self.tableWidget_hockey.setContextMenuPolicy(Qt.PreventContextMenu)
        self.tableWidget_hockey.setAutoFillBackground(False)
        self.tableWidget_hockey.setStyleSheet(u"\n"
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
        self.tableWidget_hockey.setFrameShape(QFrame.Box)
        self.tableWidget_hockey.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_hockey.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_hockey.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget_hockey.setAlternatingRowColors(True)
        self.tableWidget_hockey.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_hockey.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_hockey.setTextElideMode(Qt.ElideRight)
        self.tableWidget_hockey.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_hockey.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_hockey.setShowGrid(True)
        self.tableWidget_hockey.setGridStyle(Qt.SolidLine)
        self.tableWidget_hockey.setWordWrap(True)
        self.tableWidget_hockey.horizontalHeader().setVisible(True)
        self.tableWidget_hockey.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_hockey.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_hockey.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_hockey.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tableWidget_hockey, 0, 0, 1, 1)

        self.toolBox.addItem(self.HOCKEY, u"HOCKEY")

        self.horizontalLayout.addWidget(self.toolBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 4)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1504, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SportsToday", None))
        self.Update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply updates", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"For update the data: click Update, and then Apply Updates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to SportsToday! ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To find out the details of the event or the information of the team - double-click on it!", None))
        ___qtablewidgetitem = self.tableWidget_football.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem1 = self.tableWidget_football.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TOURNAMENT", None));
        ___qtablewidgetitem2 = self.tableWidget_football.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"HOME", None));
        ___qtablewidgetitem3 = self.tableWidget_football.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SCORE Home", None));
        ___qtablewidgetitem4 = self.tableWidget_football.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SCORE Away", None));
        ___qtablewidgetitem5 = self.tableWidget_football.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"AWAY", None));
        ___qtablewidgetitem6 = self.tableWidget_football.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"COEF1", None));
        ___qtablewidgetitem7 = self.tableWidget_football.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"COEFX", None));
        ___qtablewidgetitem8 = self.tableWidget_football.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"COEF2", None));
        self.toolBox.setItemText(self.toolBox.indexOf(self.FOOTBALL), QCoreApplication.translate("MainWindow", u"FOOTBALL", None))
        ___qtablewidgetitem9 = self.tableWidget_hockey.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DATE", None));
        ___qtablewidgetitem10 = self.tableWidget_hockey.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TOURNAMENT", None));
        ___qtablewidgetitem11 = self.tableWidget_hockey.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"HOME", None));
        ___qtablewidgetitem12 = self.tableWidget_hockey.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SCORE Home", None));
        ___qtablewidgetitem13 = self.tableWidget_hockey.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"SCORE Away", None));
        ___qtablewidgetitem14 = self.tableWidget_hockey.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"AWAY", None));
        ___qtablewidgetitem15 = self.tableWidget_hockey.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"COEF1", None));
        ___qtablewidgetitem16 = self.tableWidget_hockey.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"COEFX", None));
        ___qtablewidgetitem17 = self.tableWidget_hockey.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"COEF2", None));
        self.toolBox.setItemText(self.toolBox.indexOf(self.HOCKEY), QCoreApplication.translate("MainWindow", u"HOCKEY", None))
    # retranslateUi

