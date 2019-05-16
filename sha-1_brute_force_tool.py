from urllib.request import urlopen, hashlib

sha1hash = input("> Please insert the SHA-1 hash here.\n>")

common_passwords_list_url = input("> Please, also, provide the URL of the word list that you would like me to check.\n>")

common_passwords_list = urlopen(common_passwords_list_url).read()
common_passwords_list = str(common_passwords_list, 'utf-8')

#common_passwords_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for word in common_passwords_list.split('\n'):
    hashed_word = hashlib.sha1(bytes(word, 'utf-8')).hexdigest()
    if hashed_word == sha1hash:
        print(">We found the word. The password is ", str(word))
        quit()
    elif hashed_word != sha1hash:
        print("> The word ",str(word),"does not match this sha-1 hash, trying the next one...")
print("The word for the SHA-1 hash that you have inserted does not correspond toany word on the current database.")
