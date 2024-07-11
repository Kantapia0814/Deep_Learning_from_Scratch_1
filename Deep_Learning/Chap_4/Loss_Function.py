import numpy as np

def mean_squared_error(y, t):       # 평균 제곱 오차 (Mean squared error), 아웃라이어에 매우 민감, 회귀 문제에 사용
    return 0.5 * np.sum((y - t)**2)

def cross_entropy_error(y, t):      # 교차 엔트로피 오차 (Cross entropy error), 분류 문제에 사용
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

