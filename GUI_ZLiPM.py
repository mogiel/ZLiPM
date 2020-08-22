# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zl2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        Dialog.setFont(font)
        Dialog.setStyleSheet("font: 12pt \"Arial\";")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.buttonBoxClosed = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxClosed.setGeometry(QtCore.QRect(20, 440, 600, 30))
        self.buttonBoxClosed.setOrientation(QtCore.Qt.Vertical)
        self.buttonBoxClosed.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBoxClosed.setCenterButtons(True)
        self.buttonBoxClosed.setObjectName("buttonBoxClosed")
        self.Tablica = QtWidgets.QTabWidget(Dialog)
        self.Tablica.setEnabled(True)
        self.Tablica.setGeometry(QtCore.QRect(270, 20, 360, 280))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tablica.sizePolicy().hasHeightForWidth())
        self.Tablica.setSizePolicy(sizePolicy)
        self.Tablica.setMinimumSize(QtCore.QSize(0, 0))
        self.Tablica.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Tablica.setFont(font)
        self.Tablica.setMouseTracking(False)
        self.Tablica.setTabletTracking(False)
        self.Tablica.setAcceptDrops(False)
        self.Tablica.setToolTip("")
        self.Tablica.setAutoFillBackground(False)
        self.Tablica.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.Tablica.setTabPosition(QtWidgets.QTabWidget.West)
        self.Tablica.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tablica.setIconSize(QtCore.QSize(16, 16))
        self.Tablica.setElideMode(QtCore.Qt.ElideMiddle)
        self.Tablica.setDocumentMode(True)
        self.Tablica.setTabsClosable(False)
        self.Tablica.setMovable(True)
        self.Tablica.setTabBarAutoHide(True)
        self.Tablica.setObjectName("Tablica")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_9.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_9.setObjectName("textEdit_9")
        self.Tablica.addTab(self.tab, "")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tabWidgetPage1)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_4.setObjectName("textEdit_4")
        self.Tablica.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tabWidgetPage2)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_3.setObjectName("textEdit_3")
        self.Tablica.addTab(self.tabWidgetPage2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit_10 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_10.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_10.setObjectName("textEdit_10")
        self.Tablica.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_6.setObjectName("textEdit_6")
        self.Tablica.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_7.setObjectName("textEdit_7")
        self.Tablica.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_8.setGeometry(QtCore.QRect(0, 0, 320, 280))
        self.textEdit_8.setObjectName("textEdit_8")
        self.Tablica.addTab(self.tab_9, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 260, 440))
        self.tabWidget_2.setToolTipDuration(0)
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 220, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setAcceptDrops(False)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.tab_7)
        self.label.setGeometry(QtCore.QRect(20, 10, 220, 30))
        self.label.setObjectName("label")
        self.ZL_sprawdz = QtWidgets.QPushButton(self.tab_7)
        self.ZL_sprawdz.setGeometry(QtCore.QRect(20, 290, 220, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ZL_sprawdz.setFont(font)
        self.ZL_sprawdz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ZL_sprawdz.setStyleSheet("font: 20pt \"Arial\";")
        self.ZL_sprawdz.setCheckable(False)
        self.ZL_sprawdz.setAutoRepeat(False)
        self.ZL_sprawdz.setAutoExclusive(False)
        self.ZL_sprawdz.setDefault(True)
        self.ZL_sprawdz.setFlat(False)
        self.ZL_sprawdz.setObjectName("ZL_sprawdz")
        self.zagrozenia_ludzmi = QtWidgets.QComboBox(self.tab_7)
        self.zagrozenia_ludzmi.setGeometry(QtCore.QRect(20, 40, 220, 30))
        self.zagrozenia_ludzmi.setObjectName("zagrozenia_ludzmi")
        self.zagrozenia_ludzmi.addItem("")
        self.zagrozenia_ludzmi.addItem("")
        self.zagrozenia_ludzmi.addItem("")
        self.zagrozenia_ludzmi.addItem("")
        self.zagrozenia_ludzmi.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab_7)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 220, 30))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.tab_7)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 220, 30))
        self.label_2.setObjectName("label_2")
        self.ZL_ilosc_kondygnacji = QtWidgets.QSpinBox(self.tab_7)
        self.ZL_ilosc_kondygnacji.setGeometry(QtCore.QRect(20, 160, 220, 30))
        self.ZL_ilosc_kondygnacji.setMinimum(1)
        self.ZL_ilosc_kondygnacji.setMaximum(211)
        self.ZL_ilosc_kondygnacji.setProperty("value", 1)
        self.ZL_ilosc_kondygnacji.setObjectName("ZL_ilosc_kondygnacji")
        self.ZL_wysokosc_budynku = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.ZL_wysokosc_budynku.setGeometry(QtCore.QRect(20, 100, 220, 30))
        self.ZL_wysokosc_budynku.setMaximum(829.0)
        self.ZL_wysokosc_budynku.setSingleStep(0.1)
        self.ZL_wysokosc_budynku.setProperty("value", 8.9)
        self.ZL_wysokosc_budynku.setObjectName("ZL_wysokosc_budynku")
        self.ZL_poziom_stropu = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.ZL_poziom_stropu.setEnabled(True)
        self.ZL_poziom_stropu.setGeometry(QtCore.QRect(20, 250, 220, 30))
        self.ZL_poziom_stropu.setSingleStep(0.1)
        self.ZL_poziom_stropu.setProperty("value", 3.5)
        self.ZL_poziom_stropu.setObjectName("ZL_poziom_stropu")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 220, 60))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.PM_sprawdz = QtWidgets.QPushButton(self.tab_6)
        self.PM_sprawdz.setGeometry(QtCore.QRect(20, 290, 220, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PM_sprawdz.setFont(font)
        self.PM_sprawdz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PM_sprawdz.setStyleSheet("font: 20pt \"Arial\";")
        self.PM_sprawdz.setCheckable(False)
        self.PM_sprawdz.setAutoRepeat(False)
        self.PM_sprawdz.setAutoExclusive(False)
        self.PM_sprawdz.setDefault(True)
        self.PM_sprawdz.setFlat(False)
        self.PM_sprawdz.setObjectName("PM_sprawdz")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 220, 30))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.PM_ilosc_kondygnacji = QtWidgets.QSpinBox(self.tab_6)
        self.PM_ilosc_kondygnacji.setGeometry(QtCore.QRect(20, 130, 220, 30))
        self.PM_ilosc_kondygnacji.setMinimum(1)
        self.PM_ilosc_kondygnacji.setMaximum(211)
        self.PM_ilosc_kondygnacji.setObjectName("PM_ilosc_kondygnacji")
        self.PM_gestosc_obciazenia_ogniowego = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.PM_gestosc_obciazenia_ogniowego.setGeometry(QtCore.QRect(20, 70, 220, 30))
        self.PM_gestosc_obciazenia_ogniowego.setMaximum(10000.0)
        self.PM_gestosc_obciazenia_ogniowego.setSingleStep(100.0)
        self.PM_gestosc_obciazenia_ogniowego.setProperty("value", 500.0)
        self.PM_gestosc_obciazenia_ogniowego.setObjectName("PM_gestosc_obciazenia_ogniowego")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 220, 30))
        self.label_7.setObjectName("label_7")
        self.PM_wysokosc_budynku = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.PM_wysokosc_budynku.setGeometry(QtCore.QRect(20, 190, 220, 30))
        self.PM_wysokosc_budynku.setMaximum(829.0)
        self.PM_wysokosc_budynku.setSingleStep(0.1)
        self.PM_wysokosc_budynku.setProperty("value", 8.9)
        self.PM_wysokosc_budynku.setObjectName("PM_wysokosc_budynku")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 250, 380))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.Wynik = QtWidgets.QTextEdit(Dialog)
        self.Wynik.setGeometry(QtCore.QRect(295, 320, 321, 110))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Wynik.setFont(font)
        self.Wynik.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Wynik.setStyleSheet("font: 75 12pt \"Arial\";")
        self.Wynik.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.Wynik.setObjectName("Wynik")

        self.retranslateUi(Dialog)
        self.Tablica.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.buttonBoxClosed.rejected.connect(Dialog.reject)
        self.buttonBoxClosed.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ZLiPM"))
        self.buttonBoxClosed.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.buttonBoxClosed.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.textEdit_9.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ZL I </span><span style=\" font-size:10pt;\">– te, które zawierają pomieszczenia przeznaczone do jednoczesnego przebywania ponad 50 osób niebędących ich stałymi użytkownikami, a nie przeznaczone przede wszystkim do użytku ludzi o ograniczonej zdolności poruszania się;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ZL II</span><span style=\" font-size:10pt;\"> – przeznaczone przede wszystkim do użytku ludzi o ograniczonej zdolności poruszania się, takie jak: żłobki, przedszkola, szpitale, domy starców, hospicja itp.;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ZL III</span><span style=\" font-size:10pt;\"> – użyteczności publicznej niekwalifikowane do kategorii ZL I i ZL II;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ZL IV</span><span style=\" font-size:10pt;\"> – mieszkalne jedno i wielorodzinne;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ZL V</span><span style=\" font-size:10pt;\"> – zamieszkania zbiorowego niekwalifikowane do kategorii ZL I i ZL II.</span></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tab), _translate("Dialog", "ZL"))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kategoria budynku: </span><span style=\" font-size:10pt; font-weight:600;\">A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Klasa odporności ogniowej elementów budynku     (5., (*))</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 240</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R 30</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 120</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 120 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 60 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 30</TD></TR></TABLE></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tabWidgetPage1), _translate("Dialog", "A"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kategoria budynku: </span><span style=\" font-size:10pt; font-weight:600;\">B</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Klasa odporności ogniowej elementów budynku     (5., (*))</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 120</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R 30</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 60</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 60 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 30 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 30</TD></TR></TABLE></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tabWidgetPage2), _translate("Dialog", "B"))
        self.textEdit_10.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kategoria budynku: </span><span style=\" font-size:10pt; font-weight:600;\">C</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Klasa odporności ogniowej elementów budynku     (5., (*))</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 60</TD><TR><TD>-Konstrukcja dachu:</TD><TD>R15</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 60</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 30 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>EI 15 (4.)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>RE 15</TD></TR></TABLE></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tab_2), _translate("Dialog", "C"))
        self.textEdit_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kategoria budynku: </span><span style=\" font-size:10pt; font-weight:600;\">D</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Klasa odporności ogniowej elementów budynku     (5., (*))</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>R 30</TD><TR><TD>-Konstrukcja dachu:</TD><TD>(-)</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>REI 30</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>EI 30 (O<->I)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>(-)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>(-)</TD></TR></TABLE></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tab_3), _translate("Dialog", "D"))
        self.textEdit_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Kategoria budynku: </span><span style=\" font-size:10pt; font-weight:600;\">E</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Klasa odporności ogniowej elementów budynku     (5., (*))</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><TABLE style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><TR><TD>-Główna konstrukcja nośna:</TD><TD>(-)</TD><TR><TD>-Konstrukcja dachu:</TD><TD>(-)</TD></TR><TR><TD>-Strop ((1)*)</TD><TD>(-)</TD></TR><TR><TD>-Ściana zewnętrzna(1., 2.):</TD><TD>(-)</TD></TR><TR><TD>-Ściana wewnętrzna(1.):</TD><TD>(-)</TD></TR><TR><TD>-Przekrycie dachu(3.):</TD><TD>(-)</TD></TR></TABLE></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tab_4), _translate("Dialog", "E"))
        self.textEdit_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">R - nośność ogniowa.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">E - szczelność ogniowa.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">I - izolacyjność ogniowa.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(-) - nie stawia wymagań.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(*) - Z zastrzeżeniem §219 ust.1</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ognioodporność określana jest w minutach.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.) Jeżeli przegroda jest częścią głównej konstrukcji nośnej, powinna spełniać także kryteria nośności ogniowej (R) odpowiednio do wymagań zawartych w kol. 2 i 3 dla danej klasy odporności pożarowej budynku.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.) Klasa odporności ogniowej dotyczy pasa międzykondygnacyjnego wraz z połączeniem ze stropem.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.) Wymagania nie dotyczą naświetli dachowych, świetlików, lukarn i okien połaciowych (z zastrzeżeniem § 218), jeśli otwory w połaci dachowej nie zajmują więcej niż 20% jej powierzchni, nie dotyczą także budynku, w którym nad najwyższą kondygnacją znajduje się strop albo inna przegroda, spełniająca kryteria określone w stropach.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.) Dla ścian komór zsypu wymaga się EI 60, a dla drzwi komór zsypu - EI 30.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5.) Klasa odporności ogniowej dotyczy elementów wraz z uszczelnieniami złączy i dylatacjami. </span></p></body></html>"))
        self.Tablica.setTabText(self.Tablica.indexOf(self.tab_9), _translate("Dialog", "Opis"))
        self.label_4.setText(_translate("Dialog", "Poziom stropu nad pięrwszą kondygnacją [m]:"))
        self.label.setText(_translate("Dialog", "Kategoria zagrożenia ludzi:"))
        self.ZL_sprawdz.setText(_translate("Dialog", "Sprawdź"))
        self.zagrozenia_ludzmi.setItemText(0, _translate("Dialog", "ZL I"))
        self.zagrozenia_ludzmi.setItemText(1, _translate("Dialog", "ZL II"))
        self.zagrozenia_ludzmi.setItemText(2, _translate("Dialog", "ZL III"))
        self.zagrozenia_ludzmi.setItemText(3, _translate("Dialog", "ZL IV"))
        self.zagrozenia_ludzmi.setItemText(4, _translate("Dialog", "ZL V"))
        self.label_3.setText(_translate("Dialog", "Ilość kondygnacji nadziemnych:"))
        self.label_2.setText(_translate("Dialog", "Wysokość budynku [m]:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Dialog", "  ZL   "))
        self.label_5.setText(_translate("Dialog", "Gęstość obciążenia ogniowego strefy pożarowej w budynku Q[MJ/m2]:"))
        self.PM_sprawdz.setText(_translate("Dialog", "Sprawdź"))
        self.label_6.setText(_translate("Dialog", "Ilość kondygnacji nadziemnych:"))
        self.label_7.setText(_translate("Dialog", "Wysokość budynku [m]:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Dialog", "  PM   "))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program wykonany przez Mateusza Mogielskiego.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kontakt:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"m.mogielski@protonmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">m.mogielski@protonmail.com</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Oprogramowanie jest darmowe.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wersja zgodna z:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OBWIESZCZENIE MINISTRA INFRASTRUKTURY I RO ZWOJU z dnia 17 lipca 2015 r. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wszelkie uwagi prosze wysyłać na ww. e-maila.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wersja: 31.05.2019</p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Dialog", "  O programie  "))
        self.Wynik.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#000000;\">Zastrzegam, że aktualny stan oprogramowania nie pozwala całkowicie wykluczyć możliwości wystąpienia błędów obliczeniowych. Użytkownik programu powinien sprawdzać prawidłowość uzyskiwanych wyników oraz porównywać je z obowiązującymi przepisami, normami i dopuszczeniami technicznymi. Całkowita odpowiedzialność za wyniki przy pomocy oprogramowania spoczywa na jego użytkowniku.</span></p></body></html>"))

