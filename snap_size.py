from tkinter  import * 
import tkinter as tk 
from tkinter import filedialog          
from tkinter import messagebox
from window_utils import open_file_dialog,get_P,open_help,_from_rgb
from PIL import Image, ImageTk
import cv2
import os 
from resize_ import _resize
import random
import string


root = Tk()

root.geometry("850x380")

root.title("Snap size")

root.configure(bg=_from_rgb((99, 242, 237))) 

icon = PhotoImage(file = "logo.png")

root.iconphoto(False, icon)

v1 = DoubleVar() 

root.resizable(False, False)

def select_file(): 
    
    global file_path
    
    global img
    
    file_path = filedialog.askopenfilename(initialdir="/", title="Select A Photo", filetypes=(("jpg files", "*.jpg"),("PNG file ", "*.png")))
    
    canvas = Canvas(root, width=200 ,height =120)
    
    img = Image.open(file_path)
    
    re = img.resize((200,120),Image.ANTIALIAS)
    
    img = ImageTk.PhotoImage(re)
    
    canvas.delete(ALL)
    
    canvas.create_image(1, 1, anchor=NW, image=img) 
    
    canvas.grid(row = 0, column=2)
    
    

   
def select_dir(): 
    global dir_path 
    dir_path = filedialog.askdirectory()


def btn_clicked(): 
    try:
        label1 = Label(text=f"resized{file_path}").grid(row = 2, column= 2)
        per = v1.get()
        _resize(file_path,dir_path,per)
        #_resize(file_path,dir_path,per)
    except NameError as error :
        label2 = Label(text= f"Error: {error}",fg = '#FF0000').grid(row = 10,column=0)



top_menu = Menu(root)

root.config(menu=top_menu)

file = Menu(top_menu, tearoff=0)  

file.add_separator()  

file.add_command(label="Exit", command=root.quit)  

top_menu.add_cascade(label="File", menu=file)  

edit = Menu(top_menu, tearoff=0)  

help = Menu(top_menu, tearoff=0)  

help.add_command(label="About",command = open_help)  

top_menu.add_cascade(label="Help", menu=help)  

  
#Button
Button(root,text = "Select Photo",command= select_file,padx = 5,pady = 10 ).grid(row=0,column=0,padx = 30,pady = 10 )

Button(root,text = "Select Dir",command= select_dir,padx = 5,pady = 10).grid(row=0,column=1,pady = 20)
#Lablel one 
label= Label(text = "Choose the % of image to be resized -> ", bg  = _from_rgb((99, 242, 237))).grid(padx=7,row = 1, column = 1)
#slider
P_scale = Scale( root, variable = v1,  
           from_ = 10, to = 100,length=400,tickinterval=10 , 
           orient = HORIZONTAL,bg  = _from_rgb((99, 242, 237))).grid(pady = 20,padx=10,row = 1, column=2)

#Button 2 
Button(root,text = "save",command= btn_clicked,padx = 20,pady = 10).grid(pady = 10,row=2 ,column=0)




#canvas.create_image(20, 20, anchor=NW, image=img)


root.mainloop()