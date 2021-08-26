import pyshorteners
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('400x420')
root.resizable(False, False)
root.title('URL Shortener')
root.config(bg='black')


image = Image.open('url.png')
test = ImageTk.PhotoImage(image)
Label(image=test, bg='black').pack()

url = StringVar()
url_short = StringVar()

Label(root, text='URL Shortener', bg='black', fg='white', font='Times 20 bold').pack()
Label(root, text='(Shrey Kharbanda)', bg='black', fg='white', font='Times 12 bold').pack()


Label(root, text='Enter URL here', bg='black', fg='light pink', font='Times 16 bold').place(x=50, y=205)
Entry(root, textvariable= url, width=35, font='Times 12' ).place(x=50, y=235)

Label(root, text='URl Shortener here', bg='black', fg='light pink', font='Times 16 bold').place(x=50, y=330)
text = Entry(root, width=47, textvariable=url_short)
text.place(x = 50, y=360)

def Convert_fun():
    con_url = pyshorteners.Shortener().tinyurl.short(url.get())
    url_short.set(con_url)


Button(root, text= 'Convert', bg='#fff', fg='#000', font='Times 15 bold', command=Convert_fun).place(x=150, y=280)

root.mainloop()