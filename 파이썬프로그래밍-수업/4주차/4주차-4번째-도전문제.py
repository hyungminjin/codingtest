import time

now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는 ", thisYear,"입니다.")
age = int(input("몇 살이신지요?"))

print("2050년에는 ", age + 2050 - thisYear, "살 이시군요.")

# str대신 쉼표를 사용하여 변수와 문자열을 동시 출력할 수 있습니다.

# 개인적인 생각으로는 ,가 str보다 간단하고 훨씬 편리하다고 생각합니다.