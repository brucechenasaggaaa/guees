import random

r = random.randint(1, 3)
while True:
	 num =input('請猜數字1~3: ')
	 num = int(num)
	 if num == r:
	 	print('答對')
	 	break
	 else:
	 	print('答錯')
