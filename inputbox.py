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

        self.promptlabel=tkinter.Label(self.topframe, text="Enter a distance in Kilometers")
        self.entry=tkinter.Entry(self.topframe, width=10)




        #The two lines below move the statements to a corresponding side
        self.promptlabel.pack(side="left")
        self.entry.pack(side="left")




        #The two lines below move the statements to a corresponding side


        self.mybutton=tkinter.Button(self.main_window, text="Convert", command=self.convert)

        self.quitbutton=tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)



        self.mybutton.pack(side="left")
        self.quitbutton.pack(side="right")


        tkinter.mainloop()


    def convert(self):
        kilo=float(self.entry.get())

        miles=round(kilo*0.6214,2)

        tkinter.messagebox.showinfo("Result",str(kilo)+ "kilometers is equal to"+str(miles)+"miles")

my_gui= MyGUI()
#The print below will not run until after the box is closed because the loop is still running. Loop finishes when box is closed 
print("I am done!")
