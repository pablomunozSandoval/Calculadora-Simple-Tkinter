from tkinter import *
raiz = Tk()

miFrame=Frame(raiz)
miFrame.pack()

operacion=""
resultado=0


#-------------Pantalla
numPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="gray",fg="black",justify="right")
#------------Presionar


def numPulsado(num):
	global operacion
	mirarPantalla=numPantalla.get()

	if operacion !="":
		numPantalla.set(num)
		operacion =""
	else:		
		numPantalla.set(mirarPantalla+num)
# solicitan el valor por medio de command 
# en el boton de la interfaz en las filas
def suma(num):
	global operacion
	global resultado

	resultado+=int(num)
	operacion="suma"
	numPantalla.set(resultado)
	
def resta(num):
	global operacion
	global resultado

	resultado-= int(num)
	operacion="resta"
	numPantalla.set(resultado)

def resultadoOperacion():
	global resultado
	numPantalla.set(resultado+int(numPantalla.get()))
	resultado=0


#------------Fila1
btn1=Button(miFrame,text="1",width=3,command=lambda:numPulsado("1"))
btn1.grid(row=2,column=1)
btn2=Button(miFrame,text="2",width=3,command=lambda:numPulsado("2"))
btn2.grid(row=2,column=2)
btn3=Button(miFrame,text="3",width=3,command=lambda:numPulsado("3"))
btn3.grid(row=2,column=3)
btnSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numPantalla.get()))
btnSuma.grid(row=2,column=4)
#------------Fila2
btn4=Button(miFrame,text="4",width=3,command=lambda:numPulsado("4"))
btn4.grid(row=3,column=1)
btn5=Button(miFrame,text="5",width=3,command=lambda:numPulsado("5"))
btn5.grid(row=3,column=2)
btn6=Button(miFrame,text="6",width=3,command=lambda:numPulsado("6"))
btn6.grid(row=3,column=3)
btnResta=Button(miFrame,text="-",width=3,command=lambda:resta(numPantalla.get()))
btnResta.grid(row=3,column=4)
#------------Fila
3btn7=Button(miFrame,text="7",width=3,command=lambda:numPulsado("7"))
btn7.grid(row=4,column=1)
btn8=Button(miFrame,text="8",width=3,command=lambda:numPulsado("8"))
btn8.grid(row=4,column=2)
btn9=Button(miFrame,text="9",width=3,command=lambda:numPulsado("9"))
btn9.grid(row=4,column=3)
btnDiv=Button(miFrame,text="/",width=3,command=lambda:numPulsado("/"))
btnDiv.grid(row=4,column=4)
#------------Fila4
btnIgual=Button(miFrame,text="=",width=3,command=lambda:resultadoOperacion(numPantalla.get()))
btnIgual.grid(row=5,column=1)
btn0=Button(miFrame,text="0",width=3,command=lambda:numPulsado("0"))
btn0.grid(row=5,column=2)
btnComa=Button(miFrame,text=",",width=3,command=lambda:numPulsado(","))
btnComa.grid(row=5,column=3)
btnMult=Button(miFrame,text="x",width=3,command=lambda:numPulsado("*"))
btnMult.grid(row=5,column=4)


raiz.mainloop()