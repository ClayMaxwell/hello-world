Text = input("Enter text to encrypt: ")
distance = int(input("Enter number of offset: "))
encrypted = ""
for ch in Text:
    Value = ord(ch)
    EnVal = Value + distance
    if EnVal > ord('z'):
        EnVal = ord('a') + offset - \
            (ord('z') - Value + 1)
    encrypted = encrypted + chr(EnVal)
print(encrypted)
