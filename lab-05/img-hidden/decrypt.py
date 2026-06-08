import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # 1. Thu thập tất cả các bit cuối cùng từ các kênh màu của mỗi pixel
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            # Lưu ý: img.getpixel trả về tuple (R, G, B) hoặc (R, G, B, A)
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
    
    # 2. Chuyển đổi chuỗi nhị phân thành văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        char = chr(int(byte, 2))
        
        # Kiểm tra dấu hiệu kết thúc (ở đây là ký tự null '\0')
        if char == '\0':
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()