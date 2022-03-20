a=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107]
ads=list(range(2,1000))
for i in a:
    for u in range(1,1000):
        if u%i==0:
            if u in ads:
                ads.pop(ads.index(u))
a=ads+a




from tkinter import *
m=19
p=13
q=29
n=p*q
f=(p-1)*(q-1)
for i in a:
    if i<n and 1<i and i<f and n%i!=0:
        e=i
e=5

for i in range(0,1000000):
    if (i*e)%f==1:
        d=i
        break
print('p =',p)
print('q =',q)
print('n = p*q =',n)
print('f = (p-1)*(q-1) =',f)
print('e =',e)
print('d =',d)
c=(m**e)%n
m1=(c**d)%n
print('')
print('')
print('')


print('         Bob         ----------------------------------------           Alice')
print('=====================                                        =========================')
print('e =',e,'                                                      ')
print('                                                                m =',m)
print('                                                               c = m^e mod n =',c)
print('m = c^d mod n =',m1,'                                         ')




#shifr=(info**e)%n
#deshifr=(shifr**d)%n
      
  
def clicked():
    res=(int(txt.get())**e)%n
    info=int(txt.get())
    res1=(int(res)**d)%n
    deinfo=int(txt.get())
    lbl.configure(text='                  '+str(txt.get())+'                                     '+str(res)+'                                          '+str(res1))  
  
window = Tk()  
window.title("Шифратор RSA")  
window.geometry('600x660')


lbl = Label(window, text='Байтемиров Мадияр. Пример Шифра RSA')  
lbl.grid(padx=10, pady=10)
         
txt = Entry(window,width=30)
txt.grid(column=0, row=1)

lbl = Label(window, text='p = '+str(p))  
lbl.grid(column=0, row=2)

lbl = Label(window, text='q = '+str(q))  
lbl.grid(column=0, row=3)

lbl = Label(window, text='n = '+str(n))  
lbl.grid(column=0, row=4)

lbl = Label(window, text='f = '+str(f))  
lbl.grid(column=0, row=5)

lbl = Label(window, text='e = '+str(e))  
lbl.grid(column=0, row=6)

lbl = Label(window, text='d = '+str(d))  
lbl.grid(column=0, row=7)

lbl = Label(window, text='------------------------------------------------------------------------------------')  
lbl.grid(column=0, row=8)

lbl = Label(window, text='               Bob                                    Eva                                    Alice')  
lbl.grid(column=0, row=9)



lbl = Label(window, text='               ---                                    ---                                      ---')  
lbl.grid(column=0, row=10)
    
btn = Button(window, text="Зашифровать", command=clicked)  
btn.grid(padx=100, pady=50)


window.mainloop()

# Запускаем постоянный цикл, чтобы программа работала
#(d*e)%f=1


'''#print(2**128)
info=19

p=7
q=17
n=p*q
f=(p-1)*(q-1)
for i in a:
    if i<n and 1<i and i<f and n%i!=0:
        e=i
        
e=5############################################################

for i in range(0,10000):
    if (i*e)%f==1:
        d=i
        break


shifr=(info**e)%n
deshifr=(shifr**d)%n
print('p =',p)
print('q =',q)
print('n =',n)
print('f =',f)
print('e =',e)
print('d =',d)
print(shifr)
print(deshifr)

while e1 != 0 and f1 != 0:
    if e1 > f1:
        e1 = e1 % f1
    else:
        f1 = f1 % e1
print(e1 + f1)'''
