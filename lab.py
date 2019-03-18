from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import ntpath
import cv2


class Window(Frame):

    def __init__(self, master=None):
   
        self.imageL = None
        self.imageR = None
        self.lastC = None
     
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master
        self.panelA = None
        self.panelB = None

        self.init_window()

    def donothing(self):
        pass
    
    def openImage(self):
         
        filename = filedialog.askopenfilename(title='open')
        print(filename)
        self.initPanel(filename)
            
      
    def initPanel(self, imagePath):
        head, imagePath = ntpath.split(imagePath)
        
        image = Image.open(imagePath)
        image = image.resize((400, 400), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        
        self.panelA = Label(root, image=image)
        self.panelA.image = image
        self.panelA.pack(side="left", padx=10, pady=10)
        self.panelA.place(x=50, y=100)

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ImageProcessingGUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menubar = Menu(self.master)

        # create the file object)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="rotateH", command=self.donothing)
        filemenu.add_command(label="rotateV", command=self.donothing)
        filemenu.add_command(label="openI", command=self.openImage)
        menubar.add_cascade(label="lab1", menu=filemenu)
 
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing) 
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="lab2", menu=helpmenu)
        
        menubar.add_cascade(label="exit", menu=self.donothing)        

        self.master.config(menu=menubar)
    
    

root = Tk()

root.geometry("1000x600")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  