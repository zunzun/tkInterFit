import pickle
import pyeq3
import matplotlib

import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as tk_mbox
import tkinter.scrolledtext as tk_stxt



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
    scrolledText = tk_stxt.ScrolledText(parent, width=60, height=12, wrap=tk.NONE)
    cd = equation.GetCoefficientDesignators()
    for i in range(len(equation.solvedCoefficients)):
        scrolledText.insert(tk.END, "%s = %-.16E\n" % (cd[i], equation.solvedCoefficients[i]))

    return scrolledText


def AbsoluteErrorListing(parent, equation):
    scrolledText = tk_stxt.ScrolledText(parent, width=60, height=12, wrap=tk.NONE)
    cd = equation.GetCoefficientDesignators()
    for i in range(len(equation.solvedCoefficients)):
        scrolledText.insert(tk.END, "%s = %-.16E\n" % (cd[i], equation.solvedCoefficients[i]))

    return scrolledText
    
