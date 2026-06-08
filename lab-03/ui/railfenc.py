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
        
        # --- CÁC THÀNH PHẦN GIAO DIỆN ---
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("RAIL FENCE CIPHER")
        
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
        self.label_4.setText("Key (Số hàng > 1)")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 101, 21))
        self.label_5.setText("CipherText")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 391, 91))
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 290, 371, 31))
        
        # [RÀNG BUỘC KEY]: Rail Fence cần số nguyên >= 2
        self.lineEdit.setValidator(QIntValidator(2, 99))
        self.lineEdit.setPlaceholderText("Nhập số hàng (ví dụ: 2, 3...)")
        
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

    # --- THUẬT TOÁN RAIL FENCE ---
    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1: return plain_text
        rails = [[] for _ in range(num_rails)]
        rail_idx, direction = 0, 1
        for char in plain_text:
            rails[rail_idx].append(char)
            if rail_idx == 0: direction = 1
            elif rail_idx == num_rails - 1: direction = -1
            rail_idx += direction
        return ''.join(''.join(rail) for rail in rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1: return cipher_text
        rail_lengths = [0] * num_rails
        rail_idx, direction = 0, 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_idx] += 1
            if rail_idx == 0: direction = 1
            elif rail_idx == num_rails - 1: direction = -1
            rail_idx += direction
            
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length
            
        plain_text = ""
        rail_idx, direction = 0, 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_idx].pop(0)
            if rail_idx == 0: direction = 1
            elif rail_idx == num_rails - 1: direction = -1
            rail_idx += direction
        return plain_text

    # --- XỬ LÝ SỰ KIỆN ---
    def xu_ly_ma_hoa(self):
        plain = self.textEdit.toPlainText().strip()
        key_text = self.lineEdit.text().strip()
        if not plain or not key_text:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập đủ Plaintext và Khóa!")
            return
        self.textEdit_2.setPlainText(self.rail_fence_encrypt(plain, int(key_text)))

    def xu_ly_giai_ma(self):
        cipher = self.textEdit_2.toPlainText().strip()
        key_text = self.lineEdit.text().strip()
        if not cipher or not key_text:
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập đủ Ciphertext và Khóa!")
            return
        self.textEdit.setPlainText(self.rail_fence_decrypt(cipher, int(key_text)))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())