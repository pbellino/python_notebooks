# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_calibrated_transmission.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1347, 949)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pyqtgraph_widget = QtWidgets.QWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqtgraph_widget.sizePolicy().hasHeightForWidth())
        self.pyqtgraph_widget.setSizePolicy(sizePolicy)
        self.pyqtgraph_widget.setObjectName("pyqtgraph_widget")
        self.horizontalLayout_2.addWidget(self.pyqtgraph_widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.previous_image_button.setEnabled(False)
        self.previous_image_button.setObjectName("previous_image_button")
        self.horizontalLayout_3.addWidget(self.previous_image_button)
        self.file_slider = QtWidgets.QSlider(self.layoutWidget)
        self.file_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.file_slider.setObjectName("file_slider")
        self.horizontalLayout_3.addWidget(self.file_slider)
        self.next_image_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_3.addWidget(self.next_image_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.toolBox = QtWidgets.QToolBox(self.splitter)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 590, 646))
        self.page.setObjectName("page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.use_calibration_checkbox = QtWidgets.QCheckBox(self.page)
        self.use_calibration_checkbox.setChecked(True)
        self.use_calibration_checkbox.setObjectName("use_calibration_checkbox")
        self.horizontalLayout_12.addWidget(self.use_calibration_checkbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 1, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_3.addWidget(self.lineEdit_17, 0, 1, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_3.addWidget(self.lineEdit_31, 1, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setObjectName("label_34")
        self.gridLayout_3.addWidget(self.label_34, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setObjectName("label_36")
        self.gridLayout_3.addWidget(self.label_36, 0, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 1, 2, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_3.addWidget(self.lineEdit_29, 1, 1, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_3.addWidget(self.lineEdit_30, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_38 = QtWidgets.QLabel(self.groupBox)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_4.addWidget(self.label_38)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 1666))
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStatusTip("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_39 = QtWidgets.QLabel(self.groupBox)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_5.addWidget(self.label_39)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.horizontalLayout_5.addWidget(self.lineEdit_32)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_40 = QtWidgets.QLabel(self.groupBox_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 1, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_18.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_4.addWidget(self.lineEdit_18, 0, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_4.addWidget(self.lineEdit_33, 1, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setObjectName("label_41")
        self.gridLayout_4.addWidget(self.label_41, 0, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox_2)
        self.label_42.setObjectName("label_42")
        self.gridLayout_4.addWidget(self.label_42, 0, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.groupBox_2)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 1, 2, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_4.addWidget(self.lineEdit_34, 1, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_4.addWidget(self.lineEdit_35, 0, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_44 = QtWidgets.QLabel(self.groupBox_2)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_7.addWidget(self.label_44)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setMaximumSize(QtCore.QSize(50, 1666))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_9.addWidget(self.pushButton_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStatusTip("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_9.addWidget(self.pushButton_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_45 = QtWidgets.QLabel(self.groupBox_2)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_10.addWidget(self.label_45)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.horizontalLayout_10.addWidget(self.lineEdit_36)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 797, 698))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.remove_row = QtWidgets.QPushButton(self.page_2)
        self.remove_row.setMinimumSize(QtCore.QSize(50, 40))
        self.remove_row.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.remove_row.setFont(font)
        self.remove_row.setObjectName("remove_row")
        self.horizontalLayout_6.addWidget(self.remove_row)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.add_row = QtWidgets.QPushButton(self.page_2)
        self.add_row.setMinimumSize(QtCore.QSize(50, 40))
        self.add_row.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.add_row.setFont(font)
        self.add_row.setObjectName("add_row")
        self.horizontalLayout_6.addWidget(self.add_row)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.toolBox.addItem(self.page_2, "")
        self.measurement_widget = QtWidgets.QWidget(self.splitter_2)
        self.measurement_widget.setObjectName("measurement_widget")
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.summary_table = QtWidgets.QTableWidget(self.tab_2)
        self.summary_table.setAlternatingRowColors(True)
        self.summary_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.summary_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.summary_table.setObjectName("summary_table")
        self.summary_table.setColumnCount(3)
        self.summary_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_8.addWidget(self.summary_table)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.actionWater_Intake = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake.setObjectName("actionWater_Intake")
        self.actionImportedFilesMetadata = QtWidgets.QAction(MainWindow)
        self.actionImportedFilesMetadata.setObjectName("actionImportedFilesMetadata")
        self.actionBy_Time_Stamp = QtWidgets.QAction(MainWindow)
        self.actionBy_Time_Stamp.setObjectName("actionBy_Time_Stamp")
        self.actionBy_File_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_File_Name.setObjectName("actionBy_File_Name")
        self.actionDsc_files = QtWidgets.QAction(MainWindow)
        self.actionDsc_files.setObjectName("actionDsc_files")
        self.actionDsc = QtWidgets.QAction(MainWindow)
        self.actionDsc.setObjectName("actionDsc")
        self.actionWater_Intake_2 = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake_2.setObjectName("actionWater_Intake_2")
        self.actionProfiles = QtWidgets.QAction(MainWindow)
        self.actionProfiles.setObjectName("actionProfiles")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.file_slider.sliderMoved['int'].connect(MainWindow.slider_file_changed)
        self.file_slider.valueChanged['int'].connect(MainWindow.slider_file_changed)
        self.previous_image_button.clicked.connect(MainWindow.previous_image_button_clicked)
        self.next_image_button.clicked.connect(MainWindow.next_image_button_clicked)
        self.export_button.clicked.connect(MainWindow.export_button_clicked)
        self.use_calibration_checkbox.clicked.connect(MainWindow.use_calibration_checked)
        self.remove_row.clicked.connect(MainWindow.remove_row_button_clicked)
        self.add_row.clicked.connect(MainWindow.add_row_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calbrated Transmission"))
        self.previous_image_button.setText(_translate("MainWindow", "Prev. Image"))
        self.next_image_button.setText(_translate("MainWindow", "Next Image"))
        self.use_calibration_checkbox.setText(_translate("MainWindow", "Use Calibration"))
        self.groupBox.setTitle(_translate("MainWindow", "Calibration 1"))
        self.label_35.setText(_translate("MainWindow", "y0"))
        self.label_34.setText(_translate("MainWindow", "X0"))
        self.label_36.setText(_translate("MainWindow", "width"))
        self.label_37.setText(_translate("MainWindow", "height"))
        self.label_38.setText(_translate("MainWindow", "File Index"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "Display This File"))
        self.label_2.setText(_translate("MainWindow", "or"))
        self.pushButton_5.setText(_translate("MainWindow", "Use Current File"))
        self.label_39.setText(_translate("MainWindow", "Value"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Calibration 2"))
        self.label_40.setText(_translate("MainWindow", "y0"))
        self.label_41.setText(_translate("MainWindow", "X0"))
        self.label_42.setText(_translate("MainWindow", "width"))
        self.label_43.setText(_translate("MainWindow", "height"))
        self.label_44.setText(_translate("MainWindow", "File Index"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.pushButton_6.setText(_translate("MainWindow", "Display This File"))
        self.label_4.setText(_translate("MainWindow", "or"))
        self.pushButton_7.setText(_translate("MainWindow", "Use Current File"))
        self.label_45.setText(_translate("MainWindow", "Value"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Calibration"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X0"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y0"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Width"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Height"))
        self.remove_row.setText(_translate("MainWindow", "-"))
        self.add_row.setText(_translate("MainWindow", "+"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Measurement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Measurement"))
        item = self.summary_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Files Name"))
        item = self.summary_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time Stamp"))
        item = self.summary_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Relative Time (s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Summary"))
        self.pushButton.setText(_translate("MainWindow", "Help"))
        self.export_button.setText(_translate("MainWindow", "Export All Profiles ..."))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))

