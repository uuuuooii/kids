#!/usr/bin/env python
#-*- coding: utf-8 -*-


user= input("1번 접수하기 \n2번 결제하기\n")

if user ==1:
	print("성함, 생년월일, 전화번호를 입력해주세요")
if user ==2:
	print("성함, 생년월일, 전화번호를 입력해주세요")





select= input(">>")

if user ==1:
	print("접수되셨습니다")
if user ==2:
	my_string=' 님 수고하셨습니다.\n 오늘은 를 치료하셨습니다. \n약 처방은 '

	split_string=my_string.split()
	split_string.insert(4, '충치')
	split_string.insert(0, '은혜')
	split_string.insert(9, '없습니다.')

	final_string=''.join(split_string)

	print(final_string)
 	print("진료 비용은 총80,000원 입니다.")
 	
 	from time import sleep
 	sleep(3)

 	print("결제 되셨습니다. 감사합니다.")



#sick=(충치)
#sick=(임플란트)
#sick=(스케일링)

