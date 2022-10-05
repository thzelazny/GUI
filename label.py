import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label1=tkinter.Label(self.main_window, text="Hello World!")
        self.label2=tkinter.Label(self.main_window, text="This is my GUI program")

        #The two lines below move the statements to a corresponding side
        self.label1.pack(side="left")
        self.label2.pack(side="bottom")

        tkinter.mainloop()

my_gui= MyGUI()
#The print below will not run until after the box is closed because the loop is still running. Loop finishes when box is closed 
print("I am done!")
