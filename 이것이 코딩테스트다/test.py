# n, m = map(int, input().split())


# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
    
#     result = max(result, min_value)

# ==> n으로 나눈 뒤 m 까지 고려해서 나눠야 하는 줄알았다. 그래서 for i in rang(n)쓰고 for j in range(m) 을 썼다.
# ==> 10001 이거를 왜 사용하는가? : 임의의수 지정한 뒤 다음에 나오는 최솟값과 비교하기 위해서 


# print(result)

# for i in range(n):
#     for j in range(m):
#         data = list(map(int, input().split()))
#         min(data)

# 구현 상하 좌우
# n = int(input())
# a = list(map(input().split()))
# x,y = (1, 1)
# L = (x - 1, y)
# R = (x + 1, y)
# U = (x, y + 1)
# D = (x, y - 1)
# x,y에 LRUD를 넣어야 할 꺼같은데
# x, y가 1,y | x,y = x,1 | x,y = 1,n | x,y = n,1 일 때
# x,y = x,y

# 1. n값을 받는다.
# 2. x y 좌표를 주고 L R U D 를 지정한다.
# => 이렇게 한번에 받는 것은 배열로 지정하여 구현하는게 더 빠르고 좋을 것 같다.

# 계획 확인을 해야 한다. -> 이걸 반복문으로




n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# = > 튜플 형식으로 저장해서 이렇게 깔끔하게 표현할 수도 있구나.. 라는 생각
# 나는 전부 if를 써서 경우의 수를 다 나눠서 할 생각을 했는데 이 방법이 더 깔끔한 것 같다.
# 이동 계획을 하나씩 확인

for plan in plans:
    #이동 후 좌표
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue

    x, y = nx, ny

print(x,y)



