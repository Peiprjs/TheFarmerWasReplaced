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

def waterPlant(max_water=0):
	if get_water() < max_water:
		while get_water() < max_water + 0.2:
			use_item(Items.Water)
		return True
	else:
		return False

def get_pumpkin_requirements(desPre):
	min_req = get_world_size()**2 * 32
	min_req = desPre
	while num_items(Items.Power) < 2500:
		for i in range(get_world_size()):
			for e in range(get_world_size()):
				if get_entity_type() != Entities.Sunflower:
					plantGrassland(Entities.Sunflower)
				harvest()
				plantGrassland(Entities.Sunflower)
				waterPlant()
				move(North)
			move(East)

	if num_items(Items.Hay) < min_req:
		while num_items(Items.Hay) < desPre:
			for i in range(get_world_size()):
				harvest()
				plant(Entities.Grass)
				waterPlant()
				move(North)
			move(East)

	if num_items(Items.Wood) < min_req:
		while num_items(Items.Wood) < desPre:
			for i in range(get_world_size()):
				harvest()
				plant(Entities.Bush)
				waterPlant()
				move(North)
			move(East)

	if num_items(Items.Carrot) < min_req:
		while num_items(Items.Carrot) < desPre:
			for i in range(get_world_size()):
				for e in range(get_world_size()):
					harvest()
					plantGrassland(Entities.Carrot)
					waterPlant()
					move(North)
				move(East)