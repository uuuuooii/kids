#!/usr/bin/env python
#-*- coding: utf-8 -*-


print("Coffee \n -메뉴-")
print("1: 아메리카노 2,000원 \n 2: 핫초코 2,500원\n 3: 자몽 허니 블랙티 4,300원 \n 4: 피치&레몬 블랜디드 5,800원")

print("=============================")


coffee_price=0
total_price=0

order=input("커피 종류를 선택하세요. 번호 입력 >>>")
if order==1:
	coffee_price = 2000

elif order==2:
	coffee_price=2500

elif order==3:
   coffee_price=4300
elif order==4:
   coffee_price=5800

count=int(input("몇 잔을 드릴까요? >>>"))
total_price= coffee_price*count

#print(total_price)
#print("원 입니다.")

total= int(input(f"총 금액은 {total_price}원 입니다."))









