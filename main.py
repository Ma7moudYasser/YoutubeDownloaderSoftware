from tkinter import filedialog
from tkinter import messagebox
import pytube
from tkinter import *
import os


window = Tk()
window.geometry('1000x500+100+30')
window.config(background='#F9440B')
window.resizable(False, False)
window.title('Welcome to youtube downloader')
window.iconbitmap('images/youtube.ico')

def youtube_download():
    download1 = En1.get()
    url = En2.get()
    video_instance = pytube.YouTube(url)
    stream = video_instance.streams.get_highest_resolution()
    stream.download(download1)
    if stream:
        messagebox.showinfo('Downloading', 'the download is finished')





label1 = Label(master=window, text= 'Your desired download location', font=('Arial', 15, 'bold'), bg='#F9440B')
label1.place(x=10, y=20)

En1 = Entry(master=window, font = ('times new roman', 16), width = 50, bd = 1, relief = SOLID)
En1.place(x=320, y=20)

label2 = Label(master=window, text='Enter the url of the video you want to download', font=('Arial', 15, 'bold'), bg='#F9440B')
label2.place(x=10, y=100)


En2 = Entry(master=window, font = ('times new roman', 16), width = 50, bd = 1, relief = SOLID)
En2.place(x=220, y=150)

btn2 = Button(master=window, text='Download From youtube', cursor = 'hand2', command=youtube_download)
btn2.place(x=450, y=200)


def download_location():
    file = filedialog.askdirectory()
    if file:
        filepath = os.path.abspath(file)
        En1.insert(0, filepath)
        




btn1 = Button(window, text = '+', cursor = 'hand2', command = download_location)
btn1.place(x=900, y = 20)



window.mainloop()