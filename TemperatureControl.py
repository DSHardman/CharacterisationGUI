import matplotlib.pyplot as plt

from scipy import interpolate
import numpy as np

# Resistances stored in kOhms
res = [150, 120, 100, 82, 75, 68, 56, 51, 43, 36, 33, 27, 22, 20, 18, 16, 13, 11, 8.2, 7.5, 5.6, 3.3, 1.6, 0.56]
# Temperatures stored in Celsius
temp = [15.5, 21, 25, 29, 31, 34, 38, 41, 45, 49.5, 52, 57, 63, 65, 68, 72, 78, 83, 92, 95, 105, 123, 153, 196]
f = interpolate.interp1d(res, temp)


resnew = np.arange(1, 150, 0.1)
tempnew = f(resnew)   # 1D interpolation
plt.plot(res, temp, 'o', resnew, tempnew, '-')
plt.show()