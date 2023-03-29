from tkinter import *
import qrcode
from PIL import ImageTk, Image
from tkinter import filedialog
import customtkinter
import os





def linkTaker():
    return entryPlace.get()


def ButtonFunction():

    if entryPlace.get() != "":

        myQR = qrcode.make(linkTaker())
        
        
        myQR.save(f"{file}\default.png")

        qrImage = Image.open(f"{file}/default.png")
        resizedImage = qrImage.resize((150, 150))
        lastImage = ImageTk.PhotoImage(resizedImage)

        
        qrLabel.config(image=lastImage)
        qrLabel.image=lastImage


root = Tk()
root.geometry("315x405")
root.resizable(width=False, height=False)
root.title("QR Code Generator")
root.configure(background="#8f00ff")

file = os.getcwd()
root.iconbitmap(f"{file}/icon.ico")

buttonImage = Image.open(f"{file}/convert.jpg")
resized= buttonImage.resize((30,30))
lastButton =ImageTk.PhotoImage(resized)

quitImage= Image.open(f"{file}/quit.jpg")
resizedQuit=quitImage.resize((30,30))
lastQuit= ImageTk.PhotoImage(resizedQuit)


frameMain = Frame(root, background="#8f00ff", border=0, height=500)

entryPlace = customtkinter.CTkEntry(frameMain, width=315, corner_radius=20, text_color="#daa520",
                                    placeholder_text="Paste your link...", placeholder_text_color="#daa520")

convertButton = customtkinter.CTkButton(frameMain,image =lastButton ,text="Convert", command=ButtonFunction, compound=LEFT,
                                        hover_color="#977316", fg_color="#daa520", border_width=2, border_color="#2b50c8",
                                        corner_radius=10, font=("Open Sans", 15), text_color="Black")


quitButton = customtkinter.CTkButton(frameMain,image =lastQuit, text="Quit", command=root.quit, compound=LEFT,
                                     hover_color="#A30000", fg_color="#FF0000", border_width=2,
                                     border_color="#2b50c8", corner_radius=10, font=("Open Sans", 15), text_color="Black")

clearButton = customtkinter.CTkButton(frameMain, text="Clear", command=lambda: entryPlace.delete(0, END),
                                      hover_color="#A30000", fg_color="#FF0000", border_width=2,
                                      border_color="#2b50c8", corner_radius=10, font=("Open Sans", 15), text_color="Black")

frame = LabelFrame(frameMain, background="#8f00ff", border=0)





qrLabel = Label(frame, background="#8f00ff")


frameMain.pack()
entryPlace.pack(pady=5)
convertButton.pack(pady=10)
frame.pack()
qrLabel.pack()
quitButton.pack(pady=20)
clearButton.pack()



root.mainloop()
