# 반대로 섭씨온도를 화씨온도로 변호한하는 프로그램도 작성해보자.

# ftemp = int(input("화씨온도: "))
# ctemp = (ftemp-32)*5/9
# print("섭씨온도:", ctemp)



ctemp = int(input("섭씨온도: "))
ftemp = ctemp*9.0/5.0 + 32.0
print("화씨온도:",ftemp,"F")


# 9 ctemp = (ftemp-32) * 5
# 9ctemp/5 = ftemp - 32
# 9 ctemp / 5 + 32 = ftemp


# 완료