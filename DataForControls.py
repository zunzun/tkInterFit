import collections

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

# item[display string] = [code name string, extended version name string, additional parameters string]
eq_od2D = collections.OrderedDict()
eq_od2D['Linear Polynomial'] = ['Polynomial.Linear', 'Default', '', '']
eq_od2D['Quadratic Polynomial'] = ['Polynomial.Quadratic', 'Default', '', '']
eq_od2D['Cubic Polynomial'] = ['Polynomial.Cubic', 'Default', '', '']
eq_od2D['Witch Of Maria Agnesi A'] = ['Miscellaneous.WitchOfAgnesiA', 'Default', '', '']
eq_od2D['Lorentzian Peak C With Offset'] = ['Peak.LorentzianPeakC', 'Offset', '', '']
eq_od2D['Gamma Ray Angular Distribution (degrees) B'] = ['LegendrePolynomial.GammaRayAngularDistributionDegreesB', 'Default', '', '']
eq_od2D['Exponential With Offset'] = ['Exponential.Exponential', 'Offset', '', ''] # NOT default extended version string

# item[display string] = [code name string, extended version name string, additional parameters string]
eq_od3D = collections.OrderedDict()
eq_od3D['Linear Polynomial'] = ['Polynomial.Linear', 'Default', '', '']
eq_od3D['Full Quadratic Polynomial'] = ['Polynomial.FullQuadratic', 'Default', '', '']
eq_od3D['Full Cubic Polynomial'] = ['Polynomial.FullCubic', 'Default', '']
eq_od3D['Monkey Saddle A With Offset'] = ['Miscellaneous.MonkeySaddleA', 'Offset', '', ''] # NOT default extended version string
eq_od3D['Gaussian Curvature Of Whitneys Umbrella A'] = ['Miscellaneous.GaussianCurvatureOfWhitneysUmbrellaA', '', '']
eq_od3D['NIST Nelson Autolog'] = ['NIST.NIST_NelsonAutolog', 'Default', '', '']
eq_od3D['Custom Polynomial One'] = ['Polynomial.UserSelectablePolynomial', 'Default', ', 3, 1']

