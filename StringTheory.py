import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtNetwork import QTcpSocket
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from src import Images_rc


class Ui_StringTheory(object):
    def __init__(self, window):
        self.setupUi(window)

        self.window = window

        # Same connection settings as your working example.
        self.esp32_ip = "192.168.4.1"
        self.esp32_port = 5000

        # Store status without adding widgets or changing the layout.
        self.connection_status = "Not connected"
        self.led_state = "Unknown"

        self.socket = QTcpSocket(window)
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.readyRead.connect(self.on_ready_read)
        self.socket.errorOccurred.connect(self.on_error)

        # These are action buttons, not toggle buttons.
        self.pushButton.setCheckable(False)
        self.pushButton_4.setCheckable(False)
        self.pushButton_5.setCheckable(False)

        # Avoid Enter automatically activating a dialog button.
        for button in (
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.pushButton_5,
            self.pushButton_6,
        ):
            button.setAutoDefault(False)
            button.setDefault(False)

        self.pushButton.clicked.connect(self.connect_to_esp32)
        self.pushButton_4.clicked.connect(self.send_led_on)
        self.pushButton_5.clicked.connect(self.send_led_off)

        # Make the existing headings clickable on BOTH pages.
        self.configure_navigation_link(
            self.label_10, "Control Panel", "control"
        )
        self.configure_navigation_link(
            self.label_14, "User Guide", "guide"
        )
        self.configure_navigation_link(
            self.label_9, "Control Panel", "control"
        )
        self.configure_navigation_link(
            self.label_13, "User Guide", "guide"
        )

        self.stackedWidget.setCurrentWidget(self.controlPage)
        self.update_status_display()

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
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 741, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)

        font = QFont()
        font.setPointSize(14)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setFixedHeight(40)
        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 40))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setFixedHeight(40)
        self.horizontalLayout_5.addWidget(self.label_14)

        self.verticalLayout.addLayout(self.horizontalLayout_5)
        # self.horizontalLayout_5 = QHBoxLayout()
        # self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        # self.label_10 = QLabel(self.verticalLayoutWidget)
        # self.label_10.setObjectName(u"label_10")
        # self.label_10.setMaximumSize(QSize(16777215, 40))
        # font = QFont()
        # font.setPointSize(14)
        # self.label_10.setFont(font)
        # self.label_10.setStyleSheet(u"color: rgb(15, 75, 235);")
        # self.label_10.setAlignment(Qt.AlignCenter)
        # self.label_10.setFixedHeight(40)

        # self.horizontalLayout_5.addWidget(self.label_10)
        # self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_5.setSpacing(0)

        # self.label_14 = QLabel(self.verticalLayoutWidget)
        # self.label_14.setObjectName(u"label_14")
        # self.label_14.setMaximumSize(QSize(16777215, 40))
        # self.label_14.setFont(font)
        # self.label_14.setStyleSheet(u"color: rgb(15, 75, 235);")
        # self.label_14.setAlignment(Qt.AlignCenter)
        # self.label_14.setFixedHeight(40)

        # self.horizontalLayout_5.addWidget(self.label_14)

        # self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(15, 75, 235);\n"
