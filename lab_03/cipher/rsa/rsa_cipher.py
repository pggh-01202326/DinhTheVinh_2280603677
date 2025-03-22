import rsa
import os

# Đảm bảo thư mục keys tồn tại
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy đường dẫn tuyệt đối của thư mục hiện tại
KEYS_DIR = os.path.join(BASE_DIR, 'keys')

if not os.path.exists(KEYS_DIR):
    os.makedirs(KEYS_DIR)

class RSACipher:
    def generate_keys(self):
        """Generate RSA key pair and save to files."""
        (public_key, private_key) = rsa.newkeys(1024)
        with open(os.path.join(KEYS_DIR, 'publicKey.pem'), 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open(os.path.join(KEYS_DIR, 'privateKey.pem'), 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        """Load RSA key pair from files."""
        with open(os.path.join(KEYS_DIR, 'publicKey.pem'), 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open(os.path.join(KEYS_DIR, 'privateKey.pem'), 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        """Encrypt a message using the public key."""
        return rsa.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        """Decrypt a ciphertext using the private key."""
        return rsa.decrypt(ciphertext, key).decode('ascii')

    def sign(self, message, private_key):
        """Sign a message using the private key."""
        return rsa.sign(message.encode('ascii'), private_key, 'SHA-1')

    def verify(self, message, signature, public_key):
        """Verify a signature using the public key."""
        try:
            return rsa.verify(message.encode('ascii'), signature, public_key) == 'SHA-1'
        except rsa.VerificationError:
            return False