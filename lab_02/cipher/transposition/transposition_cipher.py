class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        # Bước 1: Tạo mảng rỗng cho các hàng (với số hàng = len(text) // key)
        num_of_rows = len(text) // key
        num_of_extra_chars = len(text) % key  # Các ký tự thừa ở cột đầu
        decrypted_text = [''] * num_of_rows
        
        col = 0
        row = 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            # Kiểm tra nếu cột đã đầy hoặc nếu có ký tự thừa
            if (row == num_of_rows and col < num_of_extra_chars):
                row = 0
                col += 1
            if row == num_of_rows:  # Cột đã đầy, chuyển qua cột tiếp theo
                row = 0
                col += 1
                
        return ''.join(decrypted_text)
