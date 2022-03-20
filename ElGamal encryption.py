from tkinter import *
p=107
g=5

#bob
cb=13
db=(g**cb)%p

m=56


#alice

k=7
r=(g**k)%p



e=(m*(db**k))%p

#bob
m1=e*(r**(p-1-cb))%p
print('                                       Eva')
print('                                  ==============')
print('                                     Db =',db)
print('                                      r =',r)
print('                                      e =',e)
print('                                       ^')
print('                                       ^')
print('                                       ^')
print('                                       ^')
print('                                       ^')
print('         Bob         ----------------------------------------           Alice')
print('=====================                                        =========================')
print('Cb =',cb,'                                                      ','k =',k)
print('Db = g^Cb mod p =',db,'                                         ','m =',m)
print('                                                               r = g^k mod p =',r)
print('                                                               e = m*Db^k mod p =',e)
print('m=(e*r^(p-1-Cb)) mod p =',m)                                          





def clicked():
    res=(int(txt.get())*(db**k))%p
    
    res1=int(res)*(r**(p-1-cb))%p
    
    lbl.configure(text='                  '+str(txt.get())+'                                     '+str(res)+'                                          '+str(res1))  
  
window = Tk()  
window.title("Протокол Эль-Гамаля")  
window.geometry('600x660')


lbl = Label(window, text='Байтемиров Мадияр ИС-32')  
lbl.grid(padx=10, pady=10)
         
txt = Entry(window,width=30)
txt.grid(column=0, row=1)

lbl = Label(window, text='p = '+str(p))  
lbl.grid(column=0, row=2)

lbl = Label(window, text='g = '+str(g))  
lbl.grid(column=0, row=3)

lbl = Label(window, text='cb = '+str(cb))  
lbl.grid(column=0, row=4)

lbl = Label(window, text='db = '+str(db))  
lbl.grid(column=0, row=5)

lbl = Label(window, text='k = '+str(k))  
lbl.grid(column=0, row=6)

lbl = Label(window, text='r = '+str(r))  
lbl.grid(column=0, row=7)

lbl = Label(window, text='e = '+str(e))  
lbl.grid(column=0, row=8)

lbl = Label(window, text='------------------------------------------------------------------------------------')  
lbl.grid(column=0, row=9)

lbl = Label(window, text='               Bob                                    Eva                                    Alice')  
lbl.grid(column=0, row=10)



lbl = Label(window, text='               ---                                    ---                                      ---')  
lbl.grid(column=0, row=11)
    
btn = Button(window, text="Зашифровать", command=clicked)  
btn.grid(padx=100, pady=50)


window.mainloop()
