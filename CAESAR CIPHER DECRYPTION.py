#IMPLEMENTATION OF CAESAR CIPHER USING PYTHON
#DECRYPTION

def decryption(encrypt_msg,letters):
    k=int(input("ENTER THE KEY VALUE: "))
    ans=""
    for i in encrypt_msg:
        if i in letters:
            pos=letters.find(i)
            new_pos=(pos-k)%26
            new_char=letters[new_pos]
            ans+=new_char
        else:
            ans+=i
    return ans
encrypt_msg=input("ENTER THE ENCRYPT MESSAGE: ")
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(decryption(encrypt_msg,letters))