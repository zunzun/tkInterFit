links = '''
URL for animated "Common Problems In Curve Fitting":
http://commonproblems.readthedocs.io/

URL for source code of this computer program:
https://github.com/zunzun/tkInterFit

URL for web version of this code, which generates \
PDF files and animated 3D surface rotations:
https://github.com/zunzun/zunzunsite3

URL for the pyeq3 fitting library, which has hundreds \
of known 2D and 3D equations:
https://github.com/zunzun/pyeq3


'''

author = '''
This is James Phillips, author of tkInterFit. My background is in \
nuclear engineering and industrial radiation physics, as I started \
working in the U.S. Navy as a submarine nuclear reactor operator \
many, many neutrons ago.

I have quite a bit of international experience calibrating industrial \
metal thickness and coating gauges. For example the thicker a piece of \
steel the more radiation it absorbs, and measuring the amount of radiation \
that passes through a sheet of steel can tell you how thick it is without \
touching it. Another example is that the thicker a zinc coating on steel \
sheets, the more zinc X-ray fluorescence energy it can emit - again allowing \
accurate thickness measurement for industrial manufacture.

My post-Navy employer originally used ad-hoc spreadsheets to very \
tediously create 4th-order polynomials calibrating to readings from \
known samples. So I started writing my own curve-fitting software in C.

When X-rays pass through aluminium, the atomic number of the alloying \
elements is much greater than that of the aluminium itself such that \
small changes in alloy composition lead to large changes in X-ray \
transmission for the same thickness. Alloy changes look like thickness \
changes, egad! However, alloy changes also cause changes to the X-rays \
that are scattered back from the aluminium, so that if both the transmitted \
and backscattered radiation is measured a more alloy-insensitive thickness \
measurement can be made - but this is now a 3D surface fit, and I started \
writing surface fitting software. I began to do considerable international work.

This finally led to the development of my Python fitting libraries, and \
this example tkinter curve and surface fitter. I also have Python 2 and 3 \
wxPython and django versions on GitHub.

James
'''

history = '''
Prior to the invention of electronic calculation, only manual methods \
were available, of course - meaning that creating mathematical models \
from experimental data was done by hand.  Even Napier's invention of \
logarithms did not help much in reducing the tediousness of this task. \
Linear regression techniques worked, but how to then compare models? \
And so the F-statistic was created for the purpose of model selection, \
since graphing models and their confidence intervals was practically \
out of the question.  Forward and backward regression techniques used \
linear methods, requiring less calculation than nonlinear methods, but \
limited the possible mathematical models to linear combinations of functions.

With the advent of computerized calculations, nonlinear methods which \
were impractical in the past could be automated and made practical. \
However, the nonlinear fitting methods all required starting points \
for their solvers - meaning in practice you had to have a good idea of \
the final equation parameters to begin with!

If however a genetic or monte carlo algorithm searched error space for \
initial parameters prior to running the nonlinear solvers, this problem \
could be strongly mitigated.  This meant that instead of hit-or-miss \
forward and backward regression, large numbers of known linear *and* \
nonlinear equations could be fitted to an experimental data set, and \
then ranked by a fit statistic such as AIC or SSQ errors.

Note that for an initial guesstimate of parameter values, not all data \
need be used.  A reduced size data set with min, max, and (hopefully) \
evenly spaced additional data points in between are used.  The total \
number of data points required is the number of equation parameters \
plus a few extra points.

Reducing the data set size used by the code's genetic algorithm greatly \
reduces total processing time.  I tested many different methods before \
choosing the one in the code, a genetic algorithm named \
"Differential Evolution".


I hope you find this code useful, and to that end I have sprinkled \
explanatory comments throughout the code.  If you have any questions, \
comments or ridicule, please e-mail me directly at zunzun@zunzun.com \
or by posting to the user group at the URL
https://groups.google.com/forum/#!forum/zunzun_dot_com

I will be glad to help you.

James R. Phillips
2548 Vera Cruz Drive
Birmingham, AL 35235 USA

email: zunzun@zunzun.com
'''
