import tkinter as tk
from tkinter import messagebox

def solo_numeros(caracter):
    return caracter.isdigit()

def validar_datos():
    nombre = entrada_nombre.get().strip()
    edad = entrada_edad.get().strip()
    sexo = opcion_sexo.get()
    correo = entrada_correo.get().strip()

    if not nombre or not edad or not sexo or not correo:
        messagebox.showwarning("Aun hay campos vacios ", "Por favor, completa todos los campos, no seas churpio.")
        return

    if "@" not in correo:
        messagebox.showwarning("Correo inválido", "El correo debe contener '@'.")
        return

    messagebox.showinfo("Datos recibidos", "¡Gracias por completar el formulario, besos vv!")

# Crear ventana
ventana = tk.Tk()
ventana.title("Formulario de Usuario")
ventana.geometry("300x300")

# Validación para entrada de edad
vcmd = (ventana.register(solo_numeros), '%S')

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana, validate="key", validatecommand=vcmd)
entrada_edad.pack()

tk.Label(ventana, text="Sexo:").pack()
opcion_sexo = tk.StringVar()
opcion_sexo.set("")  # Valor por defecto vacío
menu_sexo = tk.OptionMenu(ventana, opcion_sexo, "F", "M", "Licuadora")
menu_sexo.pack()

tk.Label(ventana, text="Correo:").pack()
entrada_correo = tk.Entry(ventana)
entrada_correo.pack()

# Botón para validar
tk.Button(ventana, text="Enviar", command=validar_datos).pack(pady=10)

# Ejecutar ventana
ventana.mainloop()