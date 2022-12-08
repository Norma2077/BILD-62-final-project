import numpy as np
def wav(x):
    max=numpy.max(x)
    min=numpy.min(x)
    y=np.linspace(max,min,1000)
    return y