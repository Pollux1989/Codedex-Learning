import tkinter as tk
from tkinter import ttk

# Función para mostrar el menú adicional
def show_second_menu():
    # Oculta el contenido del primer menú
    first_menu_frame.pack_forget()

    # Muestra el segundo menú
    second_menu_frame.pack()

# Función para regresar al primer menú
def show_first_menu():
    # Oculta el contenido del segundo menú
    second_menu_frame.pack_forget()

    # Muestra el primer menú
    first_menu_frame.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Menú Desplegable con Tkinter")

# Crear el primer menú
first_menu_frame = tk.Frame(root)
first_menu_label = tk.Label(first_menu_frame, text="Primer Menú")
first_menu_label.pack(pady=10)
go_to_second_menu_button = tk.Button(first_menu_frame, text="Ir al Segundo Menú", command=show_second_menu)
go_to_second_menu_button.pack(pady=10)
first_menu_frame.pack(pady=20)

# Crear el segundo menú
second_menu_frame = tk.Frame(root)
second_menu_label = tk.Label(second_menu_frame, text="Segundo Menú")
second_menu_label.pack(pady=10)
go_back_button = tk.Button(second_menu_frame, text="Regresar al Primer Menú", command=show_first_menu)
go_back_button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
