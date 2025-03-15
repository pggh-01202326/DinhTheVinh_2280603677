class RailFenceCipher:
    def __init__(self):
        pass
    
    def railfence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1 for down, -1 for up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text
    
    def railfence_decrypt(self, cipher_text, num_rails):
        rail_length = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_length[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        rail = []
        start = 0
        for length in rail_length:
            rail.append(cipher_text[start:start+length])
            start += length
        
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            plain_text += rail[rail_index][0]
            rail[rail_index] = rail[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text