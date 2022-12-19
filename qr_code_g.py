from tkinter import *
from tkinter import messagebox, filedialog, PhotoImage
import pyqrcode

# Create main window
tk = Tk()
tk.title('QR Code Generator')
bg = PhotoImage(file='images/black-paper-texture-png-1.png')
label = Label(tk, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)


# Function to generate the QR code and save it as a PNG file
def generate_qr():
    link = user_input.get()
    if link:
        global qr, img, file_path
        qr = pyqrcode.create(link)
        file_path = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                 filetypes=(("PNG files", "*.png"),))
        img = BitmapImage(data=qr.xbm(scale=10))
        qr.png(file_path, scale=6)
        display_code()
    else:
        messagebox.showwarning('warning', 'All fields are required!')


# Function to display the QR code image
def display_code():
    img_lbl.config(image=img)
    output.config(text=f"QR code of {user_input.get()} saved successfully at {file_path}")


# Create the label widget to ask the user to enter the text or URL
lbl = Label(tk,
            text='Enter Text or URL',
            bg='#606060',
            padx=10,
            pady=10,
            font=('Courier', 20),
            foreground='white')
lbl.pack()

user_input = StringVar()
entry = Entry(tk,
              textvariable=user_input,
              width=30,
              font=('ariel', 15))
entry.pack(padx=50,
           pady=30)

button = Button(tk,
                text='Generate QR code',
                width=20,
                command=generate_qr,
                font=('ariel', 15))
button.pack(padx=10,
            pady=10)

img_lbl = Label(tk, bg='#FFFFFF')
img_lbl.pack()

output = Label(tk,
               text='',
               bg='#00CC00')
output.pack()

tk.mainloop()