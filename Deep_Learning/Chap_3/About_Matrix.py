import numpy as np

A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))       # 배열 A의 차원을 출력
print(A.shape)          # 배열의 각 차원 크기를 튜플 형태로 반환
print(A.shape[0])

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))
print(B.shape)