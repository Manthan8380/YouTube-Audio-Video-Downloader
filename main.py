'''
YouTube Audio & Video Downloader
Author: Manthan Chopde
'''

# Importing the Packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser

# ========================== Functions ==========================
def download():
    if x.get()==0:
        messagebox.showinfo("Alert", f"Downloading...")
        mp3 = link.get()
        my_mp3 = YouTube(mp3)
        stream = my_mp3.streams.get_audio_only()
        stream.download()
    elif x.get()==1:
        messagebox.showinfo("Alert", f"Downloading...")
        video = link.get()
        my_video = YouTube(video)
        stream = my_video.streams.get_highest_resolution()
        stream.download()

def git():
    webbrowser.open_new("https://github.com/Manthan8380")
def insta():
    webbrowser.open_new("https://www.instagram.com/manthanchopde2016")
def fb():
    webbrowser.open_new("https://www.facebook.com/manthan.chopde")
# ==============================================================

# Creating Window
root = tk.Tk()
root.title('YT AV Downloader')
root.configure(bg= "#ffffff")
root.iconbitmap('icons/main.ico')

# Setting Up Canvas Size and Wallpaper
my_canvas = tk.Canvas(root, width=750, height=500)
my_canvas.pack(fill="both", expand=True)

# Wallpaper Setting
background_img = Image.open("background/wallSina.png")
resized_image = background_img.resize((750, 500), Image.ANTIALIAS)
new_bg = ImageTk.PhotoImage(resized_image)
background = my_canvas.create_image(0,0, image = new_bg, anchor = "nw")

# Creating & Adjusting the LOGO
logo = Image.open("logo/YTlogo.png")
resized_logo = logo.resize((50, 45), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)
logo_n = my_canvas.create_image(380,70, image = new_logo)
my_canvas.create_text(442,60, text="YouTube", fill='black', font=('Raleway', 10))
my_canvas.create_text(544,80, text="Audio & Video Downloader", fill='black', font=('Raleway', 16))

# Creating Text & EntryBox
my_canvas.create_text(396,175, text="Paste Your Link Here :", fill='black', font=('gabriola', 14))
link = Entry(bd = 0, bg = "#b1b1b1", highlightthickness = 0,font=('arial', 10))
link.place(x = 330, y = 190, width = 400, height = 25)

# Creating RadioButtons
x = IntVar()
rdoBtn1 = Radiobutton(root, width = 8, height = 1, font = ('Raleway', 12,'italic'),
                      bg = '#f5f7f5',text = "Download MP3", bd = 0,variable = x,value = 0, padx = 25)
rdoBtn2 = Radiobutton(root, width = 8, font = ('Raleway', 12, 'italic'),
                     bg = '#f5f7f5', text = "Download Video", bd = 0, variable = x,value = 1, padx = 25)
rdoBtn1.place(x = 360, y = 280)
rdoBtn2.place(x = 545, y = 280)

# Creating Download Button
download_text = tk.StringVar()
download_btn = tk.Button(root, textvariable=download_text, font=('Comic Sans MS', 12), bg='#45B39D',
                         fg='black', width=10, command = download)
download_btn.place(x=465, y=340)
download_text.set("Download")

# Creating Social Media Icons
img0 = PhotoImage(file = "icons/git.png")
b0 = Button(image = img0, borderwidth = 0, bg = '#f0f2f2', highlightthickness = 0, command = git, relief = "flat")
b0.place(x = 470, y = 400, width = 30, height = 30)
img1 = PhotoImage(file = "icons/insta.png")
b1 = Button(image = img1, borderwidth = 0, bg = '#f0f2f2', highlightthickness = 0, command = insta, relief = "flat")
b1.place(x = 506, y = 400, width = 30, height = 30)
img2 = PhotoImage(file = "icons/fb.png")
b2 = Button(image = img2, borderwidth = 0, bg = '#f0f2f2',  highlightthickness = 0, command = fb, relief = "flat")
b2.place(x = 542, y = 400, width = 30, height = 30)

# Footer
my_canvas.create_text(520,485, text="Min-ERVA Corp. @2021", fill='black', font=('Century Gothic', 8))

root.resizable(False,False)
root.mainloop()
# ======================================================== End ========================================================