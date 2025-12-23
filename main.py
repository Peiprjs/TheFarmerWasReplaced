from functions import *

desiredWaterLevel = 0.4

goToBeginning()
	
while True:
	for i in range(get_world_size()):
		for e in range(get_world_size()):
			harvest()
			plant(Entities.Cactus)
			move(North)
			if get_water() < desiredWaterLevel:
				use_item(Items.Water)
		move(East)

