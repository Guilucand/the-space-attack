from Crypto.Cipher import AES
import base64

begin = "JaAbDk1QlerxhNo8pLqS2Q=="
end = "nij8GNMQUx06N++TLehaxw=="


key = "aesEncryptionKey"

cipher = AES.new(key.encode('ascii'), AES.MODE_ECB)
decrypted_begin = cipher.decrypt(base64.b64decode(begin)).decode('ascii')
decrypted_end = cipher.decrypt(base64.b64decode(end)).decode('ascii')


print("Begin message:", decrypted_begin.strip())
print("End message:", decrypted_end.strip())