import os, sys, queue, pickle, time, inspect
import pyeq3

import matplotlib # ensure this dependency imports for later use in fitting results

import tkinter as tk
import tkinter.ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt

import DataForControls as dfc
import FittingThread


class InterfaceFrame(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.queue = queue.Queue()

        self.equationSelect_2D = tk.IntVar()
        self.equationSelect_3D = tk.IntVar()
        self.fittingTargetSelect_2D = tk.IntVar()
        self.fittingTargetSelect_3D = tk.IntVar()

        # ROW 0 - empty labels as visual buffers
        row, col = (0, 0) # left edge
        l = tk.Label(self, text="   ")
        l.grid(column=col, row=row)
        row, col = (0, 2) # center
        l = tk.Label(self, text="     ")
        l.grid(column=col, row=row)
        row, col = (0, 4) # right edge
        l = tk.Label(self, text="   ")
        l.grid(column=col, row=row)
        
        # ROW 1 - text data entry labels
        # no "self" needed as no later references exist
        row, col = (1, 1)
        l = tk.Label(self, text="--- 2D Data Text Editor ---", font="-weight bold")
        l.grid(column=col, row=row)
        
        row, col = (1, 3)
        l = tk.Label(self, text="--- 3D Data Text Editor ---", font="-weight bold")
        l.grid(column=col, row=row)

        # ROW 2 - text data input, no line wrap
        row, col = (2, 1)
        self.text_2D = tk_stxt.ScrolledText(self, width=45, height=12, wrap=tk.NONE)
        self.text_2D.insert(tk.END, dfc.exampleText_2D) # inital text data
        self.text_2D.grid(column=col, row=row, sticky=(tk.N, tk.W, tk.E, tk.S))

        row, col = (2, 3)
        self.text_3D = tk_stxt.ScrolledText(self, width=45, height=12, wrap=tk.NONE)
        self.text_3D.insert(tk.END, dfc.exampleText_3D) # inital text data
        self.text_3D.grid(column=col, row=row, sticky=(tk.N, tk.W, tk.E, tk.S))

        # ROW 3 - empty label as visual buffer
        row, col = (3, 0)
        l = tk.Label(self, text=" ")
        l.grid(column=col, row=row)

        # ROW 4 - equation selection labels
        # no "self" needed as no later references exist
        row, col = (4, 1)
        l = tk.Label(self, text="--- Standard 2D Equations ---", font="-weight bold")
        l.grid(column=col, row=row)
        
        row, col = (4, 3)
        l = tk.Label(self, text="--- Standard 3D Equations ---", font="-weight bold")
        l.grid(column=col, row=row)

        # ROW 5 - equation selection
        row, col = (5, 1)
        f = tk.Frame(self)
        f.grid(column=col, row=row)
        self.cb_Modules2D = tk.ttk.Combobox(f, state='readonly')
        self.cb_Modules2D['values'] = sorted(list(dfc.eq_od2D.keys()))
        self.cb_Modules2D.bind("<<ComboboxSelected>>", self.moduleSelectChanged_2D)
        self.cb_Modules2D.set('Polynomial')
        self.cb_Modules2D.pack(anchor=tk.W)

        self.cb_Equations2D = tk.ttk.Combobox(f, state='readonly')
        self.cb_Equations2D['width'] = 50
        self.cb_Equations2D['values'] = sorted(list(dfc.eq_od2D['Polynomial'].keys()))
        self.cb_Equations2D.set('1st Order (Linear)')
        self.cb_Equations2D.pack(anchor=tk.W)

        row, col = (5, 3)
        f = tk.Frame(self)
        f.grid(column=col, row=row)        
        self.cb_Modules3D = tk.ttk.Combobox(f, state='readonly')
        self.cb_Modules3D['values'] = sorted(list(dfc.eq_od3D.keys()))
        self.cb_Modules3D.bind("<<ComboboxSelected>>", self.moduleSelectChanged_3D)
        self.cb_Modules3D.set('Polynomial')
        self.cb_Modules3D.pack(anchor=tk.W)

        self.cb_Equations3D = tk.ttk.Combobox(f, state='readonly')
        self.cb_Equations3D['width'] = 50
        self.cb_Equations3D['values'] = sorted(list(dfc.eq_od3D['Polynomial'].keys()))
        self.cb_Equations3D.set('Linear')
        self.cb_Equations3D.pack(anchor=tk.W)

        # ROW 6 - empty label as visual buffer
        row, col = (6, 0)
        l = tk.Label(self, text=" ")
        l.grid(column=col, row=row)

        # ROW 7 - fitting target selection labels
        # no "self" needed as no later references exist
        row, col = (7, 1)
        l = tk.Label(self, text="--- Fitting Target 2D ---", font="-weight bold")
        l.grid(column=col, row=row)
        
        row, col = (7, 3)
        l = tk.Label(self, text="--- Fitting Target 3D ---", font="-weight bold")
        l.grid(column=col, row=row)

        # ROW 8 - fitting target selection radio buttons
        row, col = (8, 1)
        f = tk.Frame(self)
        f.grid(column=col, row=row)        
        index=0
        for fittingTargetText in dfc.fittingTargetList:
            rb = tk.Radiobutton(f, text=fittingTargetText, variable=self.fittingTargetSelect_2D, value=index)
            rb.pack(anchor=tk.W)
            index += 1

        row, col = (8, 3)
        f = tk.Frame(self)
        f.grid(column=col, row=row)        
        index=0
        for fittingTargetText in dfc.fittingTargetList:
            rb = tk.Radiobutton(f, text=fittingTargetText, variable=self.fittingTargetSelect_3D, value=index)
            rb.pack(anchor=tk.W)
            index += 1
    
            # ROW 9 - empty label as visual buffer
            row, col = (9, 0)
            l = tk.Label(self, text=" ")
            l.grid(column=col, row=row)
    
        # ROW 10 - fitting buttons
        row, col = (10, 1)
        self.buttonFit_2D = tk.Button(self, text="Fit 2D Text Data", command=self.OnFit_2D)
        self.buttonFit_2D.grid(column=col, row=row)
    
        row, col = (10, 3)
        self.buttonFit_3D = tk.Button(self, text="Fit 3D Text Data", command=self.OnFit_3D)
        self.buttonFit_3D.grid(column=col, row=row)

        # ROW 11 - empty label as visual buffer
        row, col = (11, 0)
        l = tk.Label(self, text=" ")
        l.grid(column=col, row=row)
        
        # now bind our custom ""status_update"" event to the handler function
        self.bind('<<status_update>>', self.StatusUpdateHandler)


    def moduleSelectChanged_2D(self, event):
        self.cb_Equations2D['values'] = sorted(list(dfc.eq_od2D[event.widget.get()].keys()))
        self.cb_Equations2D.current(0)


    def moduleSelectChanged_3D(self, event):
        self.cb_Equations3D['values'] = sorted(list(dfc.eq_od3D[event.widget.get()].keys()))
        self.cb_Equations3D.current(0)


    def OnFit_2D(self):
        textData = self.text_2D.get("1.0", tk.END)
        moduleSelection = self.cb_Modules2D.get()
        equationSelection = self.cb_Equations2D.get()
        fittingTargetSelection = dfc.fittingTargetList[self.fittingTargetSelect_2D.get()]
        
        # the GUI's fitting target string contains what we need - extract it
        fittingTarget = fittingTargetSelection.split('(')[1].split(')')[0]

        item = dfc.eq_od2D[moduleSelection][equationSelection]
        eqString = 'pyeq3.Models_2D.' + moduleSelection + '.' + item[0] + "('" + fittingTarget + "','" + item[1] + "')"
        self.equation = eval(eqString)

        # convert text to numeric data checking for log of negative numbers, etc.
        try:
            pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(textData, self.equation, False)
        except:
            tk_mbox.showerror("Error", self.equation.reasonWhyDataRejected)
            return

        # check for number of coefficients > number of data points to be fitted
        coeffCount = len(self.equation.GetCoefficientDesignators())
        dataCount = len(self.equation.dataCache.allDataCacheDictionary['DependentData'])
        if coeffCount > dataCount:
            tk_mbox.showerror("Error", "This equation requires a minimum of " + str(coeffCount) + " data points, you have supplied " + repr(dataCount) + ".")
            return
        
        # Now the status dialog is used. Disable fitting buttons until thread completes
        self.buttonFit_2D.config(state=tk.DISABLED)
        self.buttonFit_3D.config(state=tk.DISABLED)
        
        # create simple top-level text dialog to display status as fitting progresses
        # when the fitting thread completes, it will close the status box
        self.statusBox = tk.Toplevel()
        self.statusBox.title("Fitting Status")
        self.statusBox.text = tk.Text(self.statusBox)
        self.statusBox.text.pack()
        
        # in tkinter the status box must be manually centered
        self.statusBox.update_idletasks()
        width = self.statusBox.winfo_width()
        height = self.statusBox.winfo_height()
        x = (self.statusBox.winfo_screenwidth() // 2) - (width // 2) # integer division
        y = (self.statusBox.winfo_screenheight() // 2) - (height // 2) # integer division
        self.statusBox.geometry('{}x{}+{}+{}'.format(width, height, x, y))        

        # thread will automatically start to run
        # "status update" handler will re-enable buttons
        self.fittingWorkerThread = FittingThread.FittingThread(self, self.equation)


    def OnFit_3D(self):
        textData = self.text_3D.get("1.0", tk.END)
        moduleSelection = self.cb_Modules3D.get()
        equationSelection = self.cb_Equations3D.get()
        fittingTargetSelection = dfc.fittingTargetList[self.fittingTargetSelect_3D.get()]
        
        # the GUI's fitting target string contains what we need - extract it
        fittingTarget = fittingTargetSelection.split('(')[1].split(')')[0]

        item = dfc.eq_od3D[moduleSelection][equationSelection]
        eqString = 'pyeq3.Models_3D.' + moduleSelection + '.' + item[0] + "('" + fittingTarget + "','" + item[1] + "')"
        self.equation = eval(eqString)

        # convert text to numeric data checking for log of negative numbers, etc.
        try:
            pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(textData, self.equation, False)
        except:
            tk_mbox.showerror("Error", self.equation.reasonWhyDataRejected)
            return

        # check for number of coefficients > number of data points to be fitted
        coeffCount = len(self.equation.GetCoefficientDesignators())
        dataCount = len(self.equation.dataCache.allDataCacheDictionary['DependentData'])
        if coeffCount > dataCount:
            tk_mbox.showerror("Error", "This equation requires a minimum of " + str(coeffCount) + " data points, you have supplied " + repr(dataCount) + ".")
            return
        
        # Now the status dialog is used. Disable fitting buttons until thread completes
        self.buttonFit_2D.config(state=tk.DISABLED)
        self.buttonFit_3D.config(state=tk.DISABLED)
        
        # create simple top-level text dialog to display status as fitting progresses
        # when the fitting thread completes, it will close the status box
        self.statusBox = tk.Toplevel()
        self.statusBox.title("Fitting Status")
        self.statusBox.text = tk.Text(self.statusBox)
        self.statusBox.text.pack()
        
        # in tkinter the status box must be manually centered
        self.statusBox.update_idletasks()
        width = self.statusBox.winfo_width()
        height = self.statusBox.winfo_height()
        x = (self.statusBox.winfo_screenwidth() // 2) - (width // 2) # integer division
        y = (self.statusBox.winfo_screenheight() // 2) - (height // 2) # integer division
        self.statusBox.geometry('{}x{}+{}+{}'.format(width, height, x, y))        

        # thread will automatically start to run
        # "status update" handler will re-enable buttons
        self.fittingWorkerThread = FittingThread.FittingThread(self, self.equation)


    # When "status_update" event is generated, get
    # text data from queue and display it to the user.
    # If the queue data is not text, it is the fitted equation.
    def StatusUpdateHandler(self, *args):
        data = self.queue.get_nowait()
        
        if type(data) == type(''): # text is used for status box display to user
            self.statusBox.text.insert(tk.END, data + '\n')
        else: # the queue data is now the fitted equation.
            # write the fitted equation to a pickle file.  This
            # allows the possibility of archiving the fitted equations
            pickledEquationFile = open("pickledEquationFile", "wb")
            pickle.dump(data, pickledEquationFile)
            pickledEquationFile.close()
    
            # view fitting results
            p = os.popen(sys.executable + ' FittingResultsViewer.py')
            p.close()

            # re-enable fitting buttons
            self.buttonFit_2D.config(state=tk.NORMAL)
            self.buttonFit_3D.config(state=tk.NORMAL)
        
            # destroy the now-unused status box
            self.statusBox.destroy()
            


if __name__ == "__main__":
    root = tk.Tk()
    interface = InterfaceFrame(root)
    interface.pack()
    root.title("tkinterFit - Curve And Surface Fitting Interface")
    
    # manually center the application window on the user display
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2) # integer division
    y = (root.winfo_screenheight() // 2) - (height // 2) # integer division
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))        
    
    root.mainloop()
