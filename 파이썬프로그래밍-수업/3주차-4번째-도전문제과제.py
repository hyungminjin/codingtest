# 다음 프로그램 코드에 주석을 붙여보자.

money = int(input("투입한 돈: ")) # 투입할 돈을 입력 받음
price = int(input("물건 값: ")) # 물건 값을 입력 받음

change = money - price # 거스름 돈 :  투입할 돈 - 물건 값
coin500s = change // 500 # 거스름돈을 500원으로 나눈 몫. 즉 500원 개수
change = change % 500 # 500원으로 나눈 뒤 나머지. 500원짜리로 계산한 뒤 남은 돈
coin100s = change // 100 # 거스름돈을 100원으로 나눈 몫. 즉 100원 개수

print("500원 동전의 개수", coin500s) 
print("100원 동전의 개수", coin100s)