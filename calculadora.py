import tkinter as tk

def on_click(event):
    # Función para manejar clics de botones
    current_text = entrada.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(result))
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")

    elif button_text == "C":
        entrada.delete(0, tk.END)

    else:
        entrada.insert(tk.END, button_text)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear y agregar la entrada
entrada = tk.Entry(ventana, font=("Helvetica", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Definir botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Crear y agregar los botones
for (text, row, column) in botones:
    button = tk.Button(ventana, text=text, font=("Helvetica", 14), padx=20, pady=20)
    button.grid(row=row, column=column, sticky="nsew")
    button.bind("<Button-1>", on_click)

# Configurar el sistema de rejilla para expandir dinámicamente los botones
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
