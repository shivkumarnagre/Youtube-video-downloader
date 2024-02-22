#Importing Libraries
from tkinter import *
from pytube import YouTube

#Create Display window
root = Tk()                          #used to initialize tkinter to create display window
root.geometry('500x300')             #used to set the windows width and height
root.resizable(0,0)                  #set the fix size of window
root.title("YouTube video downloader!")

Label(root,text = "YouTube video Downloader",font = 'arial 20 bold').pack()

link = StringVar()
Label(root, text="Paste link here!", font='arial 15 bold').place(x= 160, y= 60)
link_enter = Entry(root, width=70, textvariable=link).place(x= 32, y= 90)
#textvariable used to retrieve the value of current text variable to the entry widget
#place() use to place the widget at a specific position

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root,text="Video Downloaded Successfully!", font='arial 15').place(x=180, y=210)

Button(root,text='Download', font='arial 15 bold', bg='pale violet red', padx = 2, command=downloader).place(x=180, y= 150)


root.mainloop()
