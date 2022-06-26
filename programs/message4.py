
from email import message


message4 = "Ttoleenstidhyw sst. s1e nt  a k 2 ilhotiTep3psoefhnhya4r a  a e s5itdiNts As6oo ma hlEw7r aapciaSo8idlglops r"

# The key from message 3, that defines the length of a row
key = 10

col_size = (len(message4) + key - 1) // key

decrypted = ""


for offset in range(col_size):
    while offset < len(message4):   
        decrypted += message4[offset]
        offset += col_size

print(decrypted)






