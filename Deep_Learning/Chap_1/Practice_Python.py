# 산술 연산
print(1 - 2)
print(4 * 5)
print(7 / 5)
print(3 ** 2)

# 자료형 (data type)
print(type(10))
print(type(2.718))
print(type("hello"))

# 변수 (variable)
x = 10
print(x)

x = 100
print(x)

y = 3.14
print(x * y)
print(type(x * y))

# 리스트 (List)
a = [1, 2, 3, 4, 5]
print(a)
print(len(a))       # 리스트의 길이 출력
print(a[0])         # 첫 원소에 접근
print(a[4])
a[4] = 99           # 값 대입
print(a)

print(a[0:2])       # 인덱스 0부터 2까지 얻기 (2번째는 포함하지 않는다)
print(a[1:])        # 인덱스 1부터 끝까지 얻기 
print(a[:3])        # 처음부터 인덱스 3까지 얻기 (3번째는 포함하지 않는다)
print(a[:-1])       # 처음부터 마지막 원소의 1개 앞까지 얻기
print(a[:-2])       # 처음부터 마지막 원소의 2개 앞까지 얻기

# 딕셔너리 (dictionary)
me = {'height' : 180}       # 딕셔너리 생성
print(me['height'])         # 원소에 접근
me['weight'] = 70           # 새 원소 추가
print(me)

# bool
hungry = True
sleepy = False

print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)

# if 문
hungry = True
if hungry:
    print("I'm hungry")

hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")

# for 문
for i in [1, 2, 3]:
    print(i)

# 함수 (function)
def hello():
    print("Hello World!")

hello()

def hello(object):
    print("Hello " + object + "!")

hello("cat")