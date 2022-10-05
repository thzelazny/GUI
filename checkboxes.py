import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe=tkinter.Frame(self.main_window)
        self.bottomframe=tkinter.Frame(self.main_window)
        self.topframe.pack()
        self.bottomframe.pack()

        self.cb1_var=tkinter.IntVar()
        self.cb2_var=tkinter.IntVar()
        self.cb3_var=tkinter.IntVar()

        self.cb1=tkinter.Checkbutton(self.topframe,text="Option 1",variable=self.cb1_var)

        self.cb2=tkinter.Checkbutton(self.topframe,text="Option 2",variable=self.cb2_var)

        self.cb3=tkinter.Checkbutton(self.topframe,text="Option 3",variable=self.cb3_var)
        
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()




        self.mybutton=tkinter.Button(self.main_window, text="Click Me!", command=self.do_something)

        self.quitbutton=tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)



        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="right")


        tkinter.mainloop()


    def do_something(self):
        message="You have selected:\n"
        
        if self.cb1_var.get()==1:
            message+="option 1\n"
        if self.cb2_var.get()==1:
            message+="option 2\n"
        if self.cb3_var.get()==1:
            message+="option 3\n"

        tkinter.messagebox.showinfo("Reponse",message)

my_gui= MyGUI()
#The print below will not run until after the box is closed because the loop is still running. Loop finishes when box is closed 
print("I am done!")
