# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_metadata.ui'
#
# Created: Sat Dec 15 12:36:16 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog_export_metadata(object):
    def setupUi(self, Dialog_export_metadata):
        Dialog_export_metadata.setObjectName("Dialog_export_metadata")
        Dialog_export_metadata.resize(428, 438)
        self.qdem_dialogButtonBox = QtGui.QDialogButtonBox(Dialog_export_metadata)
        self.qdem_dialogButtonBox.setGeometry(QtCore.QRect(70, 390, 341, 32))
        self.qdem_dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.qdem_dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.qdem_dialogButtonBox.setObjectName("qdem_dialogButtonBox")
        self.qdem_frame = QtGui.QFrame(Dialog_export_metadata)
        self.qdem_frame.setGeometry(QtCore.QRect(20, 100, 351, 191))
        self.qdem_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qdem_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.qdem_frame.setObjectName("qdem_frame")
        self.gridLayoutWidget = QtGui.QWidget(self.qdem_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 40, 251, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.rmdd_gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.rmdd_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.rmdd_gridLayout.setObjectName("rmdd_gridLayout")
        self.qdem_chk_export_exif_data = QtGui.QCheckBox(self.gridLayoutWidget)
        self.qdem_chk_export_exif_data.setObjectName("qdem_chk_export_exif_data")
        self.rmdd_gridLayout.addWidget(self.qdem_chk_export_exif_data, 0, 0, 1, 1)
        self.qdem_chk_export_xmp_data = QtGui.QCheckBox(self.gridLayoutWidget)
        self.qdem_chk_export_xmp_data.setObjectName("qdem_chk_export_xmp_data")
        self.rmdd_gridLayout.addWidget(self.qdem_chk_export_xmp_data, 1, 0, 1, 1)
        self.qdem_chk_export_iptc_data = QtGui.QCheckBox(self.gridLayoutWidget)
        self.qdem_chk_export_iptc_data.setObjectName("qdem_chk_export_iptc_data")
        self.rmdd_gridLayout.addWidget(self.qdem_chk_export_iptc_data, 3, 0, 1, 1)
        self.qdem_chk_export_gps_data = QtGui.QCheckBox(self.gridLayoutWidget)
        self.qdem_chk_export_gps_data.setObjectName("qdem_chk_export_gps_data")
        self.rmdd_gridLayout.addWidget(self.qdem_chk_export_gps_data, 2, 0, 1, 1)
        self.qdem_chk_export_iccprofile_data = QtGui.QCheckBox(self.gridLayoutWidget)
        self.qdem_chk_export_iccprofile_data.setObjectName("qdem_chk_export_iccprofile_data")
        self.rmdd_gridLayout.addWidget(self.qdem_chk_export_iccprofile_data, 4, 0, 1, 1)
        self.qdem_chk_export_all_metadata = QtGui.QCheckBox(self.qdem_frame)
        self.qdem_chk_export_all_metadata.setGeometry(QtCore.QRect(20, 10, 162, 17))
        self.qdem_chk_export_all_metadata.setObjectName("qdem_chk_export_all_metadata")
        self.qdem_lbl = QtGui.QLabel(Dialog_export_metadata)
        self.qdem_lbl.setGeometry(QtCore.QRect(20, 10, 391, 81))
        self.qdem_lbl.setWordWrap(True)
        self.qdem_lbl.setObjectName("qdem_lbl")
        self.qdem_lbl2 = QtGui.QLabel(Dialog_export_metadata)
        self.qdem_lbl2.setGeometry(QtCore.QRect(20, 310, 91, 16))
        self.qdem_lbl2.setObjectName("qdem_lbl2")
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog_export_metadata)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qdem_txt_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_txt_radiobutton.setChecked(True)
        self.qdem_txt_radiobutton.setObjectName("qdem_txt_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_txt_radiobutton)
        self.qdem_tab_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_tab_radiobutton.setObjectName("qdem_tab_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_tab_radiobutton)
        self.qdem_xml_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_xml_radiobutton.setObjectName("qdem_xml_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_xml_radiobutton)
        self.qdem_html_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_html_radiobutton.setObjectName("qdem_html_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_html_radiobutton)
        self.qdem_xmp_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_xmp_radiobutton.setObjectName("qdem_xmp_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_xmp_radiobutton)
        self.qdem_csv_radiobutton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.qdem_csv_radiobutton.setEnabled(False)
        self.qdem_csv_radiobutton.setObjectName("qdem_csv_radiobutton")
        self.horizontalLayout.addWidget(self.qdem_csv_radiobutton)

        self.retranslateUi(Dialog_export_metadata)
        QtCore.QObject.connect(self.qdem_dialogButtonBox, QtCore.SIGNAL("accepted()"), Dialog_export_metadata.accept)
        QtCore.QObject.connect(self.qdem_dialogButtonBox, QtCore.SIGNAL("rejected()"), Dialog_export_metadata.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_export_metadata)

    def retranslateUi(self, Dialog_export_metadata):
        Dialog_export_metadata.setWindowTitle(QtGui.QApplication.translate("Dialog_export_metadata", "Export metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_exif_data.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export exif data", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_xmp_data.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export xmp data", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_iptc_data.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export iptc data", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_gps_data.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "gps data can be both in exif and xmp data", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_gps_data.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export gps data", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_iccprofile_data.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export ICC profile", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_all_metadata.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "(Un)Check this value will (un)check all underlying values", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_chk_export_all_metadata.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export all metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_lbl.setText(QtGui.QApplication.translate("Dialog_export_metadata", "This option gives you the possibility to export the metadata from your selected photo(s). A number of formats is supported.\n"
"All formats give an export file per selected photo, apart from csv which will give you one (big) csv file for all selected photos.", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_lbl2.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Export to:", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_txt_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you a simple text output per photo", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_txt_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "Txt", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_tab_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you a tab separated text output per photo", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_tab_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "tab", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_xml_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you an xml formatted output file per photo", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_xml_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "xml", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_html_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you a table formatted html file per photo", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_html_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "html", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_xmp_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you an xmp structured file per photo", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_xmp_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "xmp", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_csv_radiobutton.setToolTip(QtGui.QApplication.translate("Dialog_export_metadata", "This option will give you one csv file for the selected photos", None, QtGui.QApplication.UnicodeUTF8))
        self.qdem_csv_radiobutton.setText(QtGui.QApplication.translate("Dialog_export_metadata", "csv", None, QtGui.QApplication.UnicodeUTF8))

