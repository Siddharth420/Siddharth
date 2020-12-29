from tkinter import *
import time
from sqlite3 import *
import random
from tkinter import messagebox

class AccBook:
    
    def __init__(self, root):
        self.root = root
        self.root.title('AccBook')
        self.root.iconbitmap('accbook1_iCn_icon.ico')
        self.root.config(bg = 'black')
        self.root.geometry('1375x750+0+0')
        self.frame = Frame(self.root, bg = 'black')
        self.frame.pack()
    
    #========================================================Home==========================================================#
        titleframe = Frame(self.frame,height = 150, width = 1350, bg = 'black', relief = 'groove')
        titleframe.pack(side = TOP)
        
        
        title = Label(titleframe, font = ("bankgohtic md bt",50,'bold'), text = "Welcome To AccBook", bg = 'black'
                      , fg = "Ghost White")
        title.grid(row = 0, column = 1)
        
        buttonframe = Frame(self.frame, height = 100, width = 1350, bg  = 'black', relief = 'groove')
        buttonframe.pack(side = BOTTOM)
        
        gapframe = Frame(self.frame, height = 300, width = 1350, bg  = 'black', relief = 'groove')
        gapframe.pack(side = BOTTOM)
        
        Cre_User = Button(buttonframe, font = ("bankgohtic md bt",20,'bold'), text = 'Create Super User', bg = 'black',
                          fg = 'Ghost White')
        Cre_User.grid(row = 0,column = 0)
        
        Sel_User = Button(buttonframe, font = ("bankgohtic md bt",20,'bold'), text = 'Select Super User', bg = 'black',
                          fg = 'Ghost White', state = DISABLED)
        Sel_User.grid(row = 0,column = 1)
        
        
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    application = AccBook(root)
    root.mainloop
        
   
    
    
        
    
