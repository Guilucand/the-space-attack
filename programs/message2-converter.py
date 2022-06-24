
from english_words import english_words_set 

message3 = "C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6TBCxC6! WTq52T 2GCT82HT6BTJS"

# for word in english_words_set:
#     word = word[::-1]

#     if len(word) != 14:
#         continue
#     # if word[0] != word[-1]:
#     #     continue

#     # if word[2] != word[5]:
#     #     continue

#     # if word[3] != word[8]:
#     #     continue

#     # if word[2] != '\'':
#     #     continue
#     print(word)

# for offset in range(256):
casear = {
}

for i in range(0,256):
    casear[chr(i)] = '-'

casear['T'] = 'E'
casear['C'] = 'T'
casear['2'] = 'A'
casear['6'] = 'O'



decrypted = ""

for letter in message3:
    decrypted += casear[letter]

# print(message3)
print(decrypted)