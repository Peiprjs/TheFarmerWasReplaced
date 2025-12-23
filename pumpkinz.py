from functions import *

desiredWaterLevel = 0.4
pumpkinSize = 0
goToBeginning()

while True:
	for i in range(get_world_size()):
		if pumpkinSize == get_world_size()**2:
			harvest()
			pumpkinSize = 0
		if not plantGrassland(Entities.Pumpkin):
			pumpkinSize += 1
				
		if get_water() < desiredWaterLevel:
			use_item(Items.Water)
		
	
		move(North)
	move(East)
	