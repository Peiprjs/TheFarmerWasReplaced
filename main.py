from functions import *

desiredWaterLevel = 0.4

goToBeginning()
	
while True:
	do_a_flip()
	for i in range(2):
	# One row of wheat
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
			move(North)
		move(East)
		# Three rows of wood
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_pos_y() % 2 == 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Grass)
				if get_water() < desiredWaterLevel:
					use_item(Items.Water)
			move(North)
		move(East)

		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_pos_y() % 2 == 0:
					plantGrassland(Entities.Carrot)
				else:
					plant(Entities.Tree)
				if get_water() < desiredWaterLevel:
					use_item(Items.Water)
			move(North)
		move(East)

		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_pos_y() % 2 == 0:
					plant(Entities.Tree)
				else:
					plantGrassland(Entities.Sunflower)
				if get_water() < desiredWaterLevel:
					use_item(Items.Water)
			move(North)
		move(East)


		
		# One row of carrots
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				plantGrassland(Entities.Carrot)
				if get_water() < desiredWaterLevel:
					use_item(Items.Water)
			move(North)
		move(East)

		# One row of sunflowers
		for i in range(get_world_size()):
			if get_entity_type() == Entities.Sunflower:
				if measure() >= 7:
					harvest()
					plant(Entities.Sunflower)
					if get_water() < desiredWaterLevel:
						use_item(Items.Water)
			else:
				plantGrassland(Entities.Sunflower)
			move(North)
		move(East)