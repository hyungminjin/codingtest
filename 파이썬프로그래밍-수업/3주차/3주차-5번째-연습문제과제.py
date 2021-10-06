# 1. 사용자로부터 두 개의 정수를 받아서 정수의 합, 정수의 차, 정수의 곱, 정수의 평균, 큰 수, 작은 수를 계산하여 화면에 출력하는 프로그램을 작성하라.
# 파이썬이 제공하는 내장 함수 max(x, y), min(x, y)을 사용해보자.
print("두 정수 x와 y를 입력하시오.")
x,y = map(int, input().split()) # 두 정수 입력 받기
sum = x + y # 정수의 합
minus = x - y# 정수의 차
multiple = x * y # 정수의 곱
avg = (x+y)/2 # 정수의 평균
max = max(x,y) # 큰 수
min = min(x,y) # 작은 수 

print("두 정수의 합: ",sum)
print("두 정수의 차: ",minus)
print("두 정수의 곱: ",multiple)
print("두 정수의 평균: ",avg)
print("큰 수: ",max)
print("작은 수: ",min)

# 완료

# 2. 원기둥의 부피를 계산하는 프로그램을 작성해보자. 원기둥의 부피는 다음과 같이 계산한다.

print("반지름과 높이를 입력하시오.")
r, h = map(int, input().split())
v = 3.141592*r**2*h
print("원기둥의 부피: ",v)

# 완료