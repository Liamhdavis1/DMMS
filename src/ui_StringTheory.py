# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StringTheory.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import Images_rc

class Ui_StringTheory(object):
    def setupUi(self, StringTheory):
        if not StringTheory.objectName():
            StringTheory.setObjectName(u"StringTheory")
        StringTheory.resize(742, 477)
        StringTheory.setAutoFillBackground(False)
        StringTheory.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.stackedWidget = QStackedWidget(StringTheory)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 741, 471))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.controlPage = QWidget()
        self.controlPage.setObjectName(u"controlPage")
        self.verticalLayoutWidget = QWidget(self.controlPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 741, 499))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetFixedSize)
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 40))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_14)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(15, 75, 235);\n"
"background-color: rgb(15, 75, 235);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalSpacer_10 = QSpacerItem(40, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"background-color: rgb(15, 75, 235);\n"
"selection-color: rgb(15, 75, 235);\n"
"selection-background-color: rgb(235, 235, 235);")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_12 = QSpacerItem(40, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"background-color: rgb(15, 75, 235);\n"
"selection-color: rgb(15, 75, 235);\n"
"selection-background-color: rgb(235, 235, 235);")
        self.pushButton_2.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSlider = QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximumSize(QSize(400, 16777215))
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet(u"color: rgb(15, 75, 235);\n"
"border-color: rgb(15, 75, 235);\n"
"gridline-color: rgb(15, 75, 235);")
        self.horizontalSlider.setMaximum(150)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(True)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"background-color: rgb(15, 75, 235);\n"
"selection-color: rgb(15, 75, 235);\n"
"selection-background-color: rgb(235, 235, 235);")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 30))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"background-color: rgb(15, 75, 235);\n"
"selection-color: rgb(15, 75, 235);\n"
"selection-background-color: rgb(235, 235, 235);")
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(16777215, 30))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"color: rgb(235, 235, 235);\n"
"background-color: rgb(15, 75, 235);\n"
"selection-color: rgb(15, 75, 235);\n"
"selection-background-color: rgb(235, 235, 235);")
        self.pushButton_5.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_14 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(150, 30))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMaximumSize(QSize(120, 70))
        self.graphicsView.setStyleSheet(u"border-image: url(:/UTSLogo/3016.png);")

        self.horizontalLayout_4.addWidget(self.graphicsView)

        self.horizontalSpacer_11 = QSpacerItem(40, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_17)

        self.stackedWidget.addWidget(self.controlPage)
        self.guidePage = QWidget()
        self.guidePage.setObjectName(u"guidePage")
        self.verticalLayoutWidget_2 = QWidget(self.guidePage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 742, 471))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(15, 75, 235);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalSpacer = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.label_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 120))
        self.label_11.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.verticalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(15, 75, 235);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.verticalSpacer_4)

        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 120))
        self.label_12.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.verticalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalSpacer_15 = QSpacerItem(40, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.guidePage)

        self.retranslateUi(StringTheory)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(StringTheory)
    # setupUi

    def retranslateUi(self, StringTheory):
        StringTheory.setWindowTitle(QCoreApplication.translate("StringTheory", u"Control Panel", None))
#if QT_CONFIG(tooltip)
        StringTheory.setToolTip(QCoreApplication.translate("StringTheory", u"<html><head/><body><p>String Theory</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("StringTheory", u"Control Panel", None))
        self.label_14.setText(QCoreApplication.translate("StringTheory", u"User Guide", None))
        self.pushButton.setText(QCoreApplication.translate("StringTheory", u"Connect to ESP32", None))
        self.pushButton_2.setText(QCoreApplication.translate("StringTheory", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("StringTheory", u"+", None))
        self.label_2.setText(QCoreApplication.translate("StringTheory", u"RPM: QAbstractSlider", None))
        self.pushButton_4.setText(QCoreApplication.translate("StringTheory", u"LED On", None))
        self.pushButton_5.setText(QCoreApplication.translate("StringTheory", u"LED Off", None))
        self.pushButton_6.setText(QCoreApplication.translate("StringTheory", u"STOP", None))
        self.label_9.setText(QCoreApplication.translate("StringTheory", u"Control Panel", None))
        self.label_13.setText(QCoreApplication.translate("StringTheory", u"User Guide", None))
        self.label_11.setText(QCoreApplication.translate("StringTheory", u"Connect to the string launcher by connecting to WiFi:\n"
"1. Enter WiFi settings on your device\n"
"2. Select \u201cStringTheory\u201d\n"
"3. Enter password - 12345678\n"
"", None))
        self.label_12.setText(QCoreApplication.translate("StringTheory", u"Once connected to the WiFi you are ready to get started! \n"
"1. Select connect to String Launcher in the control screen\n"
"2. Adjust the rpm using the + and \u2013 buttons. You can also use the slider\n"
"3. Turn the LED on and off using the designated buttons\n"
"4. Use the \u201cSTOP\u201d button to turn off the device\n"
"", None))
    # retranslateUi

