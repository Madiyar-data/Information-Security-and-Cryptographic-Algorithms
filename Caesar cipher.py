import time

def encrypt_message(key,message):
       encrypted_message = ""
       for c in message:
           encrypted_message += chr(ord(c) + key)
       return encrypted_message





def decrypt_message(key, encrypted_message):
       decrypted_message = ""
       for c in encrypted_message:
           decrypted_message += chr(ord(c) - key)
       return decrypted_message


P=19
d=2
Xa=5
Xb=7          
#d mod P
Ya=(d**Xa)%P   # d^Xa mod P
Yb=(d**Xb)%P   # d^Xb mod P

Zab1=(Yb**Xa)%P    # Yb^Xa mod P
Zab2=(Ya**Xb)%P    # Ya^Xb mod P          Alice   Bob
print("Байтемиров Мадяир ИС-32")
print("")
print("Key(pri):     Ха=",Xa,"; Хв=",Xb)
print("Key(pub):     P=",P,"; d=",d)
print("Key(partial): Уа=",Ya,"; Ув=",Yb)
print("Key(full):    Zab=",Zab1)
print("")
print("==============================================================================================================================")
print("")
print("                                                         Eva                                             ")
print("                                             ========================== ")
print("                                                       Ya =",Ya)
print("                                                       Yb =",Yb)
print("                                                          ^                                  ")
print("          Bob                                                       ^                                         Alice")
print("=======================                                   ^                                         ==========================")
print("Xa =",Xa,"                                                   ^                                        ","Xb =",Xb)
print("Ya =",d,"^",Xa,"mod",P,"=",Ya,"                                   ^                                        ","Yb =",d,"^",Xb,"mod",P,"=",Yb)
print("                      -----------------------------------------------------------------------------")
print("Yb =",Yb,"                                                                                           ","Ya =",Ya)
print("Zab =",Yb,"^",Xa,"mod",P,"=",Zab1,"                                                                          ","Zab =",Ya,"^",Xb,"mod",P,"=",Zab1)
print("                                             ")
print("===============================================================================================================================")
print("")

m_encrypted = encrypt_message(Zab1,'This is a very secret message!!!')
m_decrypted = decrypt_message(Zab2, m_encrypted)
print("This is a very secret message!!!",'           ', m_encrypted,'              ', m_decrypted)
print("")
print("===============================================================================================================================")
time.sleep(222)
