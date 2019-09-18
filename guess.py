import random
start = input('請決定數字範圍初始值: ')
end = input('請決定數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(1, 3)
count = 0
while True:
	 count += 1 # count = count + 1
	 num =input('請猜數字: ')
	 num = int(num)
	 if num == r:
	 	print('答對')
	 	print('這是你猜的第', count, '次')
	 	break
	 elif num > r:
	 	print('比答案大')
	 elif num < r:
	 	print('比答案小')
	 print('這是你猜的第', count, '次')	