americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수: "))
cafelattes = int(input("카페라테 판매 개수 : "))
capucinos = int(input("카푸치노 판매 개수: "))

sales = americanos*americano_price
sales = sales + cafelattes*cafelatte_price
sales = sales + capucinos*capucino_price
total_price = sales - 100,000

# if (total_price > 0):
#     print("흑자입니다.")
# else:
#     print("적자입니다.")
## => 이 부분이 왜 틀린거지?


print("총 매출은", sales, "입니다.")




# 아메리카노 판매 개수 10
# 카페라떼 판매 개수 : 20
# 카푸치노 판매 개수 : 30
# 총 매출 185,000원

# 도전문제 : 총 재료 비용이 100,000원이었다고 하자. 이익을 계산해보자. 적자인지, 흑자인지 표시하라.


