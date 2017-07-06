from tkinter import *
class Example:
    def __init__(self,master):
        self.lbl = Label(master, text = "What kinds of food do you like?")
        self.lbl.pack()
        self.btn=Button(master,text = "Quit", command = self.quit)
        self.btn.pack()
        self.btn2 = Checkbutton(master, text = "Mango", indicatoron = False, selectcolor = "orange")
        self.btn2.pack()
        self.btn3 = Checkbutton(master, text = "Bundu", indicatoron = False, selectcolor = "purple")
        self.btn4 = Checkbutton(master, text = "Avocado", indicatoron = False, selectcolor = "green")
        self.btn5 = Checkbutton(master, text = "Gnuts", indicatoron = False, selectcolor = "gray")
        self.btn6 = Checkbutton(master, text = "Irish Potatoe", indicatoron = False, selectcolor = "brown")
        self.btn7 = Checkbutton(master, text = "Watermelon", indicatoron = False, selectcolor = "pink")
        self.btn8 = Checkbutton(master, text = "Fish", indicatoron = False, selectcolor = "yellow")
        self.btn9 = Checkbutton(master, text = "Goatmeat", indicatoron = False, selectcolor = "magenta")
        self.btn10 = Checkbutton(master, text = "Matokai", indicatoron = False, selectcolor = "red")
        self.btn11 = Checkbutton(master, text = "Sweetpotatoes", indicatoron = False, selectcolor = "blue")
        self.btn12 = Checkbutton(master, text = "Popcorn", indicatoron = False, selectcolor = "pink")
        self.btn12.pack()
        self.btn12.invoke()

        self.btn11.invoke()
        self.btn3.invoke()
        self.btn3.pack()
        self.btn4.pack()
        self.btn5.pack()
        self.btn6.pack()
        self.btn7.pack()
        self.btn8.pack()
        self.btn9.pack()
        self.btn10.pack()
        self.btn11.pack()
        
     
   

    def quit(self):
        import sys; sys.exit()

    


root = Tk( )
ex4 = Example(root)
root.mainloop()


