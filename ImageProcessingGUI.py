from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import ntpath
import cv2
import numpy as np

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)   

        self.imageL = None
        self.imageR = None
        self.lastC = None
     
        #reference to the master widget, which is the tk window                 
        self.master = master
        self.panelA = None
        self.panelB = None

        self.init_window()

###################################################### 	  v	LAB 1
    def lab1flipH(self):
        shape = self.imageL.shape        

        im2 = np.zeros((shape[0],shape[1],shape[2]), np.uint8)

        for i in range(0,shape[0]):
            for j in range(0,shape[1]):
                for k in range(0,shape[2]):
                    im2.itemset((i, shape[1]-j-1, k),(self.imageL.item(i, j, k)))
        self.imageR = im2
        self.updatePanelR()


    def lab1flipV(self):
        shape = self.imageL.shape        

        im2 = np.zeros((shape[0],shape[1],shape[2]), np.uint8)

        for i in range(0,shape[0]):
            for j in range(0,shape[1]):
                for k in range(0,shape[2]):
                    im2.itemset((shape[0] - i -1, j, k),(self.imageL.item(i, j, k)))
        self.imageR = im2
        self.updatePanelR()
######################################################    ^  



######################################################    v	GUI 
    # swap self.imageL <-> self.imageR
    # to make quickly operation on imageR
    def swapImage(self):
        self.imageL = self.imageR
        self.updatePanelL()
 

    def openImage(self):
        event = 1
        filename = filedialog.askopenfilename(title='open')
        
        img = cv2.imread(filename)
        img = cv2.resize(img,(400,400))
        
        self.imageL = img

        self.updatePanelL()
           
    # update the right panel with self.imageR 
    # transform cv2 image to tkinter image and show
    def updatePanelR(self):
        b,g,r = cv2.split(self.imageR)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)      
        imgtk = ImageTk.PhotoImage(image = im)
        
        self.panelB = Label(self.master, image=imgtk)
        self.panelB.image = imgtk
        self.panelB.pack(side="left", padx=10, pady=10)
        self.panelB.place(x=550, y=100)
    

    # update the left panel with self.imageRL
    # transform cv2 image to tkinter image and show
    def updatePanelL(self):
        b,g,r = cv2.split(self.imageL)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)      
        imgtk = ImageTk.PhotoImage(image = im)
        
        self.panelA = Label(self.master, image=imgtk)
        self.panelA.image = imgtk
        self.panelA.pack(side="left", padx=10, pady=10)
        self.panelA.place(x=50, y=100)

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ImageProcessingGUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.openImage)
        filemenu.add_command(label="Save", command=self.openImage)
        filemenu.add_command(label="Swap", command=self.swapImage)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command= self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0) 
        editmenu.add_command(label="flipH", command=self.lab1flipH)
        editmenu.add_command(label="flipV", command=self.lab1flipV)
        menubar.add_cascade(label="lab1", menu=editmenu)

        # display the menu
        self.master.config(menu=menubar)
######################################################     ^
    

root = Tk()

root.geometry("1000x600")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  