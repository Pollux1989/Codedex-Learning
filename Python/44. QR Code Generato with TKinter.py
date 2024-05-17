
#print("#####--------44. QR Code Generato with TKinter--------#####")
#J-Robles 
#Python 🐍
#Visit documentation https://github.com/lincolnloop/python-qrcode for more information about the parameters in qrcode.QRCode(...).

import tkinter as tk #Interface Library
from tkinter import ttk #Separate the widget behaviour
from tkinter import filedialog #Allow to save the QR-code 
import qrcode # QR Library
from PIL import Image, ImageTk #Images stuff

def generate_qr():
    global qr_img
    #Get data from inputs
    data = entry_data.get()
    #Get QR code - I love you Codedex!!! 🥰😍😍😍😍😍
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)
    qr.add_data(data)
    qr.make()
    qr_img = qr.make_image(fill_color=combobox_color_qr.get(), back_color=combobox_color_bg.get())
    #Convert the image to format compatible  with TKinter
    qr_img = qr_img.resize((200, 200))
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    #Show image on the label
    qr_label.config(image = qr_img_tk)
    qr_label.image = qr_img_tk
    #Show Generate button again
    button_generate.config(state="normal")
    # Activate save button
    button_save.config(state="normal")

def save_qr():
    # Open the window to save the QR
    filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filepath:
        qr_img.save(filepath)

#Create the main window
root = tk.Tk() # create all window or frame ()
root.title('QR - Generator')

#Create and located widgets
label_data = ttk.Label(root, text ='Enter text and convert in QR code: ') #ttk.label Create the text to identify the data
label_data.grid(row=0, column=0, padx=5, pady=5, sticky='e') # here we add the location in the window, i was crazy undertanding what is row and column (youtube helped me a lot)

entry_data = ttk.Entry(root, width=30) ##ttk.entry call abox text
entry_data.grid(row=0, column=1, padx=5, pady=5, sticky="e")

label_color_qr = ttk.Label(root, text='Choose QR Color')
label_color_qr.grid(row=1, column=0, padx=5, pady=5)

colors = ["#FCF8FF","black", "red", "green", "blue", "yellow", "orange", "purple", "pink"] #I could'nt call the colorchooser for the color selection :(, maybe another day
combobox_color_qr = ttk.Combobox(root, values=colors, state="readonly", width=20)# add combobox
combobox_color_qr.current(0)
combobox_color_qr.grid(row=1, column=1, padx=5, pady=5)

label_color_bg = ttk.Label(root, text='Choose Background Color')
label_color_bg.grid(row=2, column=0, padx=5, pady=5)

colors = ["#FCF8FF", "black", "red", "green", "blue", "yellow", "orange", "purple", "pink"]
combobox_color_bg = ttk.Combobox(root, values=colors, state="readonly",width=20)
combobox_color_bg.current(0)
combobox_color_bg.grid(row=2, column=1, padx=5, pady=5)

button_generate = ttk.Button(root, text="Generate QR Code", command=generate_qr)# add button  and same as above
button_generate.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

button_save = ttk.Button(root, text="Save QR", command=save_qr, state="disabled")#It will be enabled when the code is generated
button_save.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

qr_label =ttk.Label(root)# Area where the QR appear
qr_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

#Start program
root.mainloop()
