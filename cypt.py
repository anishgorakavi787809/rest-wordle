from simplecrypt import encrypt, decrypt
passkey = 'wow'
str1 = 'I am okay'
cipher = encrypt(passkey, str1)
print(cipher)