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

        self.label1=tkinter.Label(self.topframe, text="John")
        self.label2=tkinter.Label(self.topframe, text="Jim")
        self.label3=tkinter.Label(self.topframe, text="Jerry")


        #The two lines below move the statements to a corresponding side
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")

        self.label4=tkinter.Label(self.bottomframe, text="Jill")
        self.label5=tkinter.Label(self.bottomframe, text="Jen")
        self.label6=tkinter.Label(self.bottomframe, text="Jessica")



        #The two lines below move the statements to a corresponding side
        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")


        self.mybutton=tkinter.Button(self.main_window, text="Click Me!", command=self.do_something)

        self.quitbutton=tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)



        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="right")


        tkinter.mainloop()


    def do_something(self):
        tkinter.messagebox.showinfo("Reponse","Thanks for clicking me!")

my_gui= MyGUI()
#The print below will not run until after the box is closed because the loop is still running. Loop finishes when box is closed 
print("I am done!")
