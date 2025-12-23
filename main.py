for i in range(get_pos_x()):
	move(West)

for i in range(get_pos_y()):
	move(South)
	
while True:
	# One row of wheat
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)
		
	move(East)
	
	# Two rows of wood
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_y() % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Grass)
			if get_water() < 0.5:
				use_item(Items.Water)
		move(North)
	move(East)

	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_y() % 2 == 0:
				if get_ground_type() == Grounds.Soil:
					till()
				plant(Entities.Carrot)
			else:
				plant(Entities.Tree)
			if get_water() < 0.5:
				use_item(Items.Water)
		move(North)
	move(East)

	
	# One row of carrots
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(North)
	move(East)