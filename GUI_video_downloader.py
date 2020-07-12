from tkinter import *
import os
from tkinter import messagebox
import requests

class Video_downloader:

    def __init__(self, root):
        self.root = root
        self.root.title('Video Downloader')
        self.root.geometry('500x180+600+300')

    # ==============Creating Varibles=================#
        self.name = StringVar()
        self.url = StringVar()

    # =====================creating Labels/Buttons==============#
        lbl_ser = Label(self.root, text='Name', font=('times new roman', 20, 'bold'))
        lbl_ser.grid(row=0, column=0, pady=(10, 0), padx=30, sticky='w')

        txt_ser = Entry(self.root, font=('times new roman', 16, 'bold'), textvariable=self.name, width=25, bd=5, relief=GROOVE)
        txt_ser.grid(row=0, column=1, pady=17, padx=5, sticky='w')

        lbl_ser = Label(self.root, text='Path', font=('times new roman', 20, 'bold'))
        lbl_ser.grid(row=1, column=0, pady=[10, 0], padx=30, sticky='w')

        txt_ser = Entry(self.root, font=('times new roman', 16, 'bold'), textvariable=self.url, width=25, bd=5, relief=GROOVE)
        txt_ser.grid(row=1, column=1, pady=17, padx=5, sticky='w')

        Search = Frame(self.root, relief=RIDGE)
        Search.place(x=10, y=140, width=490, height=40)

        btn = Button(Search, text='Download', width=20, height=1, command=self.download).grid(row=0, column=0, padx=30, pady=5)

    def clear(self):
        self.name.set('')
        self.url.set('')

    def download(self):
        if os.path.exists('''Provide the Path of the Directory in which You want to Store the Downloaded Video'''):
            pass
        else:
            os.mkdir('''Provide the Path of the Directory in which You want to Store the Downloaded Video''')
        os.chdir('''Provide the Path of the Directory in which You want to Store the Downloaded Video''')
        try:
            chunk_size = 256
            url = self.url.get()
            r = requests.get(url, stream=True)
            try:
                with open(self.name.get()+'.mp4', 'wb') as f:
                     for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
            except :
                pass
            self.clear()
            messagebox.showinfo('Success', 'Video Downloaded')
        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema):
            if requests.exceptions.ConnectionError:
                messagebox.showerror('Error', 'Something Went Wrong')


root = Tk()
ob = Video_downloader(root)
root.mainloop()