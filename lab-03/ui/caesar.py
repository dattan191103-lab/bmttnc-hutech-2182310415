# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator
import os

# Ép hệ thống nhận plugin giao diện từ thư mục nội bộ dự án
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r"./platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # --- CÁC WIDGET GIAO DIỆN ---
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("CAESAR CIPHER")

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
        self.label_4.setGeometry(QtCore.QRect(50, 290, 51, 21))
        self.label_4.setText("Key")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 101, 21))
        self.label_5.setText("CipherText")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 391, 91))
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 290, 371, 31))
        
        # [RÀNG BUỘC CHO KEY]: Chỉ cho nhập số từ 1 đến 25
        self.validator = QIntValidator(1, 25)
        self.lineEdit.setValidator(self.validator)
        self.lineEdit.setPlaceholderText("Nhập số từ 1 - 25")
        
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

    def caesar_cipher_logic(self, text, key, mode='encrypt'):
        result = ""
        if mode == 'decrypt':
            key = -key
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - start + key) % 26 + start)
            else:
                result += char
        return result

    def xu_ly_ma_hoa(self):
        plain_text = self.textEdit.toPlainText().strip()
        key_text = self.lineEdit.text().strip()
        
        if not plain_text:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập Plaintext!")
            return
        if not key_text:
            QMessageBox.warning(None, "Cảnh báo", "Khóa không được để trống!")
            return
            
        try:
            key = int(key_text)
            if key < 1 or key > 25:
                QMessageBox.critical(None, "Lỗi", "Khóa phải nằm trong khoảng 1-25!")
                return
            encrypted_text = self.caesar_cipher_logic(plain_text, key, mode='encrypt')
            self.textEdit_2.setPlainText(encrypted_text)
        except ValueError:
            QMessageBox.critical(None, "Lỗi", "Khóa không hợp lệ!")

    def xu_ly_giai_ma(self):
        cipher_text = self.textEdit_2.toPlainText().strip()
        key_text = self.lineEdit.text().strip()
        
        if not cipher_text:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập Ciphertext!")
            return
        if not key_text:
            QMessageBox.warning(None, "Cảnh báo", "Khóa không được để trống!")
            return

        try:
            key = int(key_text)
            if key < 1 or key > 25:
                QMessageBox.critical(None, "Lỗi", "Khóa phải nằm trong khoảng 1-25!")
                return
            decrypted_text = self.caesar_cipher_logic(cipher_text, key, mode='decrypt')
            self.textEdit.setPlainText(decrypted_text)
        except ValueError:
            QMessageBox.critical(None, "Lỗi", "Khóa không hợp lệ!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())