# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lensdefinition.ui'
#
# Created: Sun Dec  8 11:48:38 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_lensdefinitiondialog(object):
    def setupUi(self, lensdefinitiondialog):
        lensdefinitiondialog.setObjectName("lensdefinitiondialog")
        lensdefinitiondialog.resize(526, 640)
        self.qdldf_lbl = QtGui.QLabel(lensdefinitiondialog)
        self.qdldf_lbl.setGeometry(QtCore.QRect(10, 10, 501, 211))
        self.qdldf_lbl.setWordWrap(True)
        self.qdldf_lbl.setObjectName("qdldf_lbl")
        self.gridLayoutWidget_13 = QtGui.QWidget(lensdefinitiondialog)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(20, 240, 471, 335))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtGui.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(10, 10, -1, -1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_99 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_99.setObjectName("label_99")
        self.gridLayout_13.addWidget(self.label_99, 4, 0, 1, 1)
        self.lens_maxaperturevalue = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_maxaperturevalue.setObjectName("lens_maxaperturevalue")
        self.gridLayout_13.addWidget(self.lens_maxaperturevalue, 9, 1, 1, 1)
        self.label_100 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_100.setObjectName("label_100")
        self.gridLayout_13.addWidget(self.label_100, 7, 0, 1, 1)
        self.lens_make = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_make.setObjectName("lens_make")
        self.gridLayout_13.addWidget(self.lens_make, 2, 1, 1, 1)
        self.label_97 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_97.setObjectName("label_97")
        self.gridLayout_13.addWidget(self.label_97, 3, 0, 1, 1)
        self.lens_serialnumber = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_serialnumber.setObjectName("lens_serialnumber")
        self.gridLayout_13.addWidget(self.lens_serialnumber, 4, 1, 1, 1)
        self.label_96 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_96.setObjectName("label_96")
        self.gridLayout_13.addWidget(self.label_96, 2, 0, 1, 1)
        self.label_109 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_109.setObjectName("label_109")
        self.gridLayout_13.addWidget(self.label_109, 8, 0, 1, 1)
        self.lens_focallengthin35mmformat = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_focallengthin35mmformat.setObjectName("lens_focallengthin35mmformat")
        self.gridLayout_13.addWidget(self.lens_focallengthin35mmformat, 7, 1, 1, 1)
        self.label_106 = QtGui.QLabel(self.gridLayoutWidget_13)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_106.setFont(font)
        self.label_106.setText("")
        self.label_106.setObjectName("label_106")
        self.gridLayout_13.addWidget(self.label_106, 5, 0, 1, 1)
        self.lens_model = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_model.setObjectName("lens_model")
        self.gridLayout_13.addWidget(self.lens_model, 3, 1, 1, 1)
        self.checkBox_qdldf_new_lens = QtGui.QCheckBox(self.gridLayoutWidget_13)
        self.checkBox_qdldf_new_lens.setObjectName("checkBox_qdldf_new_lens")
        self.gridLayout_13.addWidget(self.checkBox_qdldf_new_lens, 0, 0, 1, 1)
        self.label_102 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_102.setObjectName("label_102")
        self.gridLayout_13.addWidget(self.label_102, 6, 0, 1, 1)
        self.lens_fnumber = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_fnumber.setObjectName("lens_fnumber")
        self.gridLayout_13.addWidget(self.lens_fnumber, 8, 1, 1, 1)
        self.lens_focallength = QtGui.QLineEdit(self.gridLayoutWidget_13)
        self.lens_focallength.setObjectName("lens_focallength")
        self.gridLayout_13.addWidget(self.lens_focallength, 6, 1, 1, 1)
        self.label_105 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_105.setText("")
        self.label_105.setObjectName("label_105")
        self.gridLayout_13.addWidget(self.label_105, 11, 0, 1, 1)
        self.label_107 = QtGui.QLabel(self.gridLayoutWidget_13)
        self.label_107.setObjectName("label_107")
        self.gridLayout_13.addWidget(self.label_107, 9, 0, 1, 1)
        self.qdldf_selectlens_label = QtGui.QLabel(self.gridLayoutWidget_13)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.qdldf_selectlens_label.setFont(font)
        self.qdldf_selectlens_label.setObjectName("qdldf_selectlens_label")
        self.gridLayout_13.addWidget(self.qdldf_selectlens_label, 1, 0, 1, 1)
        self.qdldf_selectlens_combobox = QtGui.QComboBox(self.gridLayoutWidget_13)
        self.qdldf_selectlens_combobox.setObjectName("qdldf_selectlens_combobox")
        self.gridLayout_13.addWidget(self.qdldf_selectlens_combobox, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(lensdefinitiondialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 600, 311, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.qdldf_dialogbuttons = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.qdldf_dialogbuttons.setContentsMargins(0, 0, 0, 0)
        self.qdldf_dialogbuttons.setObjectName("qdldf_dialogbuttons")
        self.btn_qdldf_select = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_qdldf_select.setObjectName("btn_qdldf_select")
        self.qdldf_dialogbuttons.addWidget(self.btn_qdldf_select)
        self.btn_qdldf_cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_qdldf_cancel.setObjectName("btn_qdldf_cancel")
        self.qdldf_dialogbuttons.addWidget(self.btn_qdldf_cancel)
        self.btn_qdldf_save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_qdldf_save.setObjectName("btn_qdldf_save")
        self.qdldf_dialogbuttons.addWidget(self.btn_qdldf_save)

        self.retranslateUi(lensdefinitiondialog)
        QtCore.QMetaObject.connectSlotsByName(lensdefinitiondialog)
        lensdefinitiondialog.setTabOrder(self.btn_qdldf_select, self.btn_qdldf_cancel)
        lensdefinitiondialog.setTabOrder(self.btn_qdldf_cancel, self.btn_qdldf_save)
        lensdefinitiondialog.setTabOrder(self.btn_qdldf_save, self.checkBox_qdldf_new_lens)
        lensdefinitiondialog.setTabOrder(self.checkBox_qdldf_new_lens, self.qdldf_selectlens_combobox)
        lensdefinitiondialog.setTabOrder(self.qdldf_selectlens_combobox, self.lens_make)
        lensdefinitiondialog.setTabOrder(self.lens_make, self.lens_model)
        lensdefinitiondialog.setTabOrder(self.lens_model, self.lens_serialnumber)
        lensdefinitiondialog.setTabOrder(self.lens_serialnumber, self.lens_focallength)
        lensdefinitiondialog.setTabOrder(self.lens_focallength, self.lens_focallengthin35mmformat)
        lensdefinitiondialog.setTabOrder(self.lens_focallengthin35mmformat, self.lens_fnumber)
        lensdefinitiondialog.setTabOrder(self.lens_fnumber, self.lens_maxaperturevalue)

    def retranslateUi(self, lensdefinitiondialog):
        lensdefinitiondialog.setWindowTitle(QtGui.QApplication.translate("lensdefinitiondialog", "Lens definitions", None, QtGui.QApplication.UnicodeUTF8))
        self.qdldf_lbl.setText(QtGui.QApplication.translate("lensdefinitiondialog", "<html><head/><body><p>This dialog gives you the option to select and use, create or modify a lens definition. <br>Examples are: <ul><li>you have an old lens (via an adapter ring) that\'s not recognised by your camera.</li> <li>you have a tele/macro converter attached onto your lens giving incorrect settings for fnumber, aperture and so on. </li></ul><p>This dialog gives you the option so select a lens definition, modify a lens definition or create a lens definition. </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_99.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Serial number:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_100.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Focal length (35mm):", None, QtGui.QApplication.UnicodeUTF8))
        self.lens_make.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "This refers to the make of the lens", None, QtGui.QApplication.UnicodeUTF8))
        self.label_97.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Model:", None, QtGui.QApplication.UnicodeUTF8))
        self.lens_serialnumber.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "This refers to the serial number of the lens", None, QtGui.QApplication.UnicodeUTF8))
        self.label_96.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Make:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_109.setText(QtGui.QApplication.translate("lensdefinitiondialog", "fnumber:", None, QtGui.QApplication.UnicodeUTF8))
        self.lens_model.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "This refers to the model of the lens", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_qdldf_new_lens.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Define new lens", None, QtGui.QApplication.UnicodeUTF8))
        self.label_102.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Focal length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_107.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Max. aperturevalue:", None, QtGui.QApplication.UnicodeUTF8))
        self.qdldf_selectlens_label.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Select lens:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_select.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "Select the lens and close the dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_select.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_cancel.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "Cancel and close this dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_cancel.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_save.setToolTip(QtGui.QApplication.translate("lensdefinitiondialog", "Save your new or modified lens definition", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_qdldf_save.setText(QtGui.QApplication.translate("lensdefinitiondialog", "Save", None, QtGui.QApplication.UnicodeUTF8))

