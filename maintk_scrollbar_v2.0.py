#!/usr/bin/python3
# -*- coding: utf8 -*-
#for jupyter-lab just type jupyter-lab
import json
import tkinter as tk
from tkinter import Tk, Label, ttk, Button, Entry, Frame, Menu, Scrollbar, Canvas
from tkinter.ttk import Notebook
from tkinter.simpledialog import askstring
from tkinter.simpledialog import Dialog
from tkinter import filedialog
from tkinter import messagebox
from tkinter import StringVar
from fpdf import *
import PIL
from PIL import ImageTk as ImgTk
from PIL import Image as Img

#Languages dictionaries
gr = { 
    'addFurn':'Βάλε έπιπλο',
    'addMat':'Πρόσθεσε υλικό',
    'addDim': 'Πρόσθεσε Διάσταση',
    'changeImg':'Άλλαξε εικόνα',
    'settings':'Ρυθμήσεις',
    'edit': 'Μορφοποίηση',
    'setngs_chng_lang':'Ελληνικά',
    'chng_name':'Άλλαξε Ονομα'
    
}
bg = {
    'addFurn':'Добави шкаф',
    'addMat':'Добави материал',
    'addDim': 'Добави размер',
    'changeImg':'Смени икона',
    'settings':'Настройки',
    'edit':'Измени',
    'setngs_chng_lang':'Български',
    'chng_name':'Άλλαξε Ονομα',
    'chng_img':'Смени икона',
    'print':'Print to bg pdf File',
    'no_img_selected':'No bg image selected'
}
en = {
    'addFurn':'Add Furniture',
    'addMat':'Add Material',
    'addDim': 'Add Dimension',
    'changeImg':'Change icon',
    'settings': 'Settings',
    'edit':'Edit',
    'setngs_chng_lang':'English',
    'chng_name':'Change Name',
    'chng_img':'Change Image',
    'print':'Print to pdf File',
    'no_img_selected':'No image selected'
}
default = {
    'addFurn':'Add Furniture',
    'addMat':'Add Material',
    'addDim': 'Add Dimension',
    'changeImg':'Change icon',
    'settings': 'Settings',
    'edit':'Edit',
    'setngs_chng_lang':'English',
    'chng_name':'Change Name',
    'chng_img':'Change Image',
    'print':'Print to pdf File',
    'no_img_selected':'No image selected'
}


class Material:
    #Instead of having linked lists and shit like that, i just create objects for each material
    #And add each dimension in the dimensions list
    #I will go with the Tabs method of design
    def __init__(self, rootFrame, **args):
        self.Id = 0
        self.matFrame = Frame(rootFrame, args)
        #self.matFrame.bind("<ButtonPress-1>", lambda event=None: print('Hello'))
        #self.Name = Entry(self.matFrame, state='normal')
        #self.Name.bind('<Return>', lambda event=None: self.ed(self.Name.get(), self.Id))
        #self.addDimensionBtn = Button(self.matFrame, text=default['addDim'], command=self.addDimension)
        self.dimLabel = Label(self.matFrame, text='Dimensions')
        self.qLabel = Label(self.matFrame, text='Quantity')
        self.xLabel = Label(self.matFrame, text='Width')
        self.yLabel = Label(self.matFrame, text='Height')
        self.Dimensions = []
        #self.Name.grid(row=0, column=0, columnspan=3)
        #self.addDimensionBtn.grid(row=0, column=1)
        self.dimLabel.grid(row=0, column=0, columnspan=3)
        self.qLabel.grid(row=1, column=0)
        self.xLabel.grid(row=1, column=1)
        self.yLabel.grid(row=1, column=2)
        
        self.currRow = 2
        self.currCol = 0

