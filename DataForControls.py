import collections, inspect
import pyeq3

exampleText_2D = """\

Example 2D data for testing
Paste your own 2D data here

  X        Y
5.357    10.376
5.457    10.489
5.936    11.049
6.161    11.327 ending text is ignored
6.697    12.054
8.442    14.744
9.769    17.068
9.861    17.104
"""

exampleText_3D = """\

Example 3D data for testing
Paste your own 3D data here

    X       Y      Z
  3.017  2.175   0.0320
  2.822  2.624   0.0629
  1.784  3.144   6.570
  2.0 2.6 4.0  ending text is ignored
  1.712  3.153   6.721
  2.972  2.106   0.0313
  2.719  2.542   0.0643
  1.479  2.957   6.583
  1.387  2.963   6.744
  2.843  1.984   0.0315
  2.485  2.320   0.0639
  0.742  2.568   6.581
  0.607  2.571   6.753
"""

fittingTargetList = ['Lowest Sum Of Squared Absolute Error (SSQABS)',
                     'Lowest Sum Of Squared Log[Pred/Actual] (LNQREL)',
                     'Lowest Sum Of Squared Relative Error (SSQREL)',
                     'Lowest Sum Of Squared Orthogonal Distance (ODR)',
                     'Lowest Akaike Information Criterion (AIC)',
                     ]

# these require additional user input - available in zunzunsite3 but not this project
excludedModuleNames_2D = [
    'Polyfunctional',
    'Rational',
    'Spline',
    'UserDefinedFunction',
]
excludedModuleNames_3D = [
    'Polyfunctional',
    'Spline',
    'UserDefinedFunction',
]

eq_od2D = collections.OrderedDict()
for submodule in inspect.getmembers(pyeq3.Models_2D):
    if inspect.ismodule(submodule[1]):
        if submodule[0] in excludedModuleNames_2D:
            continue
        eq_od2D[submodule[0]] = collections.OrderedDict()
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                for extendedVersionName in ['Default', 'Offset']:
                    
                    # if the equation *already* has an offset,do not add an offset version here
                    if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                        continue
                        
                    # if the equation requires special user input, exclude here
                    if equationClass[1].userSelectablePolynomialFlag or \
                       equationClass[1].userCustomizablePolynomialFlag or \
                       equationClass[1].userSelectableRationalFlag:
                        continue

                    equation = equationClass[1]('SSQABS', extendedVersionName)
                    equationName = equation.GetDisplayName()                    
                    eq_od2D[submodule[0]][equationName] = [equationClass[0], extendedVersionName]


eq_od3D = collections.OrderedDict()
for submodule in inspect.getmembers(pyeq3.Models_3D):
    if inspect.ismodule(submodule[1]):
        if submodule[0] in excludedModuleNames_3D:
            continue
        eq_od3D[submodule[0]] = collections.OrderedDict()
        for equationClass in inspect.getmembers(submodule[1]):
            if inspect.isclass(equationClass[1]):
                for extendedVersionName in ['Default', 'Offset']:
                    
                    # if the equation *already* has an offset,do not add an offset version here
                    if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                        continue
                        
                    # if the equation requires special user input, exclude here
                    if equationClass[1].userSelectablePolynomialFlag or \
                       equationClass[1].userCustomizablePolynomialFlag or \
                       equationClass[1].userSelectableRationalFlag:
                        continue

                    equation = equationClass[1]('SSQABS', extendedVersionName)
                    equationName = equation.GetDisplayName()                    
                    eq_od3D[submodule[0]][equationName] = [equationClass[0], extendedVersionName]
