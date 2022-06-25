
from Crypto.Cipher import AES
import base64

key = "password12345678"

message5 = "gCOQ6/UzLUyeLlGHRUYLqUlnGr32YknbLdVHDW5adg4AIfqpGYNTW7z78bcqRy2q+60ZwpJC2aGA3ya2XY66cw=="

cipher = AES.new(key.encode('ascii'), AES.MODE_ECB)
decrypted = cipher.decrypt(base64.b64decode(message5)).decode('ascii')


print(decrypted.strip())