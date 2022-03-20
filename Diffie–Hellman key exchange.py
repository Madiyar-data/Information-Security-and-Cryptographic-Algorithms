import time
P=19
d=2
Xa=5
Xb=7
#d mod P
Ya=(d**Xa)%P   # d^Xa mod P
Yb=(d**Xb)%P   # d^Xb mod P

Zab1=(Yb**Xa)%P    # Yb^Xa mod P
Zab2=(Ya**Xb)%P    # Ya^Xb mod P          Alice   Bob
print("Байтемиров Мадяир. Diffie–Hellman key exchange")
print("")
print("Key(pri):     Ха=",Xa,"; Хв=",Xb)
print("Key(pub):     P=",P,"; d=",d)
print("Key(partial): Уа=",Ya,"; Ув=",Yb)
print("Key(full):    Zab=",Zab1)
print("")
print("======================================================================================")
print("")
print("                                     Eva                         ")
print("                                  ========= ")
print("                                   Ya =",Ya)
print("                                   Yb =",Yb)
print("                                      ^              ")
print("Bob                                   ^                           Alice")
print("=======================               ^                     =========================")
print("Xa =",Xa,"                               ^                    ","Xb =",Xb)
print("Ya =",d,"^",Xa,"mod",P,"=",Ya,"               ^                    ","Yb =",d,"^",Xb,"mod",P,"=",Yb)
print("                      -------------------------------------")
print("Yb =",Yb,"                                                   ","Ya =",Ya)
print("Zab =",Yb,"^",Xa,"mod",P,"=",Zab1,"                                  ","Zab =",Ya,"^",Xb,"mod",P,"=",Zab1)
print("                                             ")
print("======================================================================================")
time.sleep(222)