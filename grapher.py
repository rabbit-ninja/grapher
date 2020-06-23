from tkinter import *
from tkinter import filedialog 
import pandas as pd
import csv

version='Grapher Version: 0.01'
class grapher(object):
    def __init__(self):
        self.filename=filedialog.askopenfilename(title="Select A CSV File", filetypes=(("CSV files", "*.csv"),("all files", "*.*")))        
    def fileloc(self):
        path=self.filename
        return path
def pro():
    graph=grapher()
    fpath=str(graph.fileloc())
    with open(fpath) as f:
        reader = csv.reader(f)
        #header_row is a list of column headers of the table
        header_row = next(reader) 
        data = pd.read_csv(fpath, 'rb', error_bad_lines=False,  engine='python')
        selector = {header_row[k]: k for k in range(len(header_row))} #cerates a dictionary with index for header (useful for future extension)
        #======file name=====
        fname_temp=fpath.strip().split('/')
        fname=str(fname_temp[len(fname_temp)-1])
        #clearing list for memory optimisation
        del fname_temp[:] 
        print("======================Done till fname=========")
        #===================================
        OPTIONS = list(selector)
        variable1 = StringVar(root)
        variable1.set(OPTIONS[0]) # default value
        w1 = OptionMenu(root, variable1, *OPTIONS)
        w1.pack()
        #======================================
        #============drop down 2=============
        variable2 = StringVar(root)
        variable2.set(OPTIONS[0]) # default value
        w2 = OptionMenu(root, variable2, *OPTIONS)
        w2.pack()
    
        def submit():
            #taking string values from drop-downs
            x_value=selector[str(variable1.get())]
            y_value=selector[str(variable2.get())]
            #taking column values from CSV file as list
            x=list(data[header_row[x_value]])
            y=list(data[header_row[y_value]])
            #print(x)
            #print(y)
            #======Plotting Graph===============
            from matplotlib import pyplot as plt
            import numpy as np
            #========Icon======
            plt.Figure()
            plt.figure(num=version +': '+ fname)
            thismanager = plt.get_current_fig_manager()
            thismanager.window.wm_iconbitmap("icon.ico")
            #========Icon End==
            plt.plot(x,y)
            plt.xlabel(str(header_row[x_value]))
            plt.ylabel(str(header_row[y_value]))
            plt.title(fname)
            plt.show()
            del x[:], y[:] #clearing list for memory optimisation
        #===========Button to display Graph====
        button = Button(root, text="Graph", command=submit)
        button.pack()
        #====================================
        

root = Tk()
root.iconbitmap(r'icon.ico')
root.title(version)
root.geometry("600x600")
my_btn = Button(root, text="Open File", command=pro).pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()