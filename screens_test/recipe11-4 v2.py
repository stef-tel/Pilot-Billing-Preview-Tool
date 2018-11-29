import tkinter
from tkinter.messagebox import showinfo
from tkinter import *
import pandas as pd
from pandas import DataFrame, read_excel, read_csv, merge




class DDList(tkinter.Listbox):     
# A Tkinter listbox with drag'n'drop reordering of entries.  

    def __init__(self, master, **kw):
        kw['selectmode'] = tkinter.SINGLE
        tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None     

    def setCurrent(self, event):         
        self.curIndex = self.nearest(event.y)     

    def shiftSelection(self, event):         
        i = self.nearest(event.y)         
        if i < self.curIndex:
            print("i : " + str(i) + " - curIndex : " + str(self.curIndex))             
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            print("i : " + str(i) + " - curIndex : " + str(self.curIndex))             
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i
        



#generate file header asa list
df2 = read_csv("download/test_20181115_232308.csv", delimiter = ",")

cols = df2.columns.tolist()
columnSequence = {}

window = tkinter.Tk()
window.title("GoDigital Billing Preview Tool")
window.iconbitmap(r'C:\Users\sesa236189\source\repos\testPyvot_v1\testPyvot_v1\testPyvot_v1\images\lifeIsOn.ico')
        
columnList = DDList(window, height=len(cols), selectbackground='green',activestyle='none', selectforeground='white',width=50)     
#columnList.pack( )
columnList.grid(column=0, row=0)

for i in range(len(cols)):         
    columnSequence[cols[i]] = i
    columnList.insert(tkinter.END, cols[i])

def clicked():
    targetSequence = []
    i = 0
    for item in columnList.get(0,len(cols)):
        #print(item)
        #print(columnSequence[str(item)])
        targetSequence.append(columnSequence[str(item)])
        i += i
    print(columnList.get(0,len(cols)))
    print(targetSequence)
    #showinfo("Window", "Final Columns sequence : " + columnList.get(0,len(cols)))

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
	
#def show( ):         # show the current ordering every 2 seconds         
#	for x in dd.get(0, Tkinter.END):             
#	#print x,         
#	#print         
#	    tk.after(2000, show)     
#	    tk.after(2000, show)     

window.mainloop( )