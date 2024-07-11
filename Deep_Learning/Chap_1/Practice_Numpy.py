import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

# 넘파이의 산술 연산
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x / 2.0)

# 넘파이의 N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)

print(A)
print(A * 10)

# 브로드캐스트
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

for row in X:
    print(row)

X = X.flatten()                 # X를 1차원 배열로 변환 (평탄화)
print(X)
print(X[np.array([0, 2, 4])])   # 인덱스가 0, 2, 4인 원소 얻기

print(X > 15)
print(X[X > 15])                # 값이 15보다 큰 원소만 꺼내기
