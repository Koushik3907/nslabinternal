p=7
q=11
e=7
n=p*q
phi=(p-1)*(q-1)
d = pow(e, -1, phi)
def encrypt(text):
    cipher=(text**e)%n
    print(cipher)
def decrypt(text):
    D_text=(text**d)%n
    print(D_text)

encrypt(13)
decrypt(62)