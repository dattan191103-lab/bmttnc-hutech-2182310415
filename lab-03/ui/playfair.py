# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import os

# Ép hệ thống nhận plugin giao diện từ thư mục nội bộ
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r"./platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # --- CÁC THÀNH PHẦN GIAO DIỆN ---
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("PLAYFAIR CIPHER")

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
        
        # [RÀNG BUỘC KEY]: Chỉ cho phép nhập chữ cái A-Z
        regex = QRegExp("[a-zA-Z]+")
        self.lineEdit.setValidator(QRegExpValidator(regex))
        self.lineEdit.setPlaceholderText("Nhập khóa (chỉ chữ cái)")
        
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

    # --- THUẬT TOÁN PLAYFAIR ---
    def chuan_hoa_chuoi(self, text):
        res = ""
        for char in text.upper():
            if char.isalpha():
                res += 'I' if char == 'J' else char
        return res

    def tao_ma_tran_playfair(self, key):
        key_clean = self.chuan_hoa_chuoi(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix_chars = []
        for char in key_clean:
            if char not in matrix_chars: matrix_chars.append(char)
        for char in alphabet:
            if char not in matrix_chars: matrix_chars.append(char)
        return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

    def tim_toa_do(self, matrix, char):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char: return r, c
        return 0, 0

    def playfair_process(self, text, key, mode='encrypt'):
        matrix = self.tao_ma_tran_playfair(key)
        text_clean = self.chuan_hoa_chuoi(text)
        prepared_text = ""
        if mode == 'encrypt':
            i = 0
            while i < len(text_clean):
                char1 = text_clean[i]
                char2 = text_clean[i+1] if i + 1 < len(text_clean) else 'X'
                if char1 == char2:
                    char2 = 'X'
                    i -= 1
                prepared_text += char1 + char2
                i += 2
        else: prepared_text = text_clean
        
        result_text = ""
        step = 1 if mode == 'encrypt' else -1
        for i in range(0, len(prepared_text), 2):
            c1, c2 = prepared_text[i], prepared_text[i+1]
            r1, col1 = self.tim_toa_do(matrix, c1)
            r2, col2 = self.tim_toa_do(matrix, c2)
            if r1 == r2:
                result_text += matrix[r1][(col1 + step) % 5] + matrix[r2][(col2 + step) % 5]
            elif col1 == col2:
                result_text += matrix[(r1 + step) % 5][col1] + matrix[(r2 + step) % 5][col2]
            else:
                result_text += matrix[r1][col2] + matrix[r2][col1]
        return result_text.lower() if mode == 'decrypt' else result_text

    # --- XỬ LÝ SỰ KIỆN ---
    def xu_ly_ma_hoa(self):
        plain = self.textEdit.toPlainText().strip()
        key = self.lineEdit.text().strip()
        if not plain or not key:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập đủ Plaintext và Khóa!")
            return
        self.textEdit_2.setPlainText(self.playfair_process(plain, key, mode='encrypt'))

    def xu_ly_giai_ma(self):
        cipher = self.textEdit_2.toPlainText().strip()
        key = self.lineEdit.text().strip()
        if not cipher or not key:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập đủ Ciphertext và Khóa!")
            return
        self.textEdit.setPlainText(self.playfair_process(cipher, key, mode='decrypt'))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())