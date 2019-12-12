import numpy as np

import matplotlib.pyplot as plt

axes_values = np.arange(-100, 100, 10)

dx, dy = np.meshgrid(axes_values, axes_values)
# print('dx is')
# print(dx)

# print('dy is')
# print(dy)

function = 2 * dy + 3 * dx
function2 = np.cos(dx) + np.cos(dy)
print(function)

# plt.imshow(function)
# plt.title('function of plot 2* dy + 3* dx')
# plt.colorbar()
# plt.savefig('myfig.png')

plt.imshow(function2)
plt.title('function of cos plot')
plt.colorbar()
plt.savefig('myfig2.png')



