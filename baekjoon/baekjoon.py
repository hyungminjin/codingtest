# 백준 2577번 

# a = int(input())
# b = int(input())
# c = int(input())

# x = list(str(a*b*c))

# # 배열안의 값을 0~9까지 하나씩 검증하기

# # 121321312313

# i = 0
# for i in range(10):    
#     print(x.count(str(i)))

# => 왜 str이 들어가고 이 코드가 답이 되는지 이해가 안된다. 이거 꼭 이해하기..!

# 백준 3052번

# 생각 : 일단 리스트로 10개의 수를 받는다.
# 각 인덱스를 42로 나눈다. 그 값을 해당 인덱스에 다시 저장한다.


# 3052번
# i = 0

# for i in 10:
#     n = list(int(input()))
#     n[i] = n [i]% 42

# result = 0

# while True:
#     if n[i] != n[1-i] and n[2] and n[3] and n[4] and n[5] and n[6] and n[7] and n[8] and n[9]:
        
# arr = []
# for i in range(10):
#     n = int(input())
#     arr.append(n%42)
# arr = set(arr)
# print(len(arr))

# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

n = int(input())

for i in n:
    a = list(int(input()))
    
