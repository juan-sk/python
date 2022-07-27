import tkinter
def main():
    root  = tkinter.Tk()
    titulo = "menus"
    creaPantalla(root,titulo)
    
    
    
def creaPantalla(root,titulo):
   root.title(titulo)
   root.resizable(width=True,height=True)
   menu(tkinter,root)
   root.mainloop()
   
   
def quit(root):
    root.destroy()
    
def menu(tkinter,root):
    bar = tkinter.Menu(root)
   
    fileMenu =  tkinter.Menu(bar,   tearoff=0)
    fileMenu.add_command(label ="Exit",command = lambda: quit(root))
    
    bar.add_cascade(label = "File",menu=fileMenu)
    root.config(menu=bar)
if __name__ == "__main__":
    main()