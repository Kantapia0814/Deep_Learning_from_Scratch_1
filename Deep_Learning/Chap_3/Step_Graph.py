import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype = int)     # NumPy 1.20.0 버전 이후로는 np.int가 아닌 int로 작성

x = np.arange(-5.0, 5.0, 0.1)               # -5.0에서 5.0까지 0.1 간격으로 생성된 배열
y = step_function(x)                        # step_function을 통해 x에 대응하는 결과 배열
plt.plot(x, y)                              # x와 y를 사용하여 그래프를 그림
plt.ylim(-0.1, 1.1)                         # y축의 범위를 설정하여 그래프가 보기 좋게 함
plt.show()