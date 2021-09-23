# n, m = map(int, input().split())

# def today(n, m):
#     print(str(n)+'월'+str(m)+'일')

# today(n,m)

# def today(n,m):
#     print(n+'월'+m+'일')

# today(10,9)

# n, m = map(int, input().split())

# print(str(n)+'월'+str(m)+'일')
# # Q. print(숫자)하려면 print(str(숫자)) 이렇게 해야한다..? 맞다..
# # 그럼 문자열과 숫자 합쳤을 때는 str로 표시해주어야 하는데



#1. 입력은 없다.
#2. 무한 수열 & 10000보다 작은 값으로.

# 33 -> 33 + 3 + 3  = 39( => d(33))
# ex) 이런 함수를 정의한다고 했을 때 
# n = list(map(int, input().split()))

# def d(n):
#     i, y = 0
#     for i in range(len(n)): # n 리스트 길이만큼 돌고 n[i]로 n[0]부터 n[i]까지 더함
#         y += n[i]
#     return n + y

# d(n)

# def d(n):
#     n + n //1000 + n // 100 + n // 10 + n // 1
#     return d(n)

# for i in range(10000):
#     if d(i) == i + i //1000 + i // 100 + i //10 + i // 1:
#         continue
#     else:
#         print(d(i))

## 이런식으로 할 때는 배열에서 빼야하나

# natural_num = set(range(1,10001))
# generate_num = set()

# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generate_num.add(i)

# self_num = sorted(natural_num - generate_num)
# for i in self_num:
#     print(i)
# ==> 백준 4673번 - 함수
# https://wook-2124.tistory.com/252

# 11047번
# n, k = map(int, input().split())

# a = []

# for i in range(n):
#     inputnumber = int(input())
#     a.append(inputnumber)
# result = 0

# while(n<0):
#     k %= a[n]
#     n -= 1
#     result += 1

# print(result)


