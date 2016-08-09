import os, sys, time, threading

import pyeq3


class FittingThread(threading.Thread):
    def __init__(self, notify_window, equation):
        threading.Thread.__init__(self)
        self.notify_window = notify_window
        self.equation = equation
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()


    def run(self):

        statusString = 'Fitting data...'
        self.notify_window.queue.put(statusString)
        self.notify_window.event_generate('<<status_update>>')
        time.sleep(0.5) # allow users a moment to see the update
        self.equation.Solve()
    
        statusString = 'Calculating model errors...'
        self.notify_window.queue.put(statusString)
        self.notify_window.event_generate('<<status_update>>')
        time.sleep(0.5) # allow users a moment to see the update
        self.equation.CalculateModelErrors(self.equation.solvedCoefficients, self.equation.dataCache.allDataCacheDictionary)
    
        statusString = 'Calculating coefficient and fit statistics...'
        self.notify_window.queue.put(statusString)
        self.notify_window.event_generate('<<status_update>>')
        time.sleep(0.5) # allow users a moment to see the update
        self.equation.CalculateCoefficientAndFitStatistics()

        statusString = 'Fitting complete, creating graphs and reports...'
        self.notify_window.queue.put(statusString)
        self.notify_window.event_generate('<<status_update>>')
        time.sleep(0.5) # allow users a moment to see the update
        
        # the fitted equation is now the queue's event data, rather than
        # a status update string.  The event handler checks the data type
        self.notify_window.queue.put(self.equation)
        self.notify_window.event_generate('<<status_update>>')
