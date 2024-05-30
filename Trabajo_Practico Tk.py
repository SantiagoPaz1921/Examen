#CONSIGNA 1
import tkinter as tk
def incrementar():
    valor_actual = int(label["text"])
    label.config(text=str(valor_actual + 1))
def decrementar():
    valor_actual = int(label["text"])
    label.config(text=str(valor_actual - 1))
ventana = tk.Tk()
ventana.title("Contador")
label = tk.Label(ventana, text="0", font=("Arial", 20))
label.pack(pady=20)
boton_incrementar = tk.Button(ventana, text="Incrementar", command=incrementar)
boton_incrementar.pack(side="left", padx=20)
boton_decrementar = tk.Button(ventana, text="Decrementar", command=decrementar)
boton_decrementar.pack(side="right", padx=20)
ventana.mainloop()
#CONSIGNA 2
import tkinter as tk
from tkinter import messagebox
def sumar():
    try:
        numero1 = float(entry1.get())
        numero2 = float(entry2.get())
        suma = numero1 + numero2
        label_resultado.config(text=f"Suma: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")
ventana = tk.Tk()
ventana.title("Sumador de Números")
label1 = tk.Label(ventana, text="Número 1:")
label1.pack(pady=5)
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)
label2 = tk.Label(ventana, text="Número 2:")
label2.pack(pady=5)
entry2 = tk.Entry(ventana)
entry2.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=10)
label_resultado = tk.Label(ventana, text="Suma: ")
label_resultado.pack(pady=20)
ventana.mainloop()
#CONSIGNA 3
import tkinter as tk
def verificar_credenciales():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    if usuario == "juan" and clave == "abc123":
        ventana.title("Correcto")
    else:
        ventana.title("Incorrecto")
ventana = tk.Tk()
ventana.title("Verificación de Usuario")
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)
label_clave = tk.Label(ventana, text="Clave:")
label_clave.pack(pady=5)
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack(pady=5)
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_credenciales)
boton_verificar.pack(pady=10)
ventana.mainloop()
#CONSIGNA 4
import tkinter as tk
ventana = tk.Tk()
ventana.title("Suma/Resta")
ventana.geometry("300x150")
num1 = tk.StringVar()
num2 = tk.StringVar()
operacion = tk.StringVar()
resultado = tk.StringVar()
etiqueta_num1 = tk.Label(ventana, text="Número 1:")
etiqueta_num1.grid(row=0, column=0)
campo_num1 = tk.Entry(ventana, textvariable=num1)
campo_num1.grid(row=0, column=1)
etiqueta_num2 = tk.Label(ventana, text="Número 2:")
etiqueta_num2.grid(row=1, column=0)
campo_num2 = tk.Entry(ventana, textvariable=num2)
campo_num2.grid(row=1, column=1)
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.grid(row=2, columnspan=2)
radio_suma = tk.Radiobutton(ventana, text="Sumar", variable=operacion, value="+")
radio_suma.grid(row=3, column=0)
radio_resta = tk.Radiobutton(ventana, text="Restar", variable=operacion, value="-")
radio_resta.grid(row=3, column=1)
def realizar_operacion():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        op = operacion.get()

        if op == "+":
            r = n1 + n2
        elif op == "-":
            r = n1 - n2
        else:
            r = "Operación no válida"

        resultado.set(r)
    except ValueError:
        resultado.set("Error: Ingrese números válidos")
boton_RESULTADO = tk.Button(ventana, text="RESULTADO", command=realizar_operacion)
boton_RESULTADO.grid(row=4, columnspan=2)
ventana.mainloop()
#CONSIGNA 5
import tkinter as tk
def mostrar_seleccionados():
    cantidad = 0
    if var_python.get():
        cantidad += 1
    if var_java.get():
        cantidad += 1
    if var_javascript.get():
        cantidad += 1
    label_resultado.config(text=f"Cantidad de seleccionados: {cantidad}")
ventana = tk.Tk()
ventana.title("Lenguajes de Programación")
var_python = tk.BooleanVar()
check_python = tk.Checkbutton(ventana, text="Python", variable=var_python)
check_python.pack(pady=5)
var_java = tk.BooleanVar()
check_java = tk.Checkbutton(ventana, text="JavaScript", variable=var_java)
check_java.pack(pady=5)
var_javascript = tk.BooleanVar()
check_javascript = tk.Checkbutton(ventana, text="JavaScript", variable=var_javascript)
check_javascript.pack(pady=5)
boton_mostrar = tk.Button(ventana, text="Mostrar Seleccionados", command=mostrar_seleccionados)
boton_mostrar.pack(pady=10)
label_resultado = tk.Label(ventana, text="Cantidad de seleccionados: 0")
label_resultado.pack(pady=20)
ventana.mainloop()
#CONSIGNA 6
import tkinter as tk
ventana = tk.Tk()
ventana.title("Navegadores Web")
ventana.geometry("400x300")
navegadores = ["Chrome", "Firefox", "Edge", "Safari", "Opera"]
navegadores_seleccionados = []
def actualizar_titulo():
    titulo = "Navegadores Web: " + ", ".join(navegadores_seleccionados)
    ventana.title(titulo)
def seleccionar_navegador(nombre_navegador):
    if nombre_navegador in navegadores_seleccionados:
        navegadores_seleccionados.remove(nombre_navegador)
    else:
        navegadores_seleccionados.append(nombre_navegador)
    actualizar_titulo()
for i, navegador in enumerate(navegadores):
    checkbox = tk.Checkbutton(ventana, text=navegador, variable=tk.IntVar(), command=lambda nombre=navegador: seleccionar_navegador(nombre))
    checkbox.grid(row=i, column=0, sticky=tk.W)
ventana.mainloop()





