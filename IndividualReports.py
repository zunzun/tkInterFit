import pickle
import pyeq3
import numpy, scipy

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt


textboxWidth = 60 # units are characters
textboxHeight = 12 # units are characters

graphWidth = 800 # units are pixels
graphHeight = 600 # units are pixels

# this is used in several reports
def DataArrayStatisticsReport(parent, titleString, tempdata):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)
    scrolledText.insert(tk.END, titleString + '\n\n')
    
    # must at least have max and min
    minData = min(tempdata)
    maxData = max(tempdata)
    
    if maxData == minData:
        scrolledText.insert(tk.END, 'All data has the same value,\n')
        scrolledText.insert(tk.END, "value = %-.16E\n" % (minData))
        scrolledText.insert(tk.END, 'statistics cannot be calculated.')
    else:
        scrolledText.insert(tk.END, "max = %-.16E\n" % (maxData))
        scrolledText.insert(tk.END, "min = %-.16E\n" % (minData))
        
        try:
            temp = scipy.mean(tempdata)
            scrolledText.insert(tk.END, "mean = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "mean gave error in calculation\n")

        try:
            temp = scipy.stats.sem(tempdata)
            scrolledText.insert(tk.END, "standard error of mean = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "standard error of mean gave error in calculation\n")

        try:
            temp = scipy.median(tempdata)
            scrolledText.insert(tk.END, "median = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "median gave error in calculation\n")

        try:
            temp = scipy.var(tempdata)
            scrolledText.insert(tk.END, "variance = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "variance gave error in calculation\n")

        try:
            temp = scipy.std(tempdata)
            scrolledText.insert(tk.END, "std. deviation = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "std. deviation gave error in calculation\n")

        try:
            temp = scipy.stats.skew(tempdata)
            scrolledText.insert(tk.END, "skew = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "skew gave error in calculation\n")

        try:
            temp = scipy.stats.kurtosis(tempdata)
            scrolledText.insert(tk.END, "kurtosis = %-.16E\n" % (temp))
        except:
            scrolledText.insert(tk.END, "kurtosis gave error in calculation\n")
            
    return scrolledText
    

def CoefficientAndFitStatistics(parent, equation):
    scrolledText = tk_stxt.ScrolledText(parent, width=80, height=25, wrap=tk.NONE)
    if equation.upperCoefficientBounds or equation.lowerCoefficientBounds:
        scrolledText.insert(tk.END, 'This model has coefficient bounds. Parameter statistics may\n')
        scrolledText.insert(tk.END, 'not be valid for parameter values at or near the bounds.\n')
        scrolledText.insert(tk.END, '\n')
    
    scrolledText.insert(tk.END, 'Degress of freedom error ' + str(equation.df_e) + '\n')
    scrolledText.insert(tk.END, 'Degress of freedom regression ' + str(equation.df_r) + '\n')
    
    if equation.rmse == None:
        scrolledText.insert(tk.END, 'Root Mean Squared Error (RMSE): n/a\n')
    else:
        scrolledText.insert(tk.END, 'Root Mean Squared Error (RMSE): ' + str(equation.rmse) + '\n')
    
    if equation.r2 == None:
        scrolledText.insert(tk.END, 'R-squared: n/a\n')
    else:
        scrolledText.insert(tk.END, 'R-squared: ' + str(equation.r2) + '\n')
    
    if equation.r2adj == None:
        scrolledText.insert(tk.END, 'R-squared adjusted: n/a\n')
    else:
        scrolledText.insert(tk.END, 'R-squared adjusted: ' + str(equation.r2adj) + '\n')
    
    if equation.Fstat == None:
        scrolledText.insert(tk.END, 'Model F-statistic: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model F-statistic: ' + str(equation.Fstat) + '\n')
    
    if equation.Fpv == None:
        scrolledText.insert(tk.END, 'Model F-statistic p-value: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model F-statistic p-value: ' + str(equation.Fpv) + '\n')
    
    if equation.ll == None:
        scrolledText.insert(tk.END, 'Model log-likelihood: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model log-likelihood: ' + str(equation.ll) + '\n')
    
    if equation.aic == None:
        scrolledText.insert(tk.END, 'Model AIC: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model AIC: ' + str(equation.aic) + '\n')
    
    if equation.bic == None:
        scrolledText.insert(tk.END, 'Model BIC: n/a\n')
    else:
        scrolledText.insert(tk.END, 'Model BIC: ' + str(equation.bic) + '\n')
    
    
    scrolledText.insert(tk.END, '\n')
    scrolledText.insert(tk.END, "Individual Parameter Statistics:\n")
    for i in range(len(equation.solvedCoefficients)):
        if equation.tstat_beta == None:
            tstat = 'n/a'
        else:
            tstat = '%-.5E' %  ( equation.tstat_beta[i])
    
        if equation.pstat_beta == None:
            pstat = 'n/a'
        else:
            pstat = '%-.5E' %  ( equation.pstat_beta[i])
    
        if equation.sd_beta != None:
            scrolledText.insert(tk.END, "Coefficient %s = %-.16E, std error: %-.5E\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i], equation.sd_beta[i]))
        else:
            scrolledText.insert(tk.END, "Coefficient %s = %-.16E, std error: n/a\n" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
        scrolledText.insert(tk.END, "          t-stat: %s, p-stat: %s, 95 percent confidence intervals: [%-.5E, %-.5E]\n" % (tstat,  pstat, equation.ci[i][0], equation.ci[i][1]))
            
    scrolledText.insert(tk.END, '\n')
    scrolledText.insert(tk.END, "Coefficient Covariance Matrix:\n")
    for i in  equation.cov_beta:
        scrolledText.insert(tk.END, str(i) + '\n')
        
    return scrolledText


def CoefficientListing(parent, equation):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)
    cd = equation.GetCoefficientDesignators()
    for i in range(len(equation.solvedCoefficients)):
        scrolledText.insert(tk.END, "%s = %-.16E\n" % (cd[i], equation.solvedCoefficients[i]))

    return scrolledText


def SourceCodeReport(parent, equation, lanuageNameString):
    scrolledText = tk_stxt.ScrolledText(parent, width=textboxWidth, height=textboxHeight, wrap=tk.NONE)    
    code = eval('pyeq3.outputSourceCodeService().GetOutputSourceCode' + lanuageNameString + '(equation)')
    scrolledText.insert(tk.END, code)
    
    return scrolledText


def AbsoluteErrorGraph(parent, equation):
    f = Figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)
    dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
    abs_error = equation.modelAbsoluteError
    axes.plot(dep_data, abs_error, 'D')
    
    if equation.GetDimensionality() == 2: # used for labels only
        axes.set_title('Absolute Error vs. X Data')
        axes.set_xlabel('X Data')
    else:
        axes.set_title('Absolute Error vs. Z Data')
        axes.set_xlabel('Z Data')
        
    axes.set_ylabel(" Absolute Error") # Y axis label is always absolute error

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=parent)
    canvas.show()
    return canvas.get_tk_widget()


def PercentErrorGraph(parent, equation):
    f = Figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)
    dep_data = equation.dataCache.allDataCacheDictionary['DependentData']
    per_error = equation.modelPercentError
    axes.plot(dep_data, per_error, 'D')
    
    if equation.GetDimensionality() == 2: # used for labels only
        axes.set_title('Percent Error vs. X Data')
        axes.set_xlabel('X Data')
    else:
        axes.set_title('Percent Error vs. Z Data')
        axes.set_xlabel('Z Data')
        
    axes.set_ylabel(" Percent Error") # Y axis label is always percent error

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=parent)
    canvas.show()
    return canvas.get_tk_widget()


def AbsoluteErrorHistogram(parent, equation):
    f = Figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)
    abs_error = equation.modelAbsoluteError
    bincount = len(abs_error)//2 # integer division
    if bincount < 5:
        bincount = 5
    if bincount > 25:
        bincount = 25
    n, bins, patches = axes.hist(abs_error, bincount, rwidth=0.8)
    
    # some axis space at the top of the graph
    ylim = axes.get_ylim()
    if ylim[1] == max(n):
        axes.set_ylim(0.0, ylim[1] + 1)

    axes.set_title('Absolute Error Histogram') # add a title
    axes.set_xlabel('Absolute Error') # X axis data label
    axes.set_ylabel(" Frequency") # Y axis label is frequency

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=parent)
    canvas.show()
    return canvas.get_tk_widget()


def PercentErrorHistogram(parent, equation):
    f = Figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)
    per_error = equation.modelPercentError
    bincount = len(per_error)//2 # integer division
    if bincount < 5:
        bincount = 5
    if bincount > 25:
        bincount = 25
    n, bins, patches = axes.hist(per_error, bincount, rwidth=0.8)
    
    # some axis space at the top of the graph
    ylim = axes.get_ylim()
    if ylim[1] == max(n):
        axes.set_ylim(0.0, ylim[1] + 1)

    axes.set_title('Percent Error Histogram') # add a title
    axes.set_xlabel('Percent Error') # X axis data label
    axes.set_ylabel(" Frequency") # Y axis label is frequency

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=parent)
    canvas.show()
    return canvas.get_tk_widget()

