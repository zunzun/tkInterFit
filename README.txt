Welcome to tkInterFit, an example of creating a
cross-platform curve and surface fitting application 
using tkinter and the pyeq3 fitting library.
see http://commonproblems.readthedocs.io/en/latest/


If you prefer wxPython, the wxPython version of this code
is at: https://github.com/zunzun/wxPythonFit


Step 1: Install Python 3, tk, scipy and matplotlib

On Debian or Ubuntu Linux, you can use this command:

sudo apt-get install python3-tk python3-scipy python3-matplotlib

On other operating systems, try the Canopy Express Free version:

https://store.enthought.com/


NOTE: if you would like to create PDF files of the fitting results,
please also install reportlab using pip:

pip3 install reportlab



Step 2: Install the pyeq3 fitting library with pip

From a command prompt, run the command

pip3 install pyeq3



Step 3: Run the tkInterFit example

From a command prompt run this command:

python3 tkInterFit.py



Step 4: Celebrate

You are now curve and surface fitting data using tkinter!



You may also be interested in the django version, which
includes PDF files, surface rotations and "function finding".
It is available at https://github.com/zunzun/zunzunsite3


Prior to the invention of electronic calculation, only manual methods
were available, of course - meaning that creating mathematical models
from experimental data was done by hand.  Even Napier's invention of
logarithms did not help much in reducing the tediousness of this task.
Linear regression techniques worked, but how to then compare models?
And so the F-statistic was created for the purpose of model selection,
since graphing models and their confidence intervals was practically
out of the question.  Forward and backward regression techniques used
linear methods, requiring less calculation than nonlinear methods, but
limited the possible mathematical models to linear combinations
of functions.

With the advent of computerized calculations, nonlinear methods which
were impractical in the past could be automated and made practical.
However, the nonlinear fitting methods all required starting points
for their solvers - meaning in practice you had to have a good idea of
the final equation parameters to begin with!

If however a genetic or monte carlo algorithm searched error space for
initial parameters prior to running the nonlinear solvers, this problem
could be strongly mitigated.  This meant that instead of hit-or-miss
forward and backward regression, large numbers of known linear *and*
nonlinear equations could be fitted to an experimental data set, and
then ranked by a fit statistic such as AIC or SSQ errors.

Note that for an initial guesstimate of parameter values, not all data
need be used.  A reduced size data set with min, max, and (hopefully)
evenly spaced additional data points in between are used.  The total
number of data points required is the number of equation parameters
plus a few extra points.

Reducing the data set size used by the code's genetic algorithm greatly
reduces total processing time.  I tested many different methods before
choosing the one in the code, a genetic algorithm named
"Differential Evolution".


I hope you find this code useful, and to that end I have sprinkled
explanatory comments throughout the code.  If you have any questions
or comments, please e-mail me directly at zunzun@zunzun.com
or by posting to the user group at the URL
https://groups.google.com/forum/#!forum/zunzun_dot_com

James R. Phillips
2548 Vera Cruz Drive
Birmingham, AL 35235 USA

email: zunzun@zunzun.com
