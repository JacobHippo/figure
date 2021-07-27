import random
s = input('請使用者輸入範圍最小值')
e = input('請使用者輸入範圍最大值')
s =int(s)
e = int(e)
x = random.randint(s, e)
y = 0
while True:
    g = input('請猜數字')
    g = int(g)
    y = y + 1
    if g == x:
    	print('你猜對了')
    	break
    elif g > x:
    	print('比答案大')
    	print('這是你猜的第', y, '次')
    elif g < x:
    	print('比答案小')
    	print('這是你猜的第', y, '次')
print('你猜了', y, '次')
    