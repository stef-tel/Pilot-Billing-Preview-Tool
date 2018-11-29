
import tkinter as tk
from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk
from module1 import connectionDetails, ZToken

class mainFrame(Frame):
    def __init__(self):
        super().__init__()
        self.mainWidgets()

    def mainWidgets(self):
        #self.columnconfigure(0, pad=3)
        #self.columnconfigure(1, pad=3)
        #self.rowconfigure(0, pad=3)
        #self.rowconfigure(1, pad=3)

        self.settingsF = settingsFrame(self)
        self.settingsF.grid(row=0, column=0,sticky='n',pady=10,padx=30)
        self.loginF = loginFrame(self)
        self.loginF.grid(row=0, column=1,pady=10,padx=30)
        self.startButton = Button(self, text="   start   ", command=self.start)
        self.startButton2 = Button(self, text="   start2   ", command=self.start)
        self.startButton3 = Button(self, text="   start   ", command=self.start)
        self.startButton4 = Button(self, text="   start2   ", command=self.start)
        self.startButton.grid(row=1,column=0)
        self.startButton2.grid(row=1,column=1)
        self.startButton3.grid(row=1,column=2)
        self.startButton4.grid(row=1,column=3)
        self.grid(columnspan=4, pady=10)
        self.configure(background='yellow') 

    def start(self):
        print("coucou")

class settingsFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.proxyCheckValue = StringVar()
        self.env = StringVar()
        self.initUI()
        #self.clientId
          
    def checkClick(self):
        global proxyUseCheck
        proxyUseCheck = self.proxyCheckValue.get()
        env = self.env.get()

    def envSelect(self,event):
        global env
        env = self.env.get()

    def initUI(self):
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        loginProxy = Label(self,text="Use SE proxy : ",background='white',foreground='green')
        proxyCheck = Checkbutton(
            self,
            variable=self.proxyCheckValue,onvalue="Y", offvalue="N",command=self.checkClick,background='white')
        proxyCheck.select()
        
        loginEnvironment = Label(self,text="Environment : ",background='white',foreground='green')
        environmentList = ttk.Combobox(
                    self, textvariable=self.env,
                    values=("DEV", "INT", "UAT", "PrePROD", "PROD"), width=8)
        environmentList.bind("<<ComboboxSelected>>", self.envSelect)
    
        loginProxy.grid(column=0,row=0)
        proxyCheck.grid(column=1,row=0)
        loginEnvironment.grid(column=0, row=1)
        environmentList.grid(column=1, row=1)
        
        #self.grid(column=0,row=0)
        self.configure(background='white',width=200, height=500)        
        #self.pack()    

class loginFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        self.loginVar = StringVar()
        self.passwordVar = StringVar()
        self.errMsg = StringVar()
        self.parent = parent
        self.initUI()
        #self.clientId

    def checkSettings(self):
        global env
        if self.loginVar.get() == "" or self.passwordVar.get() == "" or env == "":
            return False
        else :
            return True
          
    def login(self):
        global proxyUseCheck, env

        if self.checkSettings():
            myConnectionDetails = connectionDetails(self.loginVar.get(),self.passwordVar.get(),proxyUseCheck,env)
            myZToken = ZToken()
            myZToken.generate(myConnectionDetails)
            if myZToken.status == '200':
                self.errMsg.set("auth. successful, token : " + myZToken.token)
                print("Token is : " + myZToken.token)
            else:
                self.errMsg.set("auth. failure : " + myZToken.errorMsg)
                print("auth. failure : " + myZToken.errorMsg)
        else:
            self.errMsg.set("missing parameters, please check connection settings")
            print("missing parameters")

    def initUI(self):  
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)

        loginLabel = Label(self,text="Client Id : ",background='white',foreground='green')
        loginPassword = Label(self,text="Client Secret : ",background='white',foreground='green')      
        loginEntry = Entry(self,textvariable=self.loginVar)
        passwordEntry = Entry(self,show="*",textvariable=self.passwordVar)
        msgLabel = Label(self,textvariable=self.errMsg,background='white',foreground='green',wraplength=350,justify='left')

        loginSubmitButton = Button(self, text="   Login   ", command=self.login,foreground='blue')

        loginLabel.grid(column=0,row=0,sticky=W)
        loginPassword.grid(column=0,row=1,sticky=W)
        loginEntry.grid(column=1,row=0,sticky=W)
        passwordEntry.grid(column=1,row=1,sticky=W)
        loginSubmitButton.grid(columnspan=2,row=2, pady=10)
        msgLabel.grid(columnspan=3,row=3)

        #self.grid(column=1,row=0)
        self.configure(background='white',width=200, height=500)
        #self.pack()

#global variables for being used between frames ==> to be checked if parent/child object relation would not be better    
proxyUseCheck = "Y"
env = ''

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

