# python guessing number
# 產生一個隨機整數0~100
# 讓使用者重複輸入數字去猜
# 猜對的話 '印出終於猜對了！''
# 猜錯的話 要告訴他 比答案大/小

import random
start = input('key in start number.')
end = input('key in end number.')
start = int(start)
end = int(end)
num_r = random.randint(start,end)
count = 0
while True:
	count +=1 # count = count + 1
	print('The number is between:', start, '~', end)
	num_input = input('請猜數字＝？')
	num_input = int(num_input)
	if num_input == num_r:
		print('印出終於猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif num_input > num_r:
		print('比答案大')
	elif num_input < num_r:
		print('比答案小')
	print('這是你猜的第', count, '次')