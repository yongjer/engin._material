from cmath import pi
import matplotlib.pyplot as plt
import numpy as np
diameter = 12.8
init_length = 50.8
stress = lambda x: x / (((diameter/2)*(10**(-3)))**2 * np.pi) * (10**(-6))
strain = lambda x: (x-init_length) / init_length
force = np.array([12700, 25400, 38100, 50800, 76200, 89100, 92700, 102500, 107800, 119400, 128300, 149700, 159000, 160400, 159500, 151500, 124700])
length = np.array([50.825, 50.851, 50.876, 50.902, 50.952, 51.003, 51.054, 51.181, 51.308, 51.562, 51.816 ,52.832, 53.848, 54.356, 54.864, 55.880, 56.642])
lines = plt.plot(strain(length), stress(force))
plt.xlabel("strain")
plt.ylabel("stress (MPa)")
plt.setp(lines, marker = "o")
plt.show()
