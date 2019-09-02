from tkinter import *
from tkinter import filedialog
class TextEditor:
    # Intialize the text editor so that it will have the layout
    def __init__(self,root):
        self.menubar=Menu(root,font=("Callibri",12))
        root.config(menu=self.menubar)
        self.filemenu=Menu(root,tearoff=0,font=("Callibri",12))
        
        self.filemenu.add_command(label="New",command=self.donothing)
        self.filemenu.add_command(label="Open",command=self.openFile)
        self.filemenu.add_command(label="Save",command=self.saveFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=root.destroy)
        
        self.menubar.add_cascade(label="File",menu=self.filemenu)


        self.editmenu=Menu(root,tearoff=0,font=("Callibri",12))
        
        self.editmenu.add_command(label="Cut",command=self.donothing)
        self.editmenu.add_command(label="Copy",command=self.donothing)
        self.editmenu.add_command(label="Paste",command=self.donothing)
        
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)

        self.thememenu=Menu(root,tearoff=0,font=("Callibri",12))
        self.thememenu.add_command(label="Dark",command=lambda:self.themeChange(1))
        self.thememenu.add_command(label="Light",command=lambda:self.themeChange(2))
        self.menubar.add_cascade(label="Theme",menu=self.thememenu)
        self.text_area=Text(root,bg="white",fg="black",font=("Callibri",12),wrap=NONE)
        # scroll bars
        # horizontal scroll bar
        self.horizontal_scroll_bar=Scrollbar(root,orient=HORIZONTAL,bg="#3687ce",activebackground="#0056a1",command=self.text_area.xview)
        self.text_area.configure(xscrollcommand=self.horizontal_scroll_bar.set)
        self.horizontal_scroll_bar.pack(side=BOTTOM,fill=X)
        # vertical scroll bar
        self.vertical_scroll_bar=Scrollbar(root,orient=VERTICAL,bg="#3687ce",activebackground="#0056a1",command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.vertical_scroll_bar.set)
        self.vertical_scroll_bar.pack(side=RIGHT,fill=Y)
        # to fill the text widget to full root
        self.text_area.pack(expand=True,fill=BOTH)
        
    # for testing purpose
    def donothing(self):
        pass

    # for opening a file
    def openFile(self):        
        self.filename=filedialog.askopenfilename(parent=root,title="Select a file",filetypes=(("Python file","*.py"),("All files","*.*")))
        # to check a file is selected
        if self.filename!=None:
            f=open(self.filename,'r')
            contents=f.read()
            # Insert the contents from start to end
            self.text_area.insert(1.0,contents)
            # Close the file
            f.close()
    
    # for saving the file
    def saveFile(self):
        self.filename=filedialog.asksaveasfilename(parent=root,defaultextension=".txt")
        # if file name is not provided or cancel button is clicked
        if self.filename!=None:
            f=open(self.filename,'w')
            # get contents from start to end
            contents=str(self.text_area.get(1.0,END))
            # write the file to the file
            f.write(contents)
            f.close()

    # change the theme of text area
    def themeChange(self,value):
        if(value==1):
            self.text_area["bg"]="black"
            self.text_area["fg"]="white"
        if(value==2):
            self.text_area["bg"]="white"
            self.text_area["fg"]="black"

root=Tk()
root.title('Python Text Editor')
root.geometry('800x600')
text_editor_obj=TextEditor(root)
root.mainloop()