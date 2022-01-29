#!/usr/bin/env python
# -*- coding: utf-8 -*-



score = 50 #처음 스코어 점수 초기화

#게임의 문제를 출력한다
print(" ")
print("[+] Game Start")
print(" ")
intro_text="""
첫 번째 문제
[ 그녀는 항상 같은 시간에 스터디 카페에 온다. 들어오면  왠지 바로 공부하러 갈거 같아서 휴개실 앞에서 기다리기로 했다.]
"""
print(intro_text)

#사용자에게 입력을 받는다.
print("“유리야 안녕! 오늘도 진짜 덥다 그치?” \n")
print("“오 영택아 안녕! 맞아 진짜 더워. 나 집나갈 때 물마시고 나왔는데 벌써 갈증 난다?ㅋㅋㅋ \n”")
mission_1="""1. “나도 갈증 났는데 우리 아이스티 마실까? 내가 만들어줄게ㅎ” \n
2. “갈증? 계속 갈증이 나는 이유는 말이야. 첫 번째로 탈수 증상일 수 있어. 그래서 그런데 휴개실 가서 음료수 마실래? \n
3. “그럼 시원한거 마시자! 아이스티 어때?”\n """

select_value=input(">> ")
#print("[1] debug code : ",select_value)

#print("[1] debug code")
#사용자의 입력에 따라 조건을 나눈다
if select_value == 1:
	score=score+10
	print("호감도 ▲ (상승+10)")
elif select_value == 2:
	print("호감도 - 변화없음")
	pass
else:
	score=score+10
	print("호감도 ▲ (상승+10)")
#print("[2] debug code")
print("현재 호감도는 : " + str(score))
#print("[3] debug code")

mission_2 = ''' 두 번째 문제
[그녀와 함께 휴개실로 들어왔다. 둘만 있으니 긴장 된다. 일단 아이스티 만드는 거에 집중하자. 여기에 있는 아이스티는 원액으로만 있어서 몇번 펌프할지에 따라 맛이 달라진다.] 

“유리야 너는 아이스티 진한게 좋아 평범한게 좋아?”
“음.. 나는 진한게 좋아!”
<선택>
1. 5번 펌프한다. 
2. 10번 펌프한다.
3. 20번 펌프한다. 
'''
print(mission_2)

select_value=input(">> ")
#사용자의 입력에 따라 조건을 나눈다
if select_value == 1:
	score= score - 10
	print("호감도 ▼(하락)")
elif select_value == 2:
	print("호감도 - 변화없음")
	pass
else:
	score=score+10
	print("호감도 ▲ (상승+10)")
#print("[2] debug code")
print("현재 호감도는 : " + str(score))
#print("[3] debug code")

mission_3 = ''' 세 번째 문제
[아이스티 원액은 넣었다. 그다음에 얼음이랑 물을 넣을 차례다. 그녀는 시원하게 좋다고 했다]
<선택>
1. 얼음만 넣는다.
2. 얼음과 물을 넣는다.
3. 물만 넣는다. 
'''
print(mission_3)
select_value=input(">> ")
#사용자의 입력에 따라 조건을 나눈다
if select_value == 1:
	score=score+10
	print("호감도 ▲ (상승+10)")
elif select_value == 2:
	print("호감도 - 변화없음")
	pass
else:
	score=score+10
	print("호감도 ▲ (상승+10)")
#print("[2] debug code")
print("현재 호감도는 : " + str(score))
#print("[3] debug code")


mission_4 = ''' 네 번째 문제 
[이제 거의 다 됐다! ]
<선택>
1. 스푼으로 섞어서 그녀에게 준다.
2. 따로 섞지 않고 그대로 그녀에게 준다.
3. 내가 마신다.'''
print(mission_4)
select_value=input(">> ")
#사용자의 입력에 따라 조건을 나눈다
if select_value == 1:
	score=score+10
	print("호감도 ▲ (상승+10)")
elif select_value == 2:
	print("호감도 - 변화없음")
	pass
else:
	score=score+10
	print("호감도 ▲ (상승+10)")
#print("[2] debug code")
print("현재 호감도는 : " + str(score))
#print("[3] debug code")

'''









'''