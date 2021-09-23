import sys
n = int(sys.stdin.readline())

stack = []


## 함수 정의 ##
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return (-1)
    else:
        stack.pop()
        return (stack[-1])
    
def size():
    return (len(stack))

def empty():
    if len(stack) == 0:
        return (1)
    else:
        return (0)

def top():
    if len(stack) == 0:
        return (-1)
    else:
        return (stack[-1])

for i in range(n):
    e = sys.stdin.readline()  
    print(e)

