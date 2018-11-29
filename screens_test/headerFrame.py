

import tkinter as tk
from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk
from module1 import connectionDetails, ZToken
from tkinter import font
import os, time
from tkinter import messagebox

class mainFrame(Frame):
    def __init__(self):
        super().__init__()
        self.allInOneValue = StringVar()
        self.mainWidgets()
        self.changeButtonState('New')

    def mainWidgets(self):
        #self.columnconfigure(0, pad=3)
        #self.columnconfigure(1, pad=3)
        #self.rowconfigure(0, pad=3)
        #self.rowconfigure(1, pad=3)
        
        ######## Header ##########
        zHeader1= font.Font(family="Helvetica",size=20)
        titleLabel = Label(self,text="bDO - Billing forecasting",background='white',foreground='green',font=zHeader1, pady=5)
        titleLabel.grid(row=0,columnspan=10,column=0,sticky='w')
        
        ######## Description ##########
        zFont1= font.Font(family="Helvetica",size=10)
        titleDescription = Label(self,text="Generate Billing Preview Run from Zuora and lookup the result with subscription data source",background='white',foreground='grey',font=zFont1,pady=5)
        titleDescription.grid(row=1,columnspan=10,column=0,sticky='w')

        base_folder = os.path.dirname(os.path.realpath(__file__))

        ######## Start New Process ##########             
        image_path = os.path.join(base_folder, 'bigGo.png')
        #print(image_path)
        self.bigGo = PhotoImage(file=image_path)

        startNew = Button(self, image=self.bigGo,command = self.startNewProcess) 
        startNew.grid(row=2,column=0)
        zFont2= font.Font(family="Helvetica",size=7)
        startNewLabel = Label(self,text="Start New Process",background='white',foreground='green',font=zFont1,pady=5)
        startNewLabel.grid(row=2,columnspan=4,column=1,sticky='w',pady=5)

        self.allInOneCheck = Checkbutton(
            self,
            variable=self.allInOneValue,onvalue="NewAllIn", offvalue="NewNotAllIn",background='white',command= lambda: self.changeButtonState(self.allInOneValue.get()))
        self.allInOneCheck.select()
        self.allInOneCheck.grid(row=2,column=4)
        allInOne = Label(self,text="All In One Step !",background='white',foreground='green')
        allInOne.grid(row=2,column=5)

        ######## Steps ##########
        image_path2 = os.path.join(base_folder, 'smallGo.png')
        self.smallGo = PhotoImage(file=image_path2)

        self.login = Button(self, image=self.smallGo,foreground='blue')
        self.login.grid(row=3,column=0)
        loginLabel = Label(self,text="Login",background='white',foreground='grey',font=zFont2,pady=5)
        loginLabel.grid(row=3,column=1,pady=5)

        self.launchBilling = Button(self, image=self.smallGo,foreground='blue')
        self.launchBilling.grid(row=3,column=2)
        launcBillingLabel = Label(self,text="Launch Billing Preview",background='white',foreground='grey',font=zFont2,pady=5)
        launcBillingLabel.grid(row=3,column=3)

        self.launchDataSource = Button(self, image=self.smallGo,foreground='blue')
        self.launchDataSource.grid(row=3,column=4)
        dataSourceLabel = Label(self,text="Launch Data source",background='white',foreground='grey',font=zFont2,pady=5)
        dataSourceLabel.grid(row=3,column=5)

        self.arrangeHeaders = Button(self, image=self.smallGo,foreground='blue')
        self.arrangeHeaders.grid(row=3,column=6)
        headersLabel = Label(self,text="Arrange Headers",background='white',foreground='grey',font=zFont2,pady=5)
        headersLabel.grid(row=3,column=7)

        self.finalize = Button(self, image=self.smallGo,foreground='blue')
        self.finalize.grid(row=3,column=8)
        finalizeLabel = Label(self,text="Finalize",background='white',foreground='grey',font=zFont2,pady=5)
        finalizeLabel.grid(row=3,column=9)

        ######## Frame ##########
        self.grid()
        self.configure(background='white') 

    def changeButtonState(self,state):
        #container = tk.Button(self)

        if state == 'New':
            currentState = 'disabled'
            for myWidget in (self.launchBilling, self.launchDataSource, self.arrangeHeaders, self.finalize,self.allInOneCheck, self.login):
                myWidget.config(state=currentState)
        elif state == 'NewAllIn':
            currentState = 'disabled'
            for myButton in (self.launchBilling, self.launchDataSource, self.arrangeHeaders, self.finalize):
                myButton.config(state=currentState)
            currentState = 'active'
            for myButton in (self.login, self.allInOneCheck):
                myButton.config(state=currentState)
        elif state == 'NewNotAllIn':
                    currentState = 'active'
                    for myButton in (self.launchBilling, self.launchDataSource, self.arrangeHeaders, self.finalize):
                        myButton.config(state=currentState)
        else :
            print('to be handle')

    def startNewProcess(self):
        if messagebox.askyesno("start New Process","You're about to start a new Process This will restart everything, including launching a new Billing Preview. Are you OK ?"):
            self.changeButtonState('NewAllIn')



def main():
    
    myWindow = Tk()
    myWindow.title("GoDigital Billing Preview Tool")
    myWindow.iconbitmap(r'C:\Users\sesa236189\source\repos\testPyvot_v1\testPyvot_v1\testPyvot_v1\images\lifeIsOn.ico')
    myWindow.configure(background='white')
    #myWindow.geometry('500x400') # Size 500, 400    

    #app = settingsFrame()
    #app2 = loginFrame()
    app3 = mainFrame()

    myWindow.mainloop()  


if __name__ == '__main__':
    main()   

