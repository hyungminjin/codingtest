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

n, k = map(int, input().split())

# 반복으로 n만큼의 수를 입력받고
# 입력받은 수를 조건문으로 나눠서 k를 나눈다. -> 몫을 구하는 과정이 필요할 것 같음
# n개의 줄에 동전의 가치가 오름차순으로 주어지게 되면 입력을 받는게 아니라 주어지는 것인가?

# 입력을 받는다. -> 배열에 저장한다. -> 오름차순으로 순서를 맞춘다.
# k를 입력받은 배열의 index로 나눌 때 몫과 나머지를 따진다.
a = []

# 오름차순 정렬 없이 오름차순으로 입력을 한다고 가정했을 때 a[i] = num까지만 입력받는다.
for i in range(n):
    num = int(input())
    a[i] = num

if k // a[n-1] > 1:
    k = k % a[n-1]

elif k // 




