import numpy as np

def step_function_1(x):
    if x > 0:
        return 1
    else:
        return 0
    
def step_function(x):
    y = x > 0
    return y.astype(int)     # 넘파이 배열의 데이터 타입을 정수형으로 변환. ex) [1.7, 2.5, 3.9] -> [1, 2, 3]

x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)