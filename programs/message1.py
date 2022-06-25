
import base64


message1 = "d2VsY29tZSBldmVyeW9uZSB0byBjeWJlciwgdGhpcyBpcyB0aGUgZmlyc3Qgc3RlcCB0byBsZWFkIHlvdXIgdGVhbSB0byB3aW4="
decrypted = base64.b64decode(message1).decode('ascii')

print(decrypted)