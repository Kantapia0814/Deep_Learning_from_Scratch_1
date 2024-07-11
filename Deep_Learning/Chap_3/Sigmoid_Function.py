import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)                 # plt.ylim(ymin, ymax), ymin: y축의 최소값, ymax: y축의 최대값. y축이 표시되는 최소값과 최대값을 지정
plt.show()