class Furniture():#Frame):
    #This class defines a furniture
    #which consists of an image(Label), an entry(for the name of the furniture)
    #And any subsequent entries for the name of material and dimensions
    #Each object of this class will be put on the screen
    def __init__(self, rootWin, ID, **args):
        self.mainFrame = Frame(rootWin, args)
        self.Materials = []
        self.currMat = 0
        self.FurnID = ID
        self.MatID = 0
        self.Title = Label(self.mainFrame, text='Furniture')
        self.Ntbook = Notebook(self.mainFrame)
        self.imageFile = '../res/cab_cook.png'
        image = Img.open(self.imageFile)
        image.thumbnail((150, 150))
        self.furnImg = ImgTk.PhotoImage(image)
        del image
        self.objImg =  Label(self.mainFrame, text="Object Image")

        self.Title.grid(row=0, column=0, columnspan=4)
        self.objImg['image'] = self.furnImg
        self.objImg.grid(row=1, column=0, columnspan=4)
        self.Ntbook.grid(row=2, column=0, columnspan=4)

        self.mainFrame.bind('<ButtonPress-1>', self.setFocus)
        self.Title.bind('<ButtonPress-1>', self.setFocus)
        self.objImg.bind('<ButtonPress-1>', self.setFocus)


    def gridF(self, ro, col):
        self.mainFrame.grid(row=ro, column=col, sticky='nwse', padx=2, pady=2)
    def winfo_widthF(self):
        return self.mainFrame.winfo_width()
    def winfo_heightF(self):
        return self.mainFrame.winfo_height()
    def configF(self, **args):
        self.mainFrame.config(args)
    def grid_removeF(self):
        self.mainFrame.grid_remove()
    #def ed2(self, title, ID):
    #    self.Ntbook.tab(ID, text=title)
    def setFocus(self, event=None):
        focus[0] = self.FurnID
#End of class Furniture

#Functions        
def addFurniture(event=None):
    furnFrame = Furniture(objectsFrame, FurnitureID[0], highlightbackground='black', highlightthickness=1, borderwidth=5)
    FurnitureID[0] += 1
    Furnitures.append(furnFrame)
    showFurnitures()
def showFurnitures(event=None):
    colb = 0
    row = 0
    frameHeightSum[0] = 0
    frameWidthSum[0] = 0
    ScrnWidth = root.winfo_width()
    for i in range(len(Furnitures)):
        Furnitures[i].gridF(row, colb)
        Furnitures[i].configF(bg='white', padx=20)
        colb+=1
        frameWidthSum[0] += Furnitures[i].winfo_widthF()
        #Add the first row height
        if i == 1:
            frameHeightSum[0] += Furnitures[i].winfo_heightF()
            #check if the width is enough to fit all the frames
        if frameWidthSum[0] > ScrnWidth:
            row+=1
            colb = 0
            frameWidthSum[0] = 0
            Furnitures[i].gridF(row, colb)
            colb+=1
            frameWidthSum[0] += Furnitures[i].winfo_widthF()
            frameHeightSum[0] += Furnitures[i].winfo_heightF()
            #now check if the height is enough to fit new frames
        #End if
    #End for


