from tkinter import*
import random
desplazamiento_x = random.randint(1,5)
desplazamiento_x1 = random.randint(1,5)
desplazamiento_y = 0
intervalo=5
X=700
Y=300

def jugar():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, = c.coords(carro1)
    x1, y2, =c.coords(carro2)
    if x0 < 0 or y0> X: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or x0 > Y: 
        desplazamiento_y = -desplazamiento_y
    c.move(carro1, desplazamiento_x, desplazamiento_y)
    c.move(carro2, desplazamiento_x1, desplazamiento_y)
    ventana.after(intervalo, jugar)


 

ventana=Tk()
ventana.title("carritos")
ventana.resizable(False,False)
ventana.geometry("900x500")
ventana.config(bg="black")
c = Canvas(ventana, width=X, height=Y)
c.config(bg="gray")
c.place(x=100, y=100)


carretera=c.create_rectangle(-X,Y/2,X,Y/2+20,fill="yellow")
salida=c.create_rectangle(X-600,Y,X-540,-Y,fill="black")
meta=c.create_rectangle(X-100,Y,X-170,-Y,fill="red")

img_carro1=PhotoImage(file="img/carro1.png")
carro1=c.create_image(X/2-300,Y/2-50,image=img_carro1)
img_carro2=PhotoImage(file="img/carro2.png")
carro2=c.create_image(X/2-300,Y/2+50,image=img_carro2)

s=c.create_text(X-570,Y-280,text="S",font=("Arial",30),fill="white")
a=c.create_text(X-570,Y-240,text="A",font=("Arial",30),fill="white")
l=c.create_text(X-570,Y-200,text="L",font=("Arial",30),fill="white")
i=c.create_text(X-570,Y-160,text="I",font=("Arial",30),fill="white")
d=c.create_text(X-570,Y-120,text="D",font=("Arial",30),fill="white")
a=c.create_text(X-570,Y-80,text="A",font=("Arial",30),fill="white")
boton=Button(ventana,text="jugar",command=jugar)
boton.config(bg="gray")
boton.place(x=420,y=460,)


#cuadricula




ventana.mainloop()
