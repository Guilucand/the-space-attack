

message3 = "C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6 TBCxC6! WTq52T 2GCT82HT6BTJS"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !#."

offset = 43

decrypted = ""


for letter in message3:
    decrypted += alphabet[(alphabet.find(letter) + offset) % len(alphabet)]

print(decrypted)
