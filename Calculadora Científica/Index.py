from tkinter import *
raiz = Tk()

miFrame=Frame(raiz)
miFrame.pack()


#-------------Pantalla
pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1,padx=10,pady=10)
pantalla.config(background="gray",fg="black",justify="right")
pantalla.pack(fill="x",expand=True)


#------------Teclado Numérico
btn1=Button(miFrame,text="1",width=3)
btn1=grid(row=0)
btn2=Button(miFrame,text="1",width=3)
btn3=Button(miFrame,text="1",width=3)
btn4=Button(miFrame,text="1",width=3)
btn5=Button(miFrame,text="1",width=3)
btn6=Button(miFrame,text="1",width=3)
btn7=Button(miFrame,text="1",width=3)
btn8=Button(miFrame,text="1",width=3)
btn9=Button(miFrame,text="1",width=3)
btn0=Button(miFrame,text="1",width=3)


raiz.mainloop()