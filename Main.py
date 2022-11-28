import sys
from  tkinter import *
from tkinter import font, messagebox
from tkinter import ttk

root = Tk()
root.title("Consecionario")
root.configure(background='#584D5F')
root.iconbitmap('Leandro.ico')
root.geometry("1280x720")


cedula = StringVar()
cat = StringVar()
preciob = DoubleVar()
totalVenta = DoubleVar()
totalComision = DoubleVar()
preciof = DoubleVar()
def Calcular():
    global totalVenta
    global totalComision
    if cat.get() == "Familiar":
        preciof.set( preciob.get() * 30/100)
        tabla.insert("", END, text=cedula.get(), values=(cat.get(), preciob.get(), round(preciof.get(), 2)))
        button2.config(state="normal")
    elif cat.get() == "4x4":
        preciof.set( preciob.get() * 40/100)
        tabla.insert("", END, text=cedula.get(), values=(cat.get(), preciob.get(), round(preciof.get(), 2)))
        button2.config(state="normal")
    elif cat.get() == "Tipo Carga":
        preciof.set( preciob.get() * 60/100)
        tabla.insert("", END, text=cedula.get(), values=(cat.get(), preciob.get(), round(preciof.get(), 2)))
        button2.config(state="normal")
    elif cedula == "":
        messagebox.showinfo(message="El campo de cedula esta vacio", title="ERROR")
    else:
        messagebox.showinfo(message="Debes seleccionar un tipo de auto", title="ERROR")
    return preciof
def limpiar():
    cedula.set("")
    cat.set("")
    preciob.set(0.00)
    preciof.set(0.00)
    button2.config(state="disable")
def exit():
    sys.exit()
texbox1 = Entry(root,width =30,textvariable = preciob)
texbox1.place(x=610, y= 60)
texbox2 = Entry(root,width =30,textvariable = cedula)
texbox2.place(x=1000, y=60)

label1 = Label(root, text="precio del vehiculo", bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label1.place(x= 600, y= 10)
label2 = Label(root, text="Tipo de vehiculo", bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label2.place(x= 600, y= 120)


label3 = Label(root, text="Inicial", bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label3.place(x= 600, y= 200)
label4 = Label(root, textvariable=preciob, bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label4.place(x=720, y= 200)
label5 = Label(root, text="Final", bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label5.place(x= 600, y= 280)
label6 = Label(root, textvariable=preciof, bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label6.place(x=720, y= 280)
label7 =Label(root, text="Cedula", bg='#584D5F',fg='black', width=0, font=("BubbleGum", 30))
label7.place(x=1000, y=10)

comboDepartamento = ttk.Combobox(root,width =50,textvariable = cat)
comboDepartamento.place(x = 600, y = 170)
comboDepartamento["values"]= ("Familiar","4x4","Tipo Carga")

imagen = PhotoImage(file="consecionario.png")
Labelimagen = Label(root, image= imagen)
Labelimagen.pack()
Labelimagen.config(width="500", height="300")
Labelimagen.place(x=50, y=20)


button1 = Button(root, text='Calcular', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= Calcular)
button1.place(x=50, y=330)
button2 = Button(root, text='Limpiar', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= limpiar)
button2.place(x=50, y=420)
button3 = Button(root, text='Salir', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= exit )
button3.place(x=50, y=510)


tabla = ttk.Treeview(root, columns =("Tipo","Inicial","Final"))
tabla.heading("#0", text="Cedula")
tabla.heading("Tipo", text="Vehiculo")
tabla.heading("Inicial", text="Inicial")
tabla.heading("Final", text="Final")
tabla.place(x=450,y=420)

root.mainloop()