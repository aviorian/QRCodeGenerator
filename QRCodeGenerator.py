from tkinter import *
import qrcode
from PIL import ImageTk,Image
from tkinter import filedialog
import customtkinter



clickCounter=0



def linkTaker() :
    return entryPlace.get()

    

def ButtonFunction():

    global clickCounter

    if entryPlace.get() != "" :
        
        

        if clickCounter > 0 :
             
             for widget in frame.winfo_children():
                widget.destroy()

    
        clickCounter+=1

        
    #    file = filedialog.asksaveasfilename(
      #                                   defaultextension=".png",
     #                                    filetypes=(("PNG File",".png"),("JPEG File",".jpeg")))
        
        
        if file:
                myQR= qrcode.make(entryPlace.get())
                myQR.save(file)
                
                

                qrImage = Image.open(file)
                resizedImage = qrImage.resize((150,150))
                lastImage = ImageTk.PhotoImage(resizedImage)
                
                newLabel = Label(frame, image= lastImage)
                newLabel.image =lastImage
                newLabel.pack()
                 
                

root = Tk()
root.geometry("315x405")
root.resizable(width=False,height=False)
root.title("QR Code Generator")
#root.iconbitmap("icon.ico")

#buttonImage = Image.open("convert.jpg")
#resized= buttonImage.resize((30,30))
#lastButton =ImageTk.PhotoImage(resized)

#quitImage= Image.open("quit.jpg")
#resizedQuit=quitImage.resize((30,30))
#lastQuit= ImageTk.PhotoImage(resizedQuit)
                                


frameMain = Frame(root, background="#8f00ff",border=0,height=500)

entryPlace = customtkinter.CTkEntry(frameMain,width=315,corner_radius=20,text_color="#daa520",
                                    placeholder_text="Paste your link...",placeholder_text_color="#daa520")

convertButton = customtkinter.CTkButton(frameMain,text="Convert",command= ButtonFunction,compound=LEFT,
                                        hover_color="#977316",fg_color="#daa520",border_width=2 ,border_color="#2b50c8",
                                        corner_radius=10,font=("Open Sans",15),text_color="Black")
                                        


quitButton = customtkinter.CTkButton(frameMain,text="Quit",command=root.quit,compound=LEFT,
                                     hover_color="#A30000",fg_color="#FF0000",border_width=2 ,
                                     border_color="#2b50c8",corner_radius=10,font=("Open Sans",15),text_color="Black")

clearButton = customtkinter.CTkButton(frameMain,text="Clear",command=lambda: entryPlace.delete(0,END),
                                      hover_color="#A30000",fg_color="#FF0000",border_width=2,
                                      border_color="#2b50c8",corner_radius=10,font=("Open Sans",15),text_color="Black")

frame = LabelFrame(frameMain,background="#8f00ff",border=0)

#Background

background = Label(frameMain,background="#8f00ff")
background2 = Label(frameMain,bg="#8f00ff")
background3 = Label(frameMain,bg="#8f00ff")
background4 = Label(frameMain,bg="#8f00ff")
background5 = Label(frameMain,bg="#8f00ff")
background6 = Label(frameMain,bg="#8f00ff")
background7 = Label(frameMain,bg="#8f00ff")
background8 = Label(frameMain,bg="#8f00ff")
background9 = Label(frameMain,bg="#8f00ff")
background10 = Label(frameMain,bg="#8f00ff")
background11 = Label(frameMain,bg="#8f00ff")
background12 = Label(frameMain,bg="#8f00ff")




qrLabel = Label(frame,background="#8f00ff")


frameMain.pack()
entryPlace.pack(pady=5)
convertButton.pack(pady=10)
frame.pack()
qrLabel.pack()
quitButton.pack(pady=20)
clearButton.pack()

background2.pack()
background3.pack()
background4.pack()
background5.pack()
background7.pack()
background8.pack()
background9.pack()
background10.pack()
background11.pack()
background12.pack()


root.mainloop()