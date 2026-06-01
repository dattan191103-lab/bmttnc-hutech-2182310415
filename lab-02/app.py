from flask import Flask, render_template, request, json 
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)


#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
# =====================================================================
# ROUTER FOR PLAYFAIR CIPHER
# =====================================================================
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt_route():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    obj = PlayFairCipher()
    # Thuật toán Playfair của bạn yêu cầu tạo ma trận từ key trước
    matrix = obj.create_playfair_matrix(key)
    encrypted_text = obj.playfair_encrypt(text, matrix)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt_route():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    obj = PlayFairCipher()
    matrix = obj.create_playfair_matrix(key)
    decrypted_text = obj.playfair_decrypt(text, matrix)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# =====================================================================
# ROUTER FOR RAIL FENCE CIPHER
# =====================================================================
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt_route():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    
    obj = RailFenceCipher()
    # Gọi chính xác tên hàm rail_fence_encrypt trong class của bạn
    encrypted_text = obj.rail_fence_encrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt_route():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    
    obj = RailFenceCipher()
    # Gọi chính xác tên hàm rail_fence_decrypt trong class của bạn
    decrypted_text = obj.rail_fence_decrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# =====================================================================
# ROUTER FOR VIGENERE CIPHER
# =====================================================================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt_route():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    
    obj = VigenereCipher()
    # Gọi chính xác tên hàm vigenere_encrypt trong class của bạn
    encrypted_text = obj.vigenere_encrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt_route():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    
    obj = VigenereCipher()
    # Gọi chính xác tên hàm vigenere_decrypt trong class của bạn
    decrypted_text = obj.vigenere_decrypt(text, key)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)