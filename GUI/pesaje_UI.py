# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BasculaGUIXljXhv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 604)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ctrlWidget = QWidget(self.centralwidget)
        self.ctrlWidget.setObjectName(u"ctrlWidget")
        self.ctrlWidget.setGeometry(QRect(10, 410, 761, 161))
        self.btnTarar = QPushButton(self.ctrlWidget)
        self.btnTarar.setObjectName(u"btnTarar")
        self.btnTarar.setGeometry(QRect(30, 50, 171, 71))
        self.btnPesar = QPushButton(self.ctrlWidget)
        self.btnPesar.setObjectName(u"btnPesar")
        self.btnPesar.setGeometry(QRect(290, 50, 171, 71))
        self.btnBorrar = QPushButton(self.ctrlWidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setGeometry(QRect(540, 50, 171, 71))
        self.wdgtVista = QWidget(self.centralwidget)
        self.wdgtVista.setObjectName(u"wdgtVista")
        self.wdgtVista.setGeometry(QRect(20, 10, 741, 351))
        self.horizontalLayoutWidget = QWidget(self.wdgtVista)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 691, 281))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout.addWidget(self.lcdNumber)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnTarar.setText(QCoreApplication.translate("MainWindow", u"Tarar", None))
        self.btnPesar.setText(QCoreApplication.translate("MainWindow", u"Pesar", None))
        self.btnBorrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
    # retranslateUi

