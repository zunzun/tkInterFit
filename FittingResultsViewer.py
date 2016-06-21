import pickle
import pyeq3
import matplotlib

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt

import IndividualReports


class ResultsFrame(tk.Frame):
    
    def __init__(self, parent, pickledEquationFileName):
        tk.Frame.__init__(self, parent)
        
        # first, load the fitted equation
        equationFile = open(pickledEquationFileName, 'rb')
        equation = pickle.load(equationFile)
        equationFile.close()
        
        topLevelNotebook = ttk.Notebook(self)
        topLevelNotebook.pack()

        nbTextReports = ttk.Notebook(topLevelNotebook)
        nbTextReports.pack()
        topLevelNotebook.add(nbTextReports, text='Text Reports')
                
        report = IndividualReports.CoefficientAndFitStatistics(nbTextReports, equation)
        nbTextReports.add(report, text="Coefficient And Fit Statistics")
        
        report = IndividualReports.CoefficientListing(nbTextReports, equation)
        nbTextReports.add(report, text="Coefficient Listing")



if __name__ == "__main__":
    root = tk.Tk()
    interface = ResultsFrame(root, 'pickledEquationFile')
    interface.pack()
    root.title("Example tkinterFit -  Fitting Results Viewer")
    
    # manually center the application window on the user display
    #root.update_idletasks()
    #width = root.winfo_width()
    #height = root.winfo_height()
    #x = (root.winfo_screenwidth() // 2) - (width // 2) # integer division
    #y = (root.winfo_screenheight() // 2) - (height // 2) # integer division
    #root.geometry('{}x{}+{}+{}'.format(width, height, x, y))        
    root.minsize(width=666, height=666)
    root.maxsize(width=666, height=666)    
        
    root.mainloop()