def printFile():
    pdf = FPDF(orientation='L', format='A4', unit='mm' )
    pdf.add_page()
    #pdf.set_margins(left=2.54, top=2.54, right=2.54)
    pdf.set_xy(15.4, 15.4)
    #Landscape pdf Width ( A4 ) mm
    LpdfW = 297-15.4
    #Landscape pdf Height (A4) mm
    LpdfH = 210-15.4
    #pdf['orientation'] = 'L'
    #Left margin for landscape = 25mm    #Right margin for Landscape = 15mm
    #pdf.set_doc_option('core_fonts_encoding', 'windows-1252')
    pdf.add_font('OpenSans', fname='../res/Open_Sans/OpenSans-SemiBold.ttf', uni=True)
    pdf.set_font('OpenSans', size=12) #'B', 12)
    pdf.rect(15.4, 15.4, LpdfW-15.4, LpdfH-15.4, style='D')
    totalWidth = 0
    totalHeight = 0
    X = 15.4
    Y = 15.4
    print('before')
    for i in range(len(Furnitures)):
        print('inside')
        currX = pdf.get_x()
        currY = pdf.get_y()
        pdf.set_xy(X , Y)
        print(Furnitures[i].Title['text'])
        pdf.cell(45, 5, Furnitures[i].Title['text'], align='C', border=1, ln=2)
        pdf.cell(45, 40, border=1, ln=2)
        Y+=7
        pdf.set_xy(X+2, Y)
        pdf.image(name=Furnitures[i].imageFile, w=40, h=35)
        Y=45+15.4
        pdf.set_xy(X, Y)
        pdf.set_font_size(10)
        tab_names = [Furnitures[i].Ntbook.tab(j, option="text") for j in Furnitures[i].Ntbook.tabs()] # list comprehensions
        #same as using
        #tab_names = []
        #for i in notebook.tabs():
        #    tab_names.append(notebook.tab(i, "text"))
        for k in range(len(tab_names)):
            pdf.cell(45, 5, tab_names[k], align='C', border=1, ln=2)
            for l in range(len(Furnitures[i].Materials[k].Dimensions)):
                #quantity
                pdf.cell(15, 5, Furnitures[i].Materials[k].Dimensions[l][0].get(), align='L', border=1, ln=0)
                #width
                pdf.cell(15, 5, Furnitures[i].Materials[k].Dimensions[l][1].get(), align='L', border=1, ln=0)
                #height
                pdf.cell(15, 5, Furnitures[i].Materials[k].Dimensions[l][2].get(), align='L', border=1, ln=2)
                pdf.set_x(X)
                Y+=10
                print('Y=',Y)
            #End for l
            
            pdf.set_xy(X, Y)
        X+=45
        Y = 15.4
        #pdf.set_xy(X, Y)
        #im thinking of using the ln=2 for the furniture and then when done just add ln = 0
    #pdf.cell((pdf.get_string_width('Hello World!')), 16, 'Hello World!', align='center', border=1)
    #pdf.line(LpdfW/2, 0, LpdfW/2, LpdfH)
    #pdf.image('shkaf.png', x = 50, y = 50, w = 200, h = 200, type = '', link = '')
    pdf.output('tuto1.pdf', 'F')

def changeFurName(event=None):
    name = askstring(title=default['chng_name'], prompt=default['chng_name'])
    Furnitures[focus[0]].Title['text'] = name
def addMaterial(event=None):
    furn = Furnitures[focus[0]]
    matObject = Material(furn.Ntbook)
    furn.Ntbook.add(matObject.matFrame, text='Material')
    matObject.Id = furn.MatID
    furn.MatID += 1
    furn.Materials.append(matObject)
def addDimension(event=None):
    mat = Furnitures[focus[0]].Materials[-1]
    #quantity width height
    quantity = Entry(mat.matFrame) 
    width = Entry(mat.matFrame)
    height = Entry(mat.matFrame)
    quantity.grid(row=mat.currRow, column=mat.currCol)
    mat.currCol+=1
    width.grid(row=mat.currRow, column=mat.currCol)
    mat.currCol+=1
    height.grid(row=mat.currRow, column=mat.currCol)
    mat.currCol = 0
    mat.currRow+=1 
    mat.Dimensions.append([quantity, width, height])
def changeMatName(event=None):
    name = askstring(title=default['chng_name'], prompt=default['chng_name'])
    furn = Furnitures[focus[0]]
    selectedTabIndex = furn.Ntbook.index(furn.Ntbook.select())
    furn.Ntbook.tab(selectedTabIndex, text=name)
def mouseScroll(event):
    if event.delta:
        canvasF.yview_scroll(int(-1*(event.delta/120)), "units")
    elif event.num == 5:
        move = 1
    else:
        move = -1
    canvasF.yview_scroll(move, "units")
def changeImage(event=None):
    filename = filedialog.askopenfilename()
    if filename == '':
        messagebox.showinfo(message=default['no_img_selected'])
    else:
        image = Img.open(filename)
        image.thumbnail((150,150))
        Furnitures[focus[0]].imageFile = filename
        Furnitures[focus[0]].furnImg = ImgTk.PhotoImage(image)
        Furnitures[focus[0]].objImg['image'] = Furnitures[focus[0]].furnImg
        del image

