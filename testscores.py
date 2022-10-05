import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.frame1=tkinter.Frame(self.main_window)
        self.frame2=tkinter.Frame(self.main_window)
        self.frame3=tkinter.Frame(self.main_window)
        self.frame4=tkinter.Frame(self.main_window)
        self.frame5=tkinter.Frame(self.main_window)


        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()




        self.label1=tkinter.Label(self.frame1, text="Enter the score for test 1:")
        self.label2=tkinter.Label(self.frame2, text="Enter the score for test 2:")        
        self.label3=tkinter.Label(self.frame3, text="Enter the score for test 3:")
        self.label4=tkinter.Label(self.frame4,text="Average:")


        self.entry1=tkinter.Entry(self.frame1,width=10)
        self.entry2=tkinter.Entry(self.frame2,width=10)
        self.entry3=tkinter.Entry(self.frame3,width=10)

        

        #The two lines below move the statements to a corresponding side
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")
        self.label4.pack(side="left")

        self.entry1.pack(side="left")
        self.entry2.pack(side="left")
        self.entry3.pack(side="left")
        

        self.avg_var=tkinter.StringVar()




        self.avg=tkinter.IntVar()

        self.label5=tkinter.Label(self.frame4,textvariable=self.avg)

        self.label5.pack(side="left")

        self.mybutton=tkinter.Button(self.main_window, text="Average", command=self.average)
        self.mybutton.pack(side="left")

        self.quitbutton=tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)
        self.quitbutton.pack(side="right")
        





        tkinter.mainloop()


    def average(self):
        entry1=float(self.entry1.get())
        entry2=float(self.entry2.get())
        entry3=float(self.entry3.get())

        self.avg.set((entry1+entry2+entry3)/3)

my_gui= MyGUI()
#The print below will not run until after the box is closed because the loop is still running. Loop finishes when box is closed 
print("I am done!")
