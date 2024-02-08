#2.a

message = input("Enter the Encrypted Text")
message=message.upper()
ALPHABETS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(ALPHABETS)):
    trans=""
    for sy in message:
        ind=ALPHABETS.index(sy)
        ind = ind-key
        if ind<0:
            ind+=len(ALPHABETS)
        trans+=ALPHABETS[ind]
    print(f'#key:{key}:{trans}')
    