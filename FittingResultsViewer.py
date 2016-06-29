import pickle
import pyeq3

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt

import IndividualReports
import AdditionalInfo

class ResultsFrame(tk.Frame):
    
    def __init__(self, parent, pickledEquationFileName):
        tk.Frame.__init__(self, parent)
        
        # first, load the fitted equation
        equationFile = open(pickledEquationFileName, 'rb')
        equation = pickle.load(equationFile)
        equationFile.close()
        
        topLevelNotebook = ttk.Notebook(self)
        topLevelNotebook.pack()

        # the "graph reports" notebook tab
        nbGraphReports = ttk.Notebook(topLevelNotebook)
        nbGraphReports.pack()
        topLevelNotebook.add(nbGraphReports, text='Graph Reports')

        if equation.GetDimensionality() == 2:
            report = IndividualReports.ModelScatterConfidenceGraph(nbGraphReports, equation)
            nbGraphReports.add(report, text="Model With 95%Confidence")
        else:
            report = IndividualReports.SurfacePlot(nbGraphReports, equation)
            nbGraphReports.add(report, text="Surface Plot")
            
            report = IndividualReports.ContourPlot(nbGraphReports, equation)
            nbGraphReports.add(report, text="Contour Plot")
            
            report = IndividualReports.ScatterPlot(nbGraphReports, equation)
            nbGraphReports.add(report, text="Scatter Plot")

        report = IndividualReports.AbsoluteErrorGraph(nbGraphReports, equation)
        nbGraphReports.add(report, text="Absolute Error")

        report = IndividualReports.AbsoluteErrorHistogram(nbGraphReports, equation)
        nbGraphReports.add(report, text="Absolute Error Histogram")

        if equation.dataCache.DependentDataContainsZeroFlag != 1:
            report = IndividualReports.PercentErrorGraph(nbGraphReports, equation)
            nbGraphReports.add(report, text="Percent Error")

            report = IndividualReports.PercentErrorHistogram(nbGraphReports, equation)
            nbGraphReports.add(report, text="Percent Error Histogram")


        # the "text reports" notebook tab
        nbTextReports = ttk.Notebook(topLevelNotebook)
        nbTextReports.pack()
        topLevelNotebook.add(nbTextReports, text='Text Reports')
                
        report = IndividualReports.CoefficientAndFitStatistics(nbTextReports, equation)
        nbTextReports.add(report, text="Coefficient And Fit Statistics")
        
        report = IndividualReports.CoefficientListing(nbTextReports, equation)
        nbTextReports.add(report, text="Coefficient Listing")

        report = IndividualReports.DataArrayStatisticsReport(nbTextReports, 'Absolute Error Statistics', equation.modelAbsoluteError)
        nbTextReports.add(report, text="Absolute Error Statistics")
        
        if equation.dataCache.DependentDataContainsZeroFlag != 1:
            report = IndividualReports.DataArrayStatisticsReport(nbTextReports, 'Percent Error Statistics', equation.modelPercentError)
            nbTextReports.add(report, text="Percent Error Statistics")

        # the "source code" notebook tab
        nbSourceCodeReports = ttk.Notebook(topLevelNotebook)
        nbSourceCodeReports.pack()
        topLevelNotebook.add(nbSourceCodeReports, text='Source Code')
                    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation, 'CPP')
        nbSourceCodeReports.add(report, text="C++")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'CSHARP')
        nbSourceCodeReports.add(report, text="CSHARP")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'VBA')
        nbSourceCodeReports.add(report, text="VBA")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'PYTHON')
        nbSourceCodeReports.add(report, text="PYTHON")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'JAVA')
        nbSourceCodeReports.add(report, text="JAVA")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'JAVASCRIPT')
        nbSourceCodeReports.add(report, text="JAVASCRIPT")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'JULIA')
        nbSourceCodeReports.add(report, text="JULIA")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'SCILAB')
        nbSourceCodeReports.add(report, text="SCILAB")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'MATLAB')
        nbSourceCodeReports.add(report, text="MATLAB")
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, equation,'FORTRAN90')
        nbSourceCodeReports.add(report, text="FORTRAN90")

        # the "additional information" notebook tab
        nbAdditionalInfo = ttk.Notebook(topLevelNotebook)
        nbAdditionalInfo.pack()
        topLevelNotebook.add(nbAdditionalInfo, text='Additional Information')
                
        scrolledText = tk_stxt.ScrolledText(nbAdditionalInfo, width=IndividualReports.textboxWidth, height=IndividualReports.textboxHeight, wrap=tk.WORD)
        nbAdditionalInfo.add(scrolledText, text="Fitting History")
        scrolledText.insert(tk.END, AdditionalInfo.history)

        scrolledText = tk_stxt.ScrolledText(nbAdditionalInfo, width=IndividualReports.textboxWidth, height=IndividualReports.textboxHeight, wrap=tk.WORD)
        nbAdditionalInfo.add(scrolledText, text="Author History")
        scrolledText.insert(tk.END, AdditionalInfo.author)

        scrolledText = tk_stxt.ScrolledText(nbAdditionalInfo, width=IndividualReports.textboxWidth, height=IndividualReports.textboxHeight, wrap=tk.WORD)
        nbAdditionalInfo.add(scrolledText, text="Web Links")
        scrolledText.insert(tk.END, AdditionalInfo.links)



if __name__ == "__main__":
    root = tk.Tk()
    interface = ResultsFrame(root, 'pickledEquationFile')
    interface.pack()
    root.title("Example tkinterFit -  Fitting Results Viewer")
    
    # manually center the application window on the user display
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2) # integer division
    y = (root.winfo_screenheight() // 2) - (height // 2) # integer division
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))        
        
    root.mainloop()
