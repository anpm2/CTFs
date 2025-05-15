from Crypto.Cipher import AES
from hashlib import sha256

hostname = b'DESKTOP-NEU8R5D'
serial = '6CCF-75D6'.split('-')
key = sha256(hostname).digest()[:32]
iv = bytes.fromhex(''.join(serial*4))
cipher = AES.new(key, AES.MODE_CBC, iv)
flag = open('flag.txt', 'rb').read()
flag = cipher.decrypt(flag)
print(flag.decode())