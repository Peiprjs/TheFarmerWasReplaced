for i in range(get_pos_x()):
	move(West)

for i in range(get_pos_y()):
	move(South)
	
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
				if get_water() < 0.5:
					use_item(Items.Water)
			move(North)
		move(East)
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(North)
	move(East)