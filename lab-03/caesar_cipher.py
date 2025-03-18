import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_Dialog # Import giao diện từ file đã chuyển đổi

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối nút bấm với API
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_encrypt.toPlainText(),
            "key": self.ui.txt_decrypt.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_Cipher.setText(data["encrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_Cipher.toPlainText(),
            "key": self.ui.txt_decrypt.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_encrypt.setText(data["decrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)
def call_api_sign(self):
    url = "http://127.0.0.1:5000/api/rsa/sign"
    payload = {
        "message": self.ui.txt_info.toPlainText(),
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            self.ui.txt_sign.setText(data["signature"])

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Signed Successfully")
            msg.exec_()
        else:
            print("Error while calling API")
    except requests.exceptions.RequestException as e:
        print("Error: %s" % e)

def call_api_verify(self):
    url = "http://127.0.0.1:5000/api/rsa/verify"
    payload = {
        "message": self.ui.txt_info.toPlainText(),
        "signature": self.ui.txt_sign.toPlainText()
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if (data["is_verified"]):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Verified Successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Verified Fail")
                msg.exec_()
        else:
            print("Error while calling API")
    except requests.exceptions.RequestException as e:
        print("Error: %s" % e)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
