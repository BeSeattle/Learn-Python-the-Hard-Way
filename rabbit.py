for rabbit in range(1+35):
	for chicken in range(1+35):
		if rabbit + chicken == 35 and rabbit*4+chicken*2==94:
			print 'Chicken:%s,Rabbit:%s' %(chicken,rabbit)
