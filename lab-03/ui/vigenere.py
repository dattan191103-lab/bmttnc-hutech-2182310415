# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import os

# Ép hệ thống nhận plugin giao diện từ thư mục nội bộ dự án
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r"./platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # --- CÁC THÀNH PHẦN GIAO DIỆN ---
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("VIGENERE CIPHER")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setText("Bui Tan Quoc Dat _ 2182310415")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 81, 21))
        self.label_3.setText("Plaintext")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 150, 21))
        self.label_4.setText("Key (Chuỗi chữ)")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 101, 21))
        self.label_5.setText("CipherText")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 391, 91))
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 290, 371, 31))
        
        # [RÀNG BUỘC KEY]: Vigenere cần khóa là chữ cái
        regex = QRegExp("[a-zA-Z]+")
        self.lineEdit.setValidator(QRegExpValidator(regex))
        self.lineEdit.setPlaceholderText("Nhập khóa là chữ cái (A-Z)")
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 380, 391, 111))
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 530, 100, 35))
        self.pushButton.setText("Mã Hóa")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 530, 100, 35))
        self.pushButton_2.setText("Giải Mã")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Kết nối sự kiện
        self.pushButton.clicked.connect(self.xu_ly_ma_hoa)
        self.pushButton_2.clicked.connect(self.xu_ly_giai_ma)

    # --- THUẬT TOÁN VIGENERE ---
    def vigenere_process(self, text, key, mode='encrypt'):
        result = ""
        key = key.upper()
        key_index = 0
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shift = ord(key[key_index % len(key)]) - ord('A')
                if mode == 'decrypt': shift = -shift
                result += chr((ord(char) - start + shift) % 26 + start)
                key_index += 1
            else:
                result += char
        return result

    # --- XỬ LÝ SỰ KIỆN ---
    def xu_ly_ma_hoa(self):
        plain = self.textEdit.toPlainText().strip()
        key = self.lineEdit.text().strip()
        if not plain or not key:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập đủ Plaintext và Khóa!")
            return
        self.textEdit_2.setPlainText(self.vigenere_process(plain, key, mode='encrypt'))

    def xu_ly_giai_ma(self):
        cipher = self.textEdit_2.toPlainText().strip()
        key = self.lineEdit.text().strip()
        if not cipher or not key:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập đủ Ciphertext và Khóa!")
            return
        self.textEdit.setPlainText(self.vigenere_process(cipher, key, mode='decrypt'))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())