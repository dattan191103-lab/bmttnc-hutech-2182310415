# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/vigenere.ui'
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import os

# Ép hệ thống nhận plugin giao diện từ thư mục nội bộ dự án
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r"./platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Label Title
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Label Tên sinh viên
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        # Label Plaintext
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # Label Key
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        # Label CipherText
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        # Ô nhập văn bản gốc (Plaintext)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        # Ô nhập Khóa (Key - Dạng chữ)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 290, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        # Ô nhập/Hiển thị kết quả mã hóa (CipherText)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 380, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        
        # Nút Mã Hóa
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 530, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Nút Giải Mã
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 530, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # =====================================================================
        # KẾT NỐI SỰ KIỆN CLICK NÚT BẤM
        # =====================================================================
        self.pushButton.clicked.connect(self.xu_ly_ma_hoa)
        self.pushButton_2.clicked.connect(self.xu_ly_giai_ma)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vigenere Cipher - HUTECH"))
        self.label.setText(_translate("MainWindow", "VIGENERE CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Bui Tan Quoc Dat _ 2182310415"))
        self.label_3.setText(_translate("MainWindow", "Plaintext"))
        self.label_4.setText(_translate("MainWindow", "Key (Chuỗi chữ)"))
        self.label_5.setText(_translate("MainWindow", "CipherText"))
        self.pushButton.setText(_translate("MainWindow", "Mã Hóa"))
        self.pushButton_2.setText(_translate("MainWindow", "Giải Mã"))

    # =====================================================================
    # LOGIC THUẬT TOÁN VIGENERE (DỊCH CHUYỂN THEO KHÓA TUẦN HOÀN)
    # =====================================================================
    def vigenere_process(self, text, key, mode='encrypt'):
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Xác định điểm mốc ASCII tùy thuộc vào chữ hoa hay thường
                start = ord('A') if char.isupper() else ord('a')
                
                # Tính toán bước dịch chuyển dựa trên ký tự hiện tại của Key
                shift = ord(key[key_index % len(key)]) - ord('A')
                if mode == 'decrypt':
                    shift = -shift
                
                # Áp dụng công thức Vigenere vòng tròn 26 chữ cái
                result += chr((ord(char) - start + shift) % 26 + start)
                key_index += 1  # Chỉ tăng index của khóa khi gặp ký tự chữ hợp lệ
            else:
                result += char  # Giữ nguyên khoảng trắng và ký tự đặc biệt
        return result

    # =====================================================================
    # HÀM XỬ LÝ SỰ KIỆN GIAO DIỆN VÀ RÀNG BUỘC DỮ LIỆU
    # =====================================================================
    def xu_ly_ma_hoa(self):
        try:
            plain_text = self.textEdit.toPlainText()
            key_text = self.lineEdit.text().strip()
            
            if not plain_text:
                raise ValueError("Nội dung Plaintext không được để trống!")
            if not key_text:
                raise ValueError("Khóa (Key) không được để trống!")
            if not key_text.isalpha():
                raise ValueError("Khóa (Key) của Vigenere chỉ được chứa các ký tự chữ (A-Z, a-z)!")
                
            encrypted_text = self.vigenere_process(plain_text, key_text, mode='encrypt')
            self.textEdit_2.setPlainText(encrypted_text)
            
        except ValueError as e:
            QMessageBox.warning(None, "Lỗi Nhập Liệu", str(e))

    def xu_ly_giai_ma(self):
        try:
            cipher_text = self.textEdit_2.toPlainText()
            key_text = self.lineEdit.text().strip()
            
            if not cipher_text:
                raise ValueError("Nội dung CipherText không được để trống!")
            if not key_text:
                raise ValueError("Khóa (Key) không được để trống!")
            if not key_text.isalpha():
                raise ValueError("Khóa (Key) của Vigenere chỉ được chứa các ký tự chữ (A-Z, a-z)!")
                
            decrypted_text = self.vigenere_process(cipher_text, key_text, mode='decrypt')
            self.textEdit.setPlainText(decrypted_text)
            
        except ValueError as e:
            QMessageBox.warning(None, "Lỗi Nhập Liệu", str(e))


# =====================================================================
# HÀM KHỞI CHẠY ỨNG DỤNG (MAIN CHUẨN PYQT5)
# =====================================================================
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())