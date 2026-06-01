# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/playfair.ui'
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
        self.label.setGeometry(QtCore.QRect(280, 60, 331, 51))
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
        
        # Ô nhập Plaintext
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        # Ô nhập Khóa (Key)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 290, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        # Ô nhập/Hiển thị CipherText
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 380, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        
        # Nút Mã hóa
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 530, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Nút Giải mã
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
        # KẾT NỐI SỰ KIỆN BẤM NÚT
        # =====================================================================
        self.pushButton.clicked.connect(self.xu_ly_ma_hoa)
        self.pushButton_2.clicked.connect(self.xu_ly_giai_ma)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playfair Cipher - HUTECH"))
        self.label.setText(_translate("MainWindow", "PLAYFAIR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Bui Tan Quoc Dat _ 2182310415"))
        self.label_3.setText(_translate("MainWindow", "Plaintext"))
        self.label_4.setText(_translate("MainWindow", "Key"))
        self.label_5.setText(_translate("MainWindow", "CipherText"))
        self.pushButton.setText(_translate("MainWindow", "Mã Hóa"))
        self.pushButton_2.setText(_translate("MainWindow", "Giải Mã"))

    # =====================================================================
    # LOGIC THUẬT TOÁN PLAYFAIR CIPHER (MA TRẬN 5x5)
    # =====================================================================
    def chuan_hoa_chuoi(self, text):
        """Giữ lại ký tự chữ, chuyển thành viết hoa và đổi J thành I"""
        res = ""
        for char in text.upper():
            if char.isalpha():
                res += 'I' if char == 'J' else char
        return res

    def tao_ma_tran_playfair(self, key):
        """Khởi tạo ma trận 5x5 từ khóa nhập vào"""
        key_clean = self.chuan_hoa_chuoi(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không có J
        
        matrix_chars = []
        # Điền các ký tự của khóa trước (không trùng nhau)
        for char in key_clean:
            if char not in matrix_chars:
                matrix_chars.append(char)
        # Điền các chữ cái còn lại trong bảng chữ cái
        for char in alphabet:
            if char not in matrix_chars:
                matrix_chars.append(char)
                
        # Cắt mảng thành ma trận 2 chiều 5x5
        return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

    def tim_toa_do(self, matrix, char):
        """Tìm vị trí dòng (row) và cột (col) của một chữ cái trong ma trận"""
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c
        return 0, 0

    def playfair_process(self, text, key, mode='encrypt'):
        matrix = self.tao_ma_tran_playfair(key)
        text_clean = self.chuan_hoa_chuoi(text)
        
        # Xử lý chuẩn bị các cặp ký tự cho quá trình mã hóa
        prepared_text = ""
        if mode == 'encrypt':
            i = 0
            while i < len(text_clean):
                char1 = text_clean[i]
                char2 = ""
                if i + 1 < len(text_clean):
                    char2 = text_clean[i+1]
                    if char1 == char2:  # Nếu 2 chữ liên tiếp trùng nhau thì đệm 'X' vào giữa
                        char2 = 'X'
                        i -= 1
                else:
                    char2 = 'X'  # Nếu lẻ chữ ở cuối thì đệm 'X'
                prepared_text += char1 + char2
                i += 2
        else:
            prepared_text = text_clean

        # Tiến hành dịch chuyển tọa độ ma trận
        result_text = ""
        step = 1 if mode == 'encrypt' else -1
        
        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i+1]
            r1, c1 = self.tim_toa_do(matrix, char1)
            r2, c2 = self.tim_toa_do(matrix, char2)
            
            if r1 == r2:  # Cùng hàng -> dịch ngang vòng tròn
                result_text += matrix[r1][(c1 + step) % 5]
                result_text += matrix[r2][(c2 + step) % 5]
            elif c1 == c2:  # Cùng cột -> dịch dọc vòng tròn
                result_text += matrix[(r1 + step) % 5][c1]
                result_text += matrix[(r2 + step) % 5][c2]
            else:  # Khác hàng khác cột (Hình chữ nhật) -> Tráo đổi cột chéo
                result_text += matrix[r1][c2]
                result_text += matrix[r2][c1]

        # Xử lý hậu kỳ cho chuỗi giải mã (Xóa đệm X và đưa về chữ thường)
        if mode == 'decrypt':
            ban_ro = ""
            idx = 0
            while idx < len(result_text):
                # Khôi phục các cặp bị chèn 'X' ở giữa các chữ trùng lặp cũ
                if idx + 2 < len(result_text) and result_text[idx+1] == 'X' and result_text[idx] == result_text[idx+2]:
                    ban_ro += result_text[idx]
                    idx += 1
                else:
                    ban_ro += result_text[idx]
                idx += 1
            # Loại bỏ X thừa ở cuối nếu có
            if ban_ro.endswith('X'):
                ban_ro = ban_ro[:-1]
            return ban_ro.lower()
            
        return result_text

    # =====================================================================
    # HÀM XỬ LÝ SỰ KIỆN GIAO DIỆN
    # =====================================================================
    def xu_ly_ma_hoa(self):
        try:
            plain_text = self.textEdit.toPlainText().strip()
            key_text = self.lineEdit.text().strip()
            
            if not plain_text:
                raise ValueError("Vui lòng điền nội dung Plaintext cần mã hóa!")
            if not key_text:
                raise ValueError("Khóa (Key) không được phép để trống!")
                
            cipher_text = self.playfair_process(plain_text, key_text, mode='encrypt')
            self.textEdit_2.setPlainText(cipher_text)
            
        except ValueError as e:
            QMessageBox.warning(None, "Thông báo lỗi", str(e))

    def xu_ly_giai_ma(self):
        try:
            cipher_text = self.textEdit_2.toPlainText().strip()
            key_text = self.lineEdit.text().strip()
            
            if not cipher_text:
                raise ValueError("Vui lòng điền nội dung CipherText cần giải mã!")
            if not key_text:
                raise ValueError("Khóa (Key) không được phép để trống!")
                
            plain_text = self.playfair_process(cipher_text, key_text, mode='decrypt')
            self.textEdit.setPlainText(plain_text)
            
        except ValueError as e:
            QMessageBox.warning(None, "Thông báo lỗi", str(e))


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