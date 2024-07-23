#IMPLEMENTATION OF CIPHER TEXT IN PYTHON
#ENCRYPTION

def encrypt_text(plain_text,n):
    ans=""
    for i in range(len(plain_text)):
        ch=plain_text[i];
        if ch==" ":
            ans+=" "
        elif ch.isupper():
            ans+=chr((ord(ch)+n-65)%26+65)
        else:
            ans+=chr((ord(ch)+n-97)%26+97)
    return ans

plain_text=input("ENTER A PLAIN TEXT: ")
n=int(input("ENTER A KEY: "))
print(encrypt_text(plain_text, n))