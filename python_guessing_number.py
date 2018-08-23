# python guessing number
# 產生一個隨機整數0~100
# 讓使用者重複輸入數字去猜
# 猜對的話 '印出終於猜對了！''
# 猜錯的話 要告訴他 比答案大/小

import random
num_r = random.randint(0,100)
count = 0
while True:
	count +=1 # count = count + 1
	num_input = input('請猜數字＝？(0~100)')
	num_input = int(num_input)
	if num_input == num_r:
		print('印出終於猜對了！')
		break
	elif num_input > num_r:
		print('比答案大')
	elif num_input < num_r:
		print('比答案小')
	print('這是你猜的第', count, '次')