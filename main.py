while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)
	move(East)
	for i in range(2):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			move(North)
		move(East)
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(North)
	move(East)