import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Función para obtener el texto actualizado y generar el PDF
def generar_pdf():
    texto = f"""One of the {entry_most.get()} conspicuous trends in todays world is the colossal upsurge IN LEARNING FOREIGN LANGUAGES and their relevancy.
                 There is a widespread worry that this will only lead to a myriad of concerns in society. This essay will {entry_discuss.get()} both advantages and disadvantages, 
                 causes, effects OF FOREIGN LANGUAGE and their relevancy using a prudent approach and lead to a logical conclusion."""
    
    # Crear el archivo PDF
    c = canvas.Canvas("modified_text.pdf", pagesize=letter)
    c.drawString(100, 750, texto)
    c.save()

    messagebox.showinfo("PDF generado", "El archivo PDF ha sido generado con éxito.")

# Crear la ventana de la aplicación
root = tk.Tk()
root.title("Modificador de texto con PDF")

# Crear las etiquetas y entradas para modificar las palabras entre llaves
tk.Label(root, text="Palabra para {most}:").grid(row=0, column=0, padx=10, pady=10)
entry_most = tk.Entry(root, width=30)
entry_most.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Palabra para {discuss}:").grid(row=1, column=0, padx=10, pady=10)
entry_discuss = tk.Entry(root, width=30)
entry_discuss.grid(row=1, column=1, padx=10, pady=10)

# Crear botón para generar el PDF
boton_pdf = tk.Button(root, text="Generar PDF", command=generar_pdf)
boton_pdf.grid(row=2, column=1, pady=20)

# Iniciar la aplicación
root.mainloop()
