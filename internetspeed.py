import speedtest
from tkinter.ttk import *
from tkinter import *


root = Tk()
root.title("Internet Speed Tracker")
root.geometry('380x220')
root.resizable(False, False)
root.configure(bg="#ffffff")
root.iconbitmap('speed.ico')

# design Label
Label(root, text ='INTERNET SPEED', bg='#ffffff', fg='#404042', font = 'arial 25 bold').pack()
Label(root, text ='takes upto 30s to load...', bg='#fff', fg='#404042', font = 'arial 12 ').pack(side =BOTTOM)

# making label to show internet speed
down_label = Label(root, text="Download Speed - ", bg='#fff', font = 'arial 10 bold')
down_label.place(x = 90, y= 50)
up_label = Label(root, text="Upload Speed - ", bg='#fff', font = 'arial 10 bold')
up_label.place(x = 90, y= 80)



# function for progress bar and update text
def update_text():
    global download_speed, upload_speed
    # function for check speed
    global download_speed, upload_speed
    chk= speedtest.Speedtest()
    download= chk.download()
    upload = chk.upload()

    download_speed = round(download/(10**6), 2)
    upload_speed = round(upload / (10 ** 6), 2)
    progress=Progressbar(root, orient=HORIZONTAL,length=210, mode='indeterminate')
    progress.place(x = 85, y = 110)
    progress.start()
    down_label.config(text="Download Speed - "+str(download_speed)+"Mbps")
    up_label.config(text="Upload Speed - "+str(upload_speed)+"Mbps")

    progress.stop()
    progress.destroy()

# button for call to function
button = Button(root, text="Check Speed", width=30, bd = 0, bg = '#404042', fg='#fff', pady = 5, command=update_text)
button.place(x=85, y = 140)
root.mainloop()