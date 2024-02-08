def encrypt(text,key):
    A='abcdefghijklmnopqrstuvwxyz'
    text=text.lower()
    text=[A.index(char) for char in text]
    pairs=[text[i:i+2] for i in range(0,len(text),2)]
    cipher=[]
    for pair in pairs:
        
        i= [(key[0][0]*pair[0]+key[0][1]*pair[1])%26,
            (key[1][0]*pair[0]+key[1][1]*pair[1])%26]
        cipher+=i
        
    print(cipher)
    cipher_txt = "".join(A[num] for num in cipher)
    print(cipher_txt)
    
encrypt("attack", [[2,3],[3,6]])