from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import base64
encrypted_data = 'n5IUXOgMEsm/WXV5np1KKD7DLvKFUtN0vspe8Ox89XxrRRh+PSQa9TrCDPq8cUWS'
encrypted_bytes = base64.b64decode(encrypted_data)
def decrypt_aes_ecb(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(data)
        return decrypted.decode('ascii')
    except UnicodeDecodeError:
        return None
for pin in range(10000):
    pin_str = f"{pin:04d}"
    key = SHA256.new(pin_str.encode()).digest()
    result = decrypt_aes_ecb(key, encrypted_bytes)
    if result is not None:
        print(f"PIN: {pin_str}, Decrypted: {result}")
        break
else:
    print("No valid decryption found with any PIN.")
