import pickle
import pyeq3

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt
from tkinter import filedialog as filedialog

import IndividualReports
import AdditionalInfo


class ResultsFrame(tk.Frame):
    
    def __init__(self, parent, pickledEquationFileName):
        tk.Frame.__init__(self, parent)
        
        self.graphReportsListForPDF = []
        self.textReportsListForPDF = []
        self.sourceCodeReportsListForPDF = []
        
        # first, load the fitted equation
        equationFile = open(pickledEquationFileName, 'rb')
        self.equation = pickle.load(equationFile)
        equationFile.close()
        
        topLevelNotebook = ttk.Notebook(self)
        topLevelNotebook.pack()

        # the "graph reports" notebook tab
        nbGraphReports = ttk.Notebook(topLevelNotebook)
        nbGraphReports.pack()
        topLevelNotebook.add(nbGraphReports, text='Graph Reports')

        if self.equation.GetDimensionality() == 2:
            report = IndividualReports.ModelScatterConfidenceGraph(nbGraphReports, self.equation, scatterplotOnlyFlag=False)
            reportTitle = "Model With 95% Confidence"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])

            report = IndividualReports.ModelScatterConfidenceGraph(nbGraphReports, self.equation, scatterplotOnlyFlag=True)
            reportTitle = "Scatter Plot"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])
        else:
            report = IndividualReports.SurfacePlot(nbGraphReports, self.equation)
            reportTitle = "Surface Plot"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])
            
            report = IndividualReports.ContourPlot(nbGraphReports, self.equation)
            reportTitle = "Contour Plot"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])

            report = IndividualReports.ScatterPlot(nbGraphReports, self.equation)
            reportTitle = "Scatter Plot"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])

        report = IndividualReports.AbsoluteErrorGraph(nbGraphReports, self.equation)
        reportTitle = "Absolute Error"
        nbGraphReports.add(report[0], text=reportTitle)
        self.graphReportsListForPDF.append([report[1], reportTitle])

        report = IndividualReports.AbsoluteErrorHistogram(nbGraphReports, self.equation)
        reportTitle = "Absolute Error Histogram"
        nbGraphReports.add(report[0], text=reportTitle)
        self.graphReportsListForPDF.append([report[1], reportTitle])

        if self.equation.dataCache.DependentDataContainsZeroFlag != 1:
            report = IndividualReports.PercentErrorGraph(nbGraphReports, self.equation)
            reportTitle = "Percent Error"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])

            report = IndividualReports.PercentErrorHistogram(nbGraphReports, self.equation)
            reportTitle = "Percent Error Histogram"
            nbGraphReports.add(report[0], text=reportTitle)
            self.graphReportsListForPDF.append([report[1], reportTitle])


        # the "text reports" notebook tab
        nbTextReports = ttk.Notebook(topLevelNotebook)
        nbTextReports.pack()
        topLevelNotebook.add(nbTextReports, text='Text Reports')
                
        report = IndividualReports.CoefficientAndFitStatistics(nbTextReports, self.equation)
        reportTitle = "Coefficient And Fit Statistics"
        nbTextReports.add(report, text=reportTitle)
        self.textReportsListForPDF.append([report.get("1.0", tk.END), reportTitle])
        
        report = IndividualReports.CoefficientListing(nbTextReports, self.equation)
        reportTitle = "Coefficient Listing"
        nbTextReports.add(report, text=reportTitle)
        self.textReportsListForPDF.append([report.get("1.0", tk.END), reportTitle])

        report = IndividualReports.DataArrayStatisticsReport(nbTextReports, 'Absolute Error Statistics', self.equation.modelAbsoluteError)
        reportTitle = "Absolute Error Statistics"
        nbTextReports.add(report, text=reportTitle)
        self.textReportsListForPDF.append([report.get("1.0", tk.END), reportTitle])
        
        if self.equation.dataCache.DependentDataContainsZeroFlag != 1:
            report = IndividualReports.DataArrayStatisticsReport(nbTextReports, 'Percent Error Statistics', self.equation.modelPercentError)
            reportTitle = "Percent Error Statistics"
            nbTextReports.add(report, text=reportTitle)
            self.textReportsListForPDF.append([report.get("1.0", tk.END), reportTitle])

        # the "source code" notebook tab
        nbSourceCodeReports = ttk.Notebook(topLevelNotebook)
        nbSourceCodeReports.pack()
        topLevelNotebook.add(nbSourceCodeReports, text='Source Code')
                    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation, 'CPP')
        reportTitle = "C++"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'CSHARP')
        reportTitle = "CSHARP"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'VBA')
        reportTitle = "VBA"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'PYTHON')
        reportTitle = "PYTHON"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'JAVA')
        reportTitle = "JAVA"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'JAVASCRIPT')
        reportTitle = "JAVASCRIPT"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'JULIA')
        reportTitle = "JULIA"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'SCILAB')
        reportTitle = "SCILAB"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'MATLAB')
        reportTitle = "MATLAB"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])
    
        report = IndividualReports.SourceCodeReport(nbSourceCodeReports, self.equation,'FORTRAN90')
        reportTitle = "FORTRAN90"
        nbSourceCodeReports.add(report, text=reportTitle)
        self.sourceCodeReportsListForPDF.append([report.get("1.0", tk.END), reportTitle + " Source Code"])

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

        # the "list of all standard equations" notebook tab
        dim = self.equation.GetDimensionality()
        allEquations = IndividualReports.AllEquationReport(topLevelNotebook, dim)
        allEquations.pack()
        topLevelNotebook.add(allEquations, text="List Of All Standard " + str(dim) + "D Equations")

        # the "Save To PDF" tab
        fsaveFrame = tk.Frame(self)
            
        # this label is only for visual spacing
        l = tk.Label(fsaveFrame, text="\n\n\n")
        l.pack()

        buttonSavePDF = tk.Button(fsaveFrame, text="Save To PDF", command=self.createPDF, height=0, width=0)
        buttonSavePDF.pack()
        topLevelNotebook.add(fsaveFrame, text="Save To PDF File")


    def createPDF(self):
        try:
            import reportlab
        except:
            tk_mbox.showerror("Error", "\nCould not import reportlab.\n\nPlease install using the command\n\n'pip3 install reportlab'")
            return

        # see https://bugs.python.org/issue22810 for the
        # "alloc: invalid block" error on application close 
        fName = filedialog.asksaveasfilename(
                                filetypes =(("PDF Files", "*.pdf"),("All Files","*.*")),
                                title = "PDF file name"
                                )
        if fName:
            import pdfCode
            pdfCode.CreatePDF(fName,
                              self.equation,
                              self.graphReportsListForPDF,
                              self.textReportsListForPDF,
                              self.sourceCodeReportsListForPDF
                              )
            tk_mbox.showinfo("Success", "\nSuccessfully created PDF file.")



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