"background-color: rgb(15, 75, 235);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFixedHeight(2)

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
"color: rgb(0, 0, 0);")
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
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 741, 471))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setFixedHeight(40)
        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 40))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(15, 75, 235);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setFixedHeight(40)
        self.horizontalLayout_10.addWidget(self.label_13)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        # self.horizontalLayout_10 = QHBoxLayout()
        # self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        # self.label_9 = QLabel(self.verticalLayoutWidget_2)
        # self.label_9.setObjectName(u"label_9")
        # self.label_9.setMaximumSize(QSize(16777215, 40))
        # self.label_9.setFont(font)
        # self.label_9.setStyleSheet(u"color: rgb(15, 75, 235);")
        # self.label_9.setAlignment(Qt.AlignCenter)
        # self.label_9.setFixedHeight(40)

        # self.horizontalLayout_10.addWidget(self.label_9)
        # self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_10.setSpacing(0)
        # self.label_13 = QLabel(self.verticalLayoutWidget_2)
        # self.label_13.setObjectName(u"label_13")
        # self.label_13.setMaximumSize(QSize(16777215, 40))
        # self.label_13.setFont(font)
        # self.label_13.setStyleSheet(u"color: rgb(15, 75, 235);")
        # self.label_13.setAlignment(Qt.AlignCenter)
        # self.label_13.setFixedHeight(40)
        # self.horizontalLayout_10.addWidget(self.label_13)
        # self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color: rgb(15, 75, 235);\n"
    "background-color: rgb(15, 75, 235);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setFixedHeight(2)

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
        self.label_11.setStyleSheet(u"color: rgb(15, 75, 235);")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.verticalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color: rgb(15, 75, 235);\n"
    "background-color: rgb(15, 75, 235);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFixedHeight(2)

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
        self.label_12.setStyleSheet(u"color: rgb(15, 75, 235);")

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


    def configure_navigation_link(self, label, text, target):
        # Keep the existing label, font, alignment, and position.
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(
            f'<a href="{target}" '
            'style="color: rgb(15, 75, 235); '
            'text-decoration: none;">'
            f'{text}</a>'
        )
        label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.LinksAccessibleByKeyboard
        )
        label.setOpenExternalLinks(False)
        label.setCursor(Qt.CursorShape.PointingHandCursor)
        label.linkActivated.connect(self.navigate_to_page)

    def navigate_to_page(self, target):
        if target == "guide":
            self.stackedWidget.setCurrentWidget(self.guidePage)
        elif target == "control":
            self.stackedWidget.setCurrentWidget(self.controlPage)

    def update_status_display(self):
        # Show feedback without adding or moving any widgets.
        status = (
            f"{self.connection_status} | LED state: {self.led_state}"
        )

        self.window.setWindowTitle(f"Control Panel - {status}")

        for button in (
            self.pushButton,
            self.pushButton_4,
            self.pushButton_5,
        ):
            button.setToolTip(status)

    def connect_to_esp32(self):
        state = self.socket.state()

        if state == QTcpSocket.SocketState.ConnectedState:
            self.connection_status = "Already connected to ESP32"
            self.update_status_display()
            return

        if state != QTcpSocket.SocketState.UnconnectedState:
            self.connection_status = "Connection already in progress"
            self.update_status_display()
            return

        self.connection_status = (
            f"Connecting to {self.esp32_ip}:{self.esp32_port}..."
        )
        self.pushButton.setText("Connecting...")
        self.update_status_display()

        self.socket.connectToHost(self.esp32_ip, self.esp32_port)

    def send_led_on(self):
        self.send_command("LED_ON")

    def send_led_off(self):
        self.send_command("LED_OFF")

    def send_command(self, command):
        if (
            self.socket.state()
            != QTcpSocket.SocketState.ConnectedState
        ):
            self.connection_status = (
                "Not connected - click Connect to ESP32 first"
            )
            self.update_status_display()
            return

        written = self.socket.write(
            f"{command}\n".encode("utf-8")
        )

        if written == -1:
            self.connection_status = (
                f"Send error: {self.socket.errorString()}"
            )
        else:
            self.connection_status = (
                f"Queued {command} - awaiting ESP32 reply"
            )

        self.update_status_display()

    def on_connected(self):
        self.connection_status = "Connected to ESP32"
        self.led_state = "Unknown"
        self.pushButton.setText("Connected to ESP32")
        self.update_status_display()

    def on_disconnected(self):
        self.connection_status = "Disconnected from ESP32"
        self.led_state = "Unknown"
        self.pushButton.setText("Connect to ESP32")
        self.update_status_display()

    def on_ready_read(self):
        while self.socket.canReadLine():
            message = (
                bytes(self.socket.readLine())
                .decode("utf-8", errors="replace")
                .strip()
            )

            if message == "LED_IS_ON":
                self.led_state = "ON"
                self.connection_status = "Connected to ESP32"

            elif message == "LED_IS_OFF":
                self.led_state = "OFF"
                self.connection_status = "Connected to ESP32"

            elif message:
                self.connection_status = f"ESP32: {message}"

            self.update_status_display()

    def on_error(self, error):
        self.connection_status = (
            f"Connection error: {self.socket.errorString()}"
        )
        self.pushButton.setText("Connect to ESP32")
        self.update_status_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_StringTheory(window)

    window.show()
    sys.exit(app.exec())