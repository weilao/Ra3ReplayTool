# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/weilao/GitHub/Ra3ReplayTool/main.ui'
#
# Created: Wed Jan 16 20:36:38 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(838, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_H = QtGui.QMenu(self.menubar)
        self.menu_H.setObjectName(_fromUtf8("menu_H"))
        self.menu_S = QtGui.QMenu(self.menubar)
        self.menu_S.setObjectName(_fromUtf8("menu_S"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(200, 360))
        self.dockWidget.setMaximumSize(QtCore.QSize(200, 524287))
        self.dockWidget.setBaseSize(QtCore.QSize(200, 0))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(3, 0, 3, 0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(160, 160))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 160))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(70, 70, 54, 31))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName(_fromUtf8("label"))
        self.gbPlayer1 = QtGui.QGroupBox(self.groupBox_2)
        self.gbPlayer1.setGeometry(QtCore.QRect(10, 20, 61, 131))
        self.gbPlayer1.setTitle(_fromUtf8(""))
        self.gbPlayer1.setObjectName(_fromUtf8("gbPlayer1"))
        self.rbSoviet1 = QtGui.QRadioButton(self.gbPlayer1)
        self.rbSoviet1.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.rbSoviet1.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/_s.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbSoviet1.setIcon(icon1)
        self.rbSoviet1.setIconSize(QtCore.QSize(21, 18))
        self.rbSoviet1.setChecked(False)
        self.rbSoviet1.setAutoRepeat(False)
        self.rbSoviet1.setObjectName(_fromUtf8("rbSoviet1"))
        self.rbEmpire1 = QtGui.QRadioButton(self.gbPlayer1)
        self.rbEmpire1.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.rbEmpire1.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/_e.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbEmpire1.setIcon(icon2)
        self.rbEmpire1.setIconSize(QtCore.QSize(21, 18))
        self.rbEmpire1.setObjectName(_fromUtf8("rbEmpire1"))
        self.rbAllied1 = QtGui.QRadioButton(self.gbPlayer1)
        self.rbAllied1.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.rbAllied1.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/_a.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbAllied1.setIcon(icon3)
        self.rbAllied1.setIconSize(QtCore.QSize(21, 18))
        self.rbAllied1.setObjectName(_fromUtf8("rbAllied1"))
        self.rbRandom1 = QtGui.QRadioButton(self.gbPlayer1)
        self.rbRandom1.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.rbRandom1.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/_r.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbRandom1.setIcon(icon4)
        self.rbRandom1.setIconSize(QtCore.QSize(21, 18))
        self.rbRandom1.setObjectName(_fromUtf8("rbRandom1"))
        self.rbNoFaction1 = QtGui.QRadioButton(self.gbPlayer1)
        self.rbNoFaction1.setGeometry(QtCore.QRect(6, 122, 0, 0))
        self.rbNoFaction1.setMaximumSize(QtCore.QSize(0, 0))
        self.rbNoFaction1.setText(_fromUtf8(""))
        self.rbNoFaction1.setCheckable(True)
        self.rbNoFaction1.setChecked(False)
        self.rbNoFaction1.setAutoRepeat(False)
        self.rbNoFaction1.setObjectName(_fromUtf8("rbNoFaction1"))
        self.gbPlayer2 = QtGui.QGroupBox(self.groupBox_2)
        self.gbPlayer2.setGeometry(QtCore.QRect(120, 20, 61, 131))
        self.gbPlayer2.setTitle(_fromUtf8(""))
        self.gbPlayer2.setObjectName(_fromUtf8("gbPlayer2"))
        self.rbSoviet2 = QtGui.QRadioButton(self.gbPlayer2)
        self.rbSoviet2.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.rbSoviet2.setText(_fromUtf8(""))
        self.rbSoviet2.setIcon(icon1)
        self.rbSoviet2.setIconSize(QtCore.QSize(21, 18))
        self.rbSoviet2.setChecked(False)
        self.rbSoviet2.setAutoRepeat(False)
        self.rbSoviet2.setObjectName(_fromUtf8("rbSoviet2"))
        self.rbEmpire2 = QtGui.QRadioButton(self.gbPlayer2)
        self.rbEmpire2.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.rbEmpire2.setText(_fromUtf8(""))
        self.rbEmpire2.setIcon(icon2)
        self.rbEmpire2.setIconSize(QtCore.QSize(21, 18))
        self.rbEmpire2.setObjectName(_fromUtf8("rbEmpire2"))
        self.rbAllied2 = QtGui.QRadioButton(self.gbPlayer2)
        self.rbAllied2.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.rbAllied2.setText(_fromUtf8(""))
        self.rbAllied2.setIcon(icon3)
        self.rbAllied2.setIconSize(QtCore.QSize(21, 18))
        self.rbAllied2.setObjectName(_fromUtf8("rbAllied2"))
        self.rbRandom2 = QtGui.QRadioButton(self.gbPlayer2)
        self.rbRandom2.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.rbRandom2.setText(_fromUtf8(""))
        self.rbRandom2.setIcon(icon4)
        self.rbRandom2.setIconSize(QtCore.QSize(21, 18))
        self.rbRandom2.setObjectName(_fromUtf8("rbRandom2"))
        self.rbNoFaction2 = QtGui.QRadioButton(self.gbPlayer2)
        self.rbNoFaction2.setEnabled(True)
        self.rbNoFaction2.setGeometry(QtCore.QRect(55, 122, 0, 0))
        self.rbNoFaction2.setMinimumSize(QtCore.QSize(0, 0))
        self.rbNoFaction2.setMaximumSize(QtCore.QSize(0, 0))
        self.rbNoFaction2.setText(_fromUtf8(""))
        self.rbNoFaction2.setCheckable(True)
        self.rbNoFaction2.setChecked(False)
        self.rbNoFaction2.setAutoRepeat(False)
        self.rbNoFaction2.setObjectName(_fromUtf8("rbNoFaction2"))
        self.pbAllReps = QtGui.QPushButton(self.groupBox_2)
        self.pbAllReps.setGeometry(QtCore.QRect(80, 120, 31, 23))
        self.pbAllReps.setObjectName(_fromUtf8("pbAllReps"))
        self.verticalLayout.addWidget(self.groupBox_2)
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 192, 219))
        self.toolBoxPage1.setObjectName(_fromUtf8("toolBoxPage1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.toolBoxPage1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.toolBox.addItem(self.toolBoxPage1, _fromUtf8(""))
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 192, 219))
        self.toolBoxPage2.setObjectName(_fromUtf8("toolBoxPage2"))
        self.toolBox.addItem(self.toolBoxPage2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_A = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_A.setIcon(icon5)
        self.action_A.setObjectName(_fromUtf8("action_A"))
        self.menu_H.addAction(self.action_A)
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "红色警戒3 录像工具", None))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)", None))
        self.menu_S.setTitle(_translate("MainWindow", "设置(S&)", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "录像分类", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "搜索", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "阵营", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Vs</span></p></body></html>", None))
        self.pbAllReps.setText(_translate("MainWindow", "全部", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("MainWindow", "             地图", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), _translate("MainWindow", "             玩家", None))
        self.action_A.setText(_translate("MainWindow", "联系作者(&A)", None))

import res_rc