#Main window variable-object
root = Tk()

#-------------------------------MENU-------------------------------
#Menu Bar 
MenuBar = Menu(root, bg='lightgrey', fg='black')
#Edit menu
edit_menu = Menu(MenuBar, tearoff=0, bg='lightgrey', fg='black')
edit_menu.add_command(label=default['addFurn'], command=addFurniture, accelerator='Ctr+A')
edit_menu.add_command(label=default['chng_name'], command=changeFurName, accelerator='Ctr+R')
edit_menu.add_command(label=default['addMat'], command=addMaterial, accelerator='Ctr+M')
edit_menu.add_command(label=default['addDim'], command=addDimension, accelerator='Ctr+D')
edit_menu.add_command(label=default['chng_name'], command=changeMatName)
edit_menu.add_command(label=default['chng_img'], command=changeImage, accelerator='Ctr+I')
edit_menu.add_separator()
edit_menu.add_command(label=default['print'], command=printFile, accelerator='Ctr+P')
#Settings menu
settings_menu = Menu(MenuBar, tearoff=0, bg='lightgrey', fg='black')
#settings_menu.add_radiobutton(label=en['setngs_chng_lang'], command=changeLang(en))
#settings_menu.add_radiobutton(label=bg['setngs_chng_lang'], command=changeLang(bg))
#settings_menu.add_separator()
settings_menu.add_command(label='Show', command= lambda: print(default['addFurn']))
MenuBar.add_cascade(label=default['edit'], menu=edit_menu)
MenuBar.add_cascade(label=default['settings'], menu=settings_menu)
#End Menu Bar
#------------------------------------------------------------------

root.title("Furniture Print - Tk version")
#------------------------------SCREEN------------------------------
#Screen
# 'widthxheight+-x+-y
ScreenWidth = root.winfo_screenwidth()//2
ScreenHeight = root.winfo_screenheight()//2
root.geometry(str(ScreenWidth)+'x'+str(ScreenHeight)+'+0+0')
#winfo_screenmmwidth()
root.resizable(True, True)
root.configure(menu=MenuBar)
#End Screen
#-------------------------------------------------------------------


#----------------------------Variables-----------------------------
FurnitureID = [0] #Helps us make connection between furniture Classes and the Application Menu Bar
focus = [0] #saving the state in a 1 item list so it is imutable, can be used as this: Furnitures[focus[0]]
Furnitures = []
frameHeightSum = [0]
frameWidthSum = [0]
theme = ttk.Style()
theme.theme_use('default')
#------------------------------------------------------------------


#-------------------------GUI components---------------------------
#addFurnitureObject = Button(root, text=default['addFurn'], command=addFurniture)
canvasF = Canvas(root)
objectsFrame = Frame(canvasF)
scrollbar = Scrollbar(canvasF, orient='vertical', command=canvasF.yview)
canvasF.configure(yscrollcommand=scrollbar.set)


#------------------------------------------------------------------

#-------------------------Main Layout------------------------------
#Layout of the main gui components of the main window
canvasF.grid(row=1, column=0, sticky='nwes', columnspan=2)
scrollbar.pack(side='right', fill='y')
objectsFrame.pack(side='left', fill='both')
canvas_frame = canvasF.create_window((0,0), window=objectsFrame, anchor='nw')
#addFurnitureObject.grid(row=0, column=0, sticky='nw')
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
#addFurnitureObject.rowconfigure(0, weight=1)
#------------------------------------------------------------------

#-----------------------Root Bindings - Events--------------------------
#root - MainWindow
root.bind('<Control-a>', addFurniture)
root.bind('<Control-r>', changeFurName)
root.bind('<Control-m>', addMaterial)
root.bind('<Configure>', showFurnitures)
root.bind('<Control-p>', lambda event=None: print(Furnitures))

root.bind_all("<MouseWheel>", mouseScroll)
root.bind_all("<Button-4>", mouseScroll)
root.bind_all("<Button-5>", mouseScroll)

root.configure(background='white')
#------------------------------------------------------------------

root.mainloop() 

