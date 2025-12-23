from functions import *

desiredWaterLevel = 0.4
currentPumpkinSize = 0
desiredPumpkinSize = 5
goToBeginning()

while True:
	for i in range(5):
		for i in range(5):
			if currentPumpkinSize == get_world_size()**2:
				harvest()
				currentPumpkinSize = 0
			if not plantGrassland(Entities.Pumpkin):
				currentPumpkinSize += 1
					
			if get_water() < desiredWaterLevel:
				use_item(Items.Water)
			
		
			move(North)
		for i in range(5):
			move(North)
		move(East)
	