from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk
from module1 import connectionDetails, ZToken
import os

class settingsFrame(Frame):
    def __init__(self):
        super().__init__()
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

        loginProxy = Label(self,text="Use SE proxy : ",background='green',foreground='white')
        proxyCheck = Checkbutton(
            self,
            variable=self.proxyCheckValue,onvalue="Y", offvalue="N",command=self.checkClick,background='green')
        proxyCheck.select()
        
        loginEnvironment = Label(self,text="Environment : ",background='green',foreground='white')
        environmentList = ttk.Combobox(
                    self, textvariable=self.env,
                    values=("DEV", "INT", "UAT", "PrePROD", "PROD"), width=8)
        environmentList.bind("<<ComboboxSelected>>", self.envSelect)
    
        loginProxy.grid(column=0,row=0)
        proxyCheck.grid(column=1,row=0)
        loginEnvironment.grid(column=0, row=1)
        environmentList.grid(column=1, row=1)
        
        self.grid(column=0,row=0)
        self.configure(background='yellow')        
        #self.pack()    

class loginFrame(Frame):
    def __init__(self):
        super().__init__()
        self.loginVar = StringVar()
        self.passwordVar = StringVar()
        self.errMsg = StringVar()
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

        loginLabel = Label(self,text="Client Id : ",background='green',foreground='white')
        loginPassword = Label(self,text="Client Secret : ",background='green',foreground='white')      
        loginEntry = Entry(self,textvariable=self.loginVar)
        passwordEntry = Entry(self,show="*",textvariable=self.passwordVar)
        msgLabel = Label(self,textvariable=self.errMsg,background='green',foreground='white',wraplength=350,justify='left')



        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'button_login.png')
        loginImage = PhotoImage(file=image_path)
        #loginSubmitButton = Button(self, text="   Login   ", command=self.login)
        loginSubmitButton = Button(self, image=loginImage, command=self.login,bg='green',bd=0,activebackground ='green')

        loginLabel.grid(column=0,row=0)
        loginPassword.grid(column=0,row=1)
        loginEntry.grid(column=1,row=0)
        passwordEntry.grid(column=1,row=1)
        loginSubmitButton.grid(columnspan=2,row=2)
        msgLabel.grid(columnspan=2,row=3)

        self.grid(column=1,row=0)
        self.configure(background='red')
        #self.pack()

    
proxyUseCheck = "Y"
env = ''

def main():
    
    myWindow = Tk()
    myWindow.title("GoDigital Billing Preview Tool")
    myWindow.iconbitmap(r'C:\Users\sesa236189\source\repos\testPyvot_v1\testPyvot_v1\testPyvot_v1\images\lifeIsOn.ico')
    myWindow.configure(background='green')
    myWindow.geometry('500x400') # Size 500, 400    

    app = settingsFrame()
    app2 = loginFrame()

    myWindow.mainloop()  


if __name__ == '__main__':
    main()   

