#!/usr/bin/env python
#-*- coding: utf-8 -*-


print("Coffee \n -메뉴-")
print("1: 아메리카노 2,000원 \n 2: 핫초코 2,500원\n 3: 자몽 허니 블랙티 4,300원 \n 4: 피치&레몬 블랜디드 5,800원")

print("=============================")


coffee_price=0
total_price=0
change=0

order=int(input("커피 종류를 선택하세요. 번호 입력 >>>"))

if order==1:
	coffee_price = 2000
elif order==2:
	coffee_price=2500
elif order==3:
   coffee_price=4300
elif order==4:
   coffee_price=5800
#print("[+debug 2] ", coffee_price)
count=int(input("몇 잔을 드릴까요? >>>"))
#print("[+debug 3] ", coffee_price)
total_price=coffee_price*count
#print("[+debug 4] ", coffee_price)


print("총 금액은 %s원 입니다." % total_price)

'''
주제: 거스름돈 로직 구현
'''
#1.사용자에게 받을 금액을 입력받는다.
received=int(input("돈을 투입해주세요 >>> "))


#2.입력받은 금액이 총금액과 크거나 작거나 

if received >= total_price:

#3.입력받은 총 금액보다 값이 큰 경우 (입력 값 - 총 금액)
	change = received - total_price
	print("거스름돈은 ", end='')
	print(int(change), end='')
	print("원 입니다.")

#4.입력받은 값이 총 금액보다 작은경우 
else:
	print("금액이 부족합니다. 주문이 취소되었습니다.")

  

'''
###문자열 출력을 다양하게 하는 방법들

#method 1.
	print("거스름돈은", int(change), "원 입니다.")
#method 2.
	print("거 스름돈은 %d원 입니다." % int(change))
#method 3.
	print("거스름돈은 "+str(int(change))+"원 입니다.")
'''










