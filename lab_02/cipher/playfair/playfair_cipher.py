class PlayFairCipher:
    def __init__(self) -> None:
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển J thành I trong khoá
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)  # Tạo ma trận bắt đầu từ khóa
        
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]  # Chia thành 5 cột
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        """Tìm tọa độ của ký tự trong ma trận."""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Letter '{letter}' not found in matrix.")  # Nếu không tìm thấy, ném lỗi
    
    def playfair_encrypt(self, plain_text, matrix):
        """Mã hóa văn bản theo phương pháp Playfair."""
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:  # Nếu có ký tự lẻ thì thêm 'X' vào
                pair += "X"
            try:
                row1, col1 = self.find_letter_coords(matrix, pair[0])
                row2, col2 = self.find_letter_coords(matrix, pair[1])
            except ValueError as e:
                print(f"Error: {e}")  # In lỗi nếu không tìm thấy ký tự
                continue  # Tiếp tục với cặp tiếp theo

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        """Giải mã văn bản theo phương pháp Playfair."""
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            try:
                row1, col1 = self.find_letter_coords(matrix, pair[0])
                row2, col2 = self.find_letter_coords(matrix, pair[1])
            except ValueError as e:
                print(f"Error: {e}")
                continue

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        brano = ""
        # Loại bỏ kí tự X nếu nó là kí tự cuối và là kí tự được thêm vào
        for i in range(0, len(decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                brano += decrypted_text[i]
            else:
                brano += decrypted_text[i] + decrypted_text[i+1]
                
        if decrypted_text[-1] == "X":
            brano += decrypted_text[-2]
        else:
            brano += decrypted_text[-2]
            brano += decrypted_text[-1]
        return brano
