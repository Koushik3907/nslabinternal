P_10_TABLE = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P_8_TABLE = [6, 3, 7, 4, 8, 5, 10, 9]
IP_TABLE = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
EP_TABLE = [4, 1, 2, 3, 2, 3, 4, 1]
P_4_TABLE = [2, 4, 3, 1]

sbox = [
    [[1, 0], [0, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 0], [0, 0]],
    [[0, 1], [1, 1], [1, 1], [0, 1]]
]

def xor(list1,list2):
    rs=[]
    for i in range(len(list1)):
        if list1[i]==list[2]:
            rs.append(0)
        else:
            rs.append(1)
    return rs

def sbox_up(bits):
    row=int(bits[0]*2+bits[3])
    col=int(bits[1]*2+bits[2])
    return sbox[row][col]

def fiestal(data,key):
    left_part=data[:4]
    right_part=data[4:]
    
    ep_right_part=[right_part[i-1]for i in EP_TABLE]
    
    xor1=xor(key,ep_right_part)
    
    sbox_output=sbox_up(xor1[4:])+sbox_up(xor1[:4])
    p4=[sbox_output[i-1] for i in P_4_TABLE]
    
    xor2=xor(p4,left_part)
    
    combined = xor2+right_part
    return combined

def key_gen(key):
    inital_key=[key[i-1] for i in P_10_TABLE]
    left_part=inital_key[:5]
    right_part=inital_key[5:]
    
    left_part=left_part[1:]+left_part[:1]
    right_part=right_part[1:]+right_part[:1]
    
    combined = left_part+right_part
    subkey1= [combined[i-1]for i in P_8_TABLE]
    left_part = left_part[2:]+left_part[:2]
    right_part=right_part[2:]+right_part[:2]
    combined=left_part+right_part
    subkey2= [combined[i-1] for i in P_8_TABLE]
    
    return (subkey1,subkey2)

def encrypt(message,key):
    subkey1,subkey2 = key_gen(key)
    inital_per=[message[i-1] for i in IP_TABLE]
    print("ip",inital_per)
    
    first_round=fiestal(inital_per,subkey1)
    second_round=fiestal(first_round[4:]+first_round[:4],subkey2)
    
    final_text=[second_round[i-1] for i in IP_INVERSE]
    print("cipher:",final_text)
    return final_text

plaintext = [1, 0, 0, 0, 0, 0, 0, 1]  
key = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0] 
final_cipher_text = encrypt(plaintext,key)

def sdes_dec(cipher, key):
  subkey1, subkey2 = key_gen(key)
  
 
  initial_permutation = [cipher[i - 1] for i in IP_TABLE]
  

  first_half = fiestal(initial_permutation, subkey2)
  second_half = fiestal(first_half[4:] + first_half[:4], subkey1)

  message = [second_half[i - 1] for i in IP_INVERSE]

  print("dct: ", message)

print("ptx: ", plaintext)
sdes_dec(final_cipher_text, key)
