from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget, which is a window
# with a title bar and other decoration provided by the window manager.  The 
# root widget has to be created before any other widgets and there can only be one
root = Tk()

#The next line contains the Label widget.  First parameter is called parent window.
# So our Label widget is a child of the root widget.  The keywork parameter "text" 
# specifies the text to be shown.
w = Label(root,text="Hello Tkinter!")

#The pack method tells Tk to fit the size of the window to the given text
w.pack()

#The window won't appear until we enter the Tkinter event loop
root.mainloop()