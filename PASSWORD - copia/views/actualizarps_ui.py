# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizarps.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import ui_files.resources_rc as resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(349, 451)
        Form.setMinimumSize(QSize(100, 200))
        Form.setMaximumSize(QSize(1666666, 166666))
        Form.setSizeIncrement(QSize(0, 0))
        Form.setBaseSize(QSize(0, 0))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #57b1e6;\n"
"}\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(Form)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.background_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"color:black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color:black;\n"
"border: 1px solid  #0055ff; \n"
"border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_pushButton = QPushButton(self.content_frame)
        self.img_pushButton.setObjectName(u"img_pushButton")
        self.img_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.img_pushButton.setAutoFillBackground(False)
        self.img_pushButton.setStyleSheet(u"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/iconos/assets/iconos/ambienteslogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.img_pushButton.setIcon(icon)
        self.img_pushButton.setIconSize(QSize(150, 150))

        self.verticalLayout.addWidget(self.img_pushButton)

        self.titulo_label = QLabel(self.content_frame)
        self.titulo_label.setObjectName(u"titulo_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo_label.sizePolicy().hasHeightForWidth())
        self.titulo_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Myanmar Text 12"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.titulo_label.setFont(font)
        self.titulo_label.setAutoFillBackground(False)
        self.titulo_label.setStyleSheet(u"font:  20pt \"Myanmar Text\" bold;\n"
"color: #00003d;")
        self.titulo_label.setScaledContents(False)
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.titulo_label)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.passwactual_label_2 = QLabel(self.content_frame)
        self.passwactual_label_2.setObjectName(u"passwactual_label_2")
        font1 = QFont()
        font1.setFamilies([u"Myanmar Text 12"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.passwactual_label_2.setFont(font1)
        self.passwactual_label_2.setAutoFillBackground(False)
        self.passwactual_label_2.setStyleSheet(u"")
        self.passwactual_label_2.setScaledContents(False)
        self.passwactual_label_2.setAlignment(Qt.AlignCenter)
        self.passwactual_label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.passwactual_label_2)

        self.campopssact_lineEdit = QLineEdit(self.content_frame)
        self.campopssact_lineEdit.setObjectName(u"campopssact_lineEdit")
        self.campopssact_lineEdit.setAutoFillBackground(False)
        self.campopssact_lineEdit.setStyleSheet(u"")
        self.campopssact_lineEdit.setEchoMode(QLineEdit.Password)
        self.campopssact_lineEdit.setDragEnabled(False)
        self.campopssact_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.campopssact_lineEdit.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.campopssact_lineEdit)


        self.formLayout_4.setLayout(0, QFormLayout.SpanningRole, self.formLayout)

        self.alerta1_label = QLabel(self.content_frame)
        self.alerta1_label.setObjectName(u"alerta1_label")
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(7)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.alerta1_label.setFont(font2)
        self.alerta1_label.setStyleSheet(u"QLabel{\n"
"	font: 75 7pt \"MS Shell Dlg 2\";\n"
"	text-decoration: underline;\n"
"color:red;}")
        self.alerta1_label.setMargin(0)
        self.alerta1_label.setIndent(-1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.alerta1_label)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(7)
        self.formLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.passwnew_label_3 = QLabel(self.content_frame)
        self.passwnew_label_3.setObjectName(u"passwnew_label_3")
        self.passwnew_label_3.setFont(font1)
        self.passwnew_label_3.setAutoFillBackground(False)
        self.passwnew_label_3.setStyleSheet(u"")
        self.passwnew_label_3.setScaledContents(False)
        self.passwnew_label_3.setAlignment(Qt.AlignCenter)
        self.passwnew_label_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.passwnew_label_3)

        self.campopssnew_lineEdit = QLineEdit(self.content_frame)
        self.campopssnew_lineEdit.setObjectName(u"campopssnew_lineEdit")
        self.campopssnew_lineEdit.setAutoFillBackground(False)
        self.campopssnew_lineEdit.setStyleSheet(u"")
        self.campopssnew_lineEdit.setEchoMode(QLineEdit.Password)
        self.campopssnew_lineEdit.setDragEnabled(False)
        self.campopssnew_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.campopssnew_lineEdit.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.campopssnew_lineEdit)


        self.formLayout_4.setLayout(2, QFormLayout.SpanningRole, self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(7)
        self.formLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.passwnewconf_label_4 = QLabel(self.content_frame)
        self.passwnewconf_label_4.setObjectName(u"passwnewconf_label_4")
        self.passwnewconf_label_4.setFont(font1)
        self.passwnewconf_label_4.setAutoFillBackground(False)
        self.passwnewconf_label_4.setStyleSheet(u"")
        self.passwnewconf_label_4.setScaledContents(False)
        self.passwnewconf_label_4.setAlignment(Qt.AlignCenter)
        self.passwnewconf_label_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.passwnewconf_label_4)

        self.campopssnewconf_lineEdit = QLineEdit(self.content_frame)
        self.campopssnewconf_lineEdit.setObjectName(u"campopssnewconf_lineEdit")
        self.campopssnewconf_lineEdit.setAutoFillBackground(False)
        self.campopssnewconf_lineEdit.setStyleSheet(u"")
        self.campopssnewconf_lineEdit.setEchoMode(QLineEdit.Password)
        self.campopssnewconf_lineEdit.setDragEnabled(False)
        self.campopssnewconf_lineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.campopssnewconf_lineEdit.setClearButtonEnabled(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.campopssnewconf_lineEdit)


        self.formLayout_4.setLayout(3, QFormLayout.SpanningRole, self.formLayout_3)

        self.alerta2_label = QLabel(self.content_frame)
        self.alerta2_label.setObjectName(u"alerta2_label")
        self.alerta2_label.setStyleSheet(u"QLabel{\n"
"	font: 75 7pt \"MS Shell Dlg 2\";\n"
"	text-decoration: underline;\n"
"color:red;}")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.alerta2_label)


        self.verticalLayout.addLayout(self.formLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_actualizar = QPushButton(self.content_frame)
        self.pushButton_actualizar.setObjectName(u"pushButton_actualizar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.pushButton_actualizar.sizePolicy().hasHeightForWidth())
        self.pushButton_actualizar.setSizePolicy(sizePolicy1)
        self.pushButton_actualizar.setSizeIncrement(QSize(10, 4))
        font3 = QFont()
        font3.setFamilies([u"MS Reference Sans Serif"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.pushButton_actualizar.setFont(font3)
        self.pushButton_actualizar.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_actualizar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/iconos/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_actualizar.setIcon(icon1)
        self.pushButton_actualizar.setIconSize(QSize(19, 19))

        self.horizontalLayout.addWidget(self.pushButton_actualizar)

        self.pushButton_cancelar = QPushButton(self.content_frame)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        sizePolicy1.setHeightForWidth(self.pushButton_cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_cancelar.setSizePolicy(sizePolicy1)
        self.pushButton_cancelar.setSizeIncrement(QSize(10, 4))
        self.pushButton_cancelar.setBaseSize(QSize(0, 0))
        self.pushButton_cancelar.setFont(font3)
        self.pushButton_cancelar.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton_cancelar.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_cancelar.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/iconos/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_cancelar.setIcon(icon2)
        self.pushButton_cancelar.setIconSize(QSize(19, 19))

        self.horizontalLayout.addWidget(self.pushButton_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.content_frame)


        self.verticalLayout_5.addWidget(self.background_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.img_pushButton.setText("")
        self.titulo_label.setText(QCoreApplication.translate("Form", u"CAMBIO DE CLAVE", None))
        self.passwactual_label_2.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a Actual:", None))
#if QT_CONFIG(tooltip)
        self.campopssact_lineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alerta1_label.setText("")
        self.passwnew_label_3.setText(QCoreApplication.translate("Form", u"Nueva Contrase\u00f1a:", None))
#if QT_CONFIG(tooltip)
        self.campopssnew_lineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.passwnewconf_label_4.setText(QCoreApplication.translate("Form", u"Confirmar Contrase\u00f1a:", None))
#if QT_CONFIG(tooltip)
        self.campopssnewconf_lineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alerta2_label.setText("")
        self.pushButton_actualizar.setText(QCoreApplication.translate("Form", u"ACTUALIZAR", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("Form", u"CANCELAR", None))
    # retranslateUi

