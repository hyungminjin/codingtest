# 연습문제 5번
print("기호를 입력하시오: ")
c = input()
print("중간에 삽입할 문자열을 입력하시오 : ")
d = input()
print(c[0]+d+c[1])

# 연습문제 6번
list = ['1','2','3','4']
sum = int(list[0])+int(list[1])+int(list[2])+int(list[3])
print("리스트 숫자들의 합 = ",sum) 

# 연습문제 7번
import turtle
t = turtle.Turtle()
t.shape("turtle")

color = [0] * 3
color[0] = input("색상 1을 입력:")
color[1] = input("색상 2을 입력:")
color[2] = input("색상 3을 입력:")

t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()

t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()

t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()

