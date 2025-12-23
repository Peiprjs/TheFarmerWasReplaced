def goToBeginning():
	for i in range(get_pos_x()):
		move(West)
		 
	for i in range(get_pos_y()):
		move(South)

def plantGrassland(entity):
	harvest()
	if get_ground_type() == Grounds.Grassland:
		till()
	if plant(entity):
		return True
	else: 
		return False
	
def get_pumpkin_requirements(desiredPrerequisites):
	while num_items(Items.Power) < 2500:
		if get_entity_type() != Entities.Sunflower:
			for i in range(get_world_size()):
				for e in range(get_world_size()):
					plantGrassland(Entities.Sunflower)
					move(North)
				move(East)
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				harvest()
				plantGrassland(Entities.Sunflower)
				move(North)
			move(East)
	while num_items(Items.Hay) < desiredPrerequisites:
		if get_entity_type() != Entities.Grass:
			for i in range(get_world_size()):
				for e in range(get_world_size()):
					plantGrassland(Entities.Grass)
					move(North)
				move(East)
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				harvest()
				plant(Entities.Grass)
				move(North)
			move(East)
	while num_items(Items.Wood) < desiredPrerequisites:
		if get_entity_type() != Entities.Bush:
			for i in range(get_world_size()):
				for e in range(get_world_size()):
					plant(Entities.Bush)
					move(North)
				move(East)
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				harvest()
				plant(Entities.Bush)
				move(North)
			move(East)
	while num_items(Items.Carrot) < desiredPrerequisites:
		if get_entity_type() != Entities.Carrot:
			for i in range(get_world_size()):
				for e in range(get_world_size()):
					plantGrassland(Entities.Carrot)
					move(North)
				move(East)
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				harvest()
				plantGrassland(Entities.Carrot)
				move(North)
			move(East)
