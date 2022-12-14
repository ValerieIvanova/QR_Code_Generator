import pyqrcode
from tkinter import *

root = Tk()
root.title('QR Code Generator')
root.geometry('400x200')
root.config(background='black')


def generator():
    # Getting the link from the user
    link = input('Enter URL or Message: ')
    # Generate the QR code
    url = pyqrcode.create(link)
    # Creating the png file and saving it under a name that the user chose
    file_name = input('File name: ') + '.svg'
    url.svg(file_name, scale=6)
    print(f'{file_name} is saved successfully.')


generator()