import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from soupsieve import select

from server import BUFFER_SIZE, IP_ADDRESS, SERVER

PORT = 8050
IP_ADDRESS = '192.168.1.26'
SERVER = None
BUFFER_SIZE = 4096


def openMusicWindow():

    print("\n\t\t\t\tIP MESSENGER")

   
    window=Tk()

    window.title('MUSIC WINDOW')
    window.geometry("500x350")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select A Song",bg='LightSkyBlue', font = ("Calibri",10))
    selectlabel.place(x=10, y=8)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    playButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download = Button(window, text= "Download", width=10, bd=1,bg='LightSkyBlue',font = ("Calibri",10))
    Download.place(x=200, y=250)

    infoLabel = Label(window,text="", fg="blue",font = ("Calibri",10))
    infoLabel.place(x=4,y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()
openMusicWindow()